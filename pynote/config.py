import functools
import pathlib
import typing

import confboy


@functools.cache
def get_note_path():
    return pathlib.Path.home() / '.notes'


config = confboy.Config(
    {
        'note_path': 'callable:get_note_path',
    },
    callables={
        'get_note_path': {
            'func': get_note_path,
            'kwargs': {},
        },
    },
    toml_config_path=pathlib.Path.home() / '.pynote.cfg',
)


def __getattr__(name: str) -> typing.Any:
    return config.__getattr__(name)
