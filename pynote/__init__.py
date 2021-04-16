import typer

from . import engine


app = typer.Typer()


def terminate(message: str) -> None:
    typer.echo(message, err=True)
    raise typer.Exit(code=1)


@app.command()
def edit(
    title: str = typer.Argument(
        ...,
        help='Title of the note to edit.',
        autocompletion=engine.list_notes,
    ),
):
    """Create or edit note with TITLE."""

    try:
        engine.edit_note(title)
    except engine.NotePathIsFile:
        terminate(f'{engine.NOTE_PATH} exists and is not a directory.')
    except engine.NoteNotSaved:
        terminate(f'Could not save note at {engine.NOTE_PATH / title}.')


@app.command()
def view(
    title: str = typer.Argument(
        ...,
        help='Title of the note to view.',
        autocompletion=engine.list_notes,
    ),
):
    """View note with TITLE."""

    try:
        engine.view_note(title)
    except engine.NotePathIsFile:
        terminate(f'{engine.NOTE_PATH} exists and is not a directory.')
    except engine.NoteDoesNotExist:
        terminate(f'Note at {engine.NOTE_PATH / title} does not exist.')


@app.command()
def delete(
    title: str = typer.Argument(
        ...,
        help='Title of the note to delete.',
        autocompletion=engine.list_notes,
    ),
    force: bool = typer.Option(
        ...,
        help='Delete without confirmation.',
        prompt='You sure?',
    ),
):
    """Delete note with TITLE.

    If --force is not used, will ask for confirmation.
    """

    if not force:
        terminate('Deletion cancelled.')

    try:
        engine.delete_note(title)
    except engine.NotePathIsFile:
        terminate(f'{engine.NOTE_PATH} exists and is not a directory.')
    except engine.NoteDoesNotExist:
        terminate(f'Note at {engine.NOTE_PATH / title} does not exist.')
    except engine.NoteIsDirectory:
        terminate(f'Note at {engine.NOTE_PATH / title} is a directory.')


@app.command()
def list():
    """List available notes."""

    try:
        for note_name in engine.list_notes():
            typer.echo(note_name)
    except engine.NotePathIsFile:
        terminate(f'{engine.NOTE_PATH} exists and is not a directory.')
