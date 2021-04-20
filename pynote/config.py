import pathlib
import typing

import confboy


config = confboy.Config(
    {
        'note_path': f'{pathlib.Path.home() / ".notes"}',
        'edit_args': [
            'nvim', '-c', '"set syntax=markdown"', '{PATH}',
        ],
        'view_args': [
            'bat', '--file-name', '{TITLE}', '-l', 'markdown', '{PATH}',
        ],
    },
    toml_config_path=pathlib.Path.home() / '.pynote.cfg',
)


def __getattr__(name: str) -> typing.Any:
    return config.__getattr__(name)
