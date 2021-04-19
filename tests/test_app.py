import functools

import pytest
import pytest_mock
import typer
import typer.testing

import pynote


@pytest.fixture
def invoke():
    runner = typer.testing.CliRunner()
    return functools.partial(runner.invoke, pynote.app)


def test_terminate(mocker: pytest_mock.MockerFixture):
    echo = mocker.patch('typer.echo')
    message = 'message'

    with pytest.raises(typer.Exit):
        pynote.terminate(message)

    echo.assert_called_once_with(message, err=True)


def test_edit(mocker: pytest_mock.MockerFixture, invoke):
    edit = mocker.patch('pynote.engine.edit_note')
    title = 'note title'

    result = invoke(['edit', title])
    assert result.exit_code == 0
    edit.assert_called_once_with(title)


def test_edit_failure(mocker: pytest_mock.MockerFixture, invoke):
    mocker.patch(
        'pynote.engine.edit_note',
        side_effect=pynote.engine.NoteNotSaved,
    )

    result = invoke(['edit', 'note title'])
    assert result.exit_code == 1
    assert 'Could not save note at' in result.stdout


def test_view(mocker: pytest_mock.MockerFixture, invoke):
    view = mocker.patch('pynote.engine.view_note')
    title = 'note title'

    result = invoke(['view', title])
    assert result.exit_code == 0
    view.assert_called_once_with(title)


def test_view_failure(mocker: pytest_mock.MockerFixture, invoke):
    mocker.patch(
        'pynote.engine.view_note',
        side_effect=pynote.engine.NoteDoesNotExist,
    )

    result = invoke(['view', 'note title'])
    assert result.exit_code == 1
    assert ' does not exist.' in result.stdout


def test_delete(mocker: pytest_mock.MockerFixture, invoke):
    delete = mocker.patch('pynote.engine.delete_note')
    title = 'note title'

    result = invoke(['delete', '--force', title])
    assert result.exit_code == 0
    delete.assert_called_once_with(title)


def test_delete_directory(mocker: pytest_mock.MockerFixture, invoke):
    mocker.patch(
        'pynote.engine.delete_note',
        side_effect=pynote.engine.NoteIsDirectory,
    )

    result = invoke(['delete', '--force', 'note title'])
    assert result.exit_code == 1
    assert ' is a directory.' in result.stdout


def test_delete_nonexistent(mocker: pytest_mock.MockerFixture, invoke):
    mocker.patch(
        'pynote.engine.delete_note',
        side_effect=pynote.engine.NoteDoesNotExist,
    )

    result = invoke(['delete', '--force', 'note title'])
    assert result.exit_code == 1
    assert ' does not exist.' in result.stdout


def test_delete_confirm(mocker: pytest_mock.MockerFixture, invoke):
    mocker.patch('pynote.engine.delete_note')

    result = invoke(['delete', 'note_title'], input='y\n')
    assert result.exit_code == 0


def test_delete_no_confirm(invoke):
    result = invoke(['delete', 'note_title'], input='n\n')
    assert result.exit_code == 1
    assert 'Deletion cancelled.' in result.stdout


def test_list(mocker: pytest_mock.MockerFixture, invoke):
    notes = ['hello', 'slim_shady', 'groceries']
    mocker.patch('pynote.engine.list_notes', return_value=notes)
    cr = '\n'

    result = invoke(['list'])
    assert result.exit_code == 0
    assert result.stdout == f'{cr.join(notes)}{cr}'


@pytest.mark.parametrize(
    'args',
    [
        ['list'],
        ['edit', 'title'],
        ['view', 'title'],
        ['delete', '--force', 'title'],
    ],
)
def test_failed_init(
    mocker: pytest_mock.MockerFixture, invoke, args,
):
    mocker.patch(
        'pynote.engine.initialize',
        side_effect=pynote.engine.NotePathIsFile,
    )

    result = invoke(args)
    assert result.exit_code == 1
    assert ' exists and is not a directory.' in result.stdout
