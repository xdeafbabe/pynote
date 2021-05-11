# Pynote

[![codecov](https://codecov.io/gh/Euromance/pynote/branch/master/graph/badge.svg?token=aRfAPtBzsP)](https://codecov.io/gh/Euromance/pynote)

Note taking app.
Uses `NeoVim` and `bat` to edit and show notes respectively by default.
Markdown is also enforced with default settings.

## Installation

```
pip install pynote
```

## Configuration

Configuration is optional. The app will work with no config file at all
or with some lines purged. It's okay as long as it's a valid TOML file.

```
cp ./pynote.cfg.example ~/.pynote.cfg
$EDITOR ~/.pynote.cfg
```

## Usage

Notes will be saved to the directory you specified in config.
`~/.notes` by default. Available commands:

```
note --install-completion
     # Install autocompletion for your shell.
     # Provides you completion for commands,
     # arguments and note titles.

note edit sample-note
     # Create or edit a note with provided TITLE.
     # Launches `NeoVim` or the one you set in the config file.

note list
     # Lists available notes.

note view sample-note
     # View a note with provided TITLE.
     # Launches `bat` or the one you set in the config file.

note delete sample-note
     # Deletes a note with provided TITLE.
     # Asks for confirmation as long as you don't pass `--force`!
```

## Development

Open Makefile to see all targets.

```
make deps
make lint
make testreport
```
