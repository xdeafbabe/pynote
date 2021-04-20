import os
import pathlib
import subprocess

from . import config


if isinstance(NOTE_PATH := config.note_path, str):  # pragma: no cover
    NOTE_PATH = pathlib.Path(NOTE_PATH)


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

    args = [
        arg.format(
            PATH=NOTE_PATH / title,
            TITLE=title,
        )
        for arg in config.edit_args
    ]

    try:
        subprocess.run(
            args,
            check=True,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as e:
        raise NoteNotSaved from e


def view_note(title: str) -> None:
    initialize()

    args = [
        arg.format(
            PATH=NOTE_PATH / title,
            TITLE=title,
        )
        for arg in config.view_args
    ]

    try:
        subprocess.run(
            args,
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
