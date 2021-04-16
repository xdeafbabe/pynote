import os
import pathlib
import subprocess


NOTE_PATH = pathlib.Path.home() / '.notes'


class NotePathIsFile(Exception):
    pass


class NoteNotSaved(Exception):
    pass


class NoteDoesNotExist(Exception):
    pass


class NoteIsDirectory(Exception):
    pass


def initialize() -> None:
    if os.path.exists(NOTE_PATH):
        if not os.path.isdir(NOTE_PATH):
            raise NotePathIsFile
    else:
        os.mkdir(NOTE_PATH)


def edit_note(title: str) -> None:
    initialize()

    try:
        subprocess.run(
            [
                'nvim',
                '-c',
                'set syntax=markdown',
                f'{NOTE_PATH / title}',
            ],
            check=True,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as e:
        raise NoteNotSaved from e


def view_note(title: str) -> None:
    initialize()

    try:
        subprocess.run(
            [
                'bat',
                '--file-name',
                title,
                '-l',
                'markdown',
                f'{NOTE_PATH / title}',
            ],
            check=True,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as e:
        raise NoteDoesNotExist from e


def delete_note(title: str) -> None:
    initialize()

    try:
        os.remove(NOTE_PATH / title)
    except IsADirectoryError as e:
        raise NoteIsDirectory from e
    except FileNotFoundError as e:
        raise NoteDoesNotExist from e


def list_notes() -> list[str]:
    initialize()

    return [
        note.name
        for note in os.scandir(NOTE_PATH)
        if not os.path.isdir(note)
    ]
