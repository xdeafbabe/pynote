import subprocess
import unittest.mock

import pytest
import pytest_mock

import pynote.engine


def test_initialize(mocker: pytest_mock.MockerFixture):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isdir', return_value=True)

    mkdir = mocker.patch('os.mkdir')
    pynote.engine.initialize()
    mkdir.assert_not_called()


def test_initialize_not_a_dir(mocker: pytest_mock.MockerFixture):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isdir', return_value=False)

    with pytest.raises(pynote.engine.NotePathIsFile):
        pynote.engine.initialize()


def test_initialize_mkdir(mocker: pytest_mock.MockerFixture):
    mocker.patch('os.path.exists', return_value=False)
    mkdir = mocker.patch('os.mkdir')

    pynote.engine.initialize()
    mkdir.assert_called_once_with(pynote.engine.NOTE_PATH)


def test_edit_note(mocker: pytest_mock.MockerFixture):
    mocker.patch('pynote.engine.initialize')
    run = mocker.patch('subprocess.run')
    title = 'note_title'

    pynote.engine.edit_note(title)
    run.assert_called_once_with(
        [
            'nvim', '-c', 'set syntax=markdown',
            f'{pynote.engine.NOTE_PATH / title}',
        ],
        check=True,
        stderr=subprocess.DEVNULL,
    )


def test_edit_note_failure(mocker: pytest_mock.MockerFixture):
    mocker.patch('pynote.engine.initialize')
    mocker.patch(
        'subprocess.run',
        side_effect=subprocess.CalledProcessError(1, ''),
    )

    with pytest.raises(pynote.engine.NoteNotSaved):
        pynote.engine.edit_note('note title')


def test_view_note(mocker: pytest_mock.MockerFixture):
    mocker.patch('pynote.engine.initialize')
    run = mocker.patch('subprocess.run')
    title = 'note_title'

    pynote.engine.view_note(title)
    run.assert_called_once_with(
        [
            'bat', '--file-name', title, '-l', 'markdown',
            f'{pynote.engine.NOTE_PATH / title}',
        ],
        check=True,
        stderr=subprocess.DEVNULL,
    )


def test_view_note_failure(mocker: pytest_mock.MockerFixture):
    mocker.patch('pynote.engine.initialize')
    mocker.patch(
        'subprocess.run',
        side_effect=subprocess.CalledProcessError(1, ''),
    )

    with pytest.raises(pynote.engine.NoteDoesNotExist):
        pynote.engine.view_note('note title')


def test_delete_note(mocker: pytest_mock.MockerFixture):
    mocker.patch('pynote.engine.initialize')
    remove = mocker.patch('os.remove')
    title = 'note title'

    pynote.engine.delete_note(title)
    remove.assert_called_once_with(pynote.engine.NOTE_PATH / title)


def test_delete_note_directory(mocker: pytest_mock.MockerFixture):
    mocker.patch('pynote.engine.initialize')
    mocker.patch('os.remove', side_effect=IsADirectoryError)

    with pytest.raises(pynote.engine.NoteIsDirectory):
        pynote.engine.delete_note('note title')


def test_delete_note_nonexistent(mocker: pytest_mock.MockerFixture):
    mocker.patch('pynote.engine.initialize')
    mocker.patch('os.remove', side_effect=FileNotFoundError)

    with pytest.raises(pynote.engine.NoteDoesNotExist):
        pynote.engine.delete_note('note title')


def test_list_notes(mocker: pytest_mock.MockerFixture):
    mocker.patch('pynote.engine.initialize')

    filenames = ['one', 'two']
    files = []

    for filename in filenames:
        mock = unittest.mock.Mock()
        mock.name = filename
        files.append(mock)

    mocker.patch('os.scandir', return_value=files)
    mocker.patch('os.path.isdir', return_value=False)

    assert pynote.engine.list_notes() == filenames
