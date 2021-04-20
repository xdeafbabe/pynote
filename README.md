# Pynote

[![codecov](https://codecov.io/gh/Euromance/pynote/branch/master/graph/badge.svg?token=aRfAPtBzsP)](https://codecov.io/gh/Euromance/pynote)

Note taking app.
Requires `bat` as it's my file viewer of choice.
Might later make viewing configurable with custom commands and args and stuff.
Utilizes `NeoVim` by default to edit notes, although might be configured.

Didn't see any point in not using `NeoVim` or `bat` since they are awesome
and have syntax highlighting and line numbers and less/cat behaviour and stuff.
Much better than `print(file.read())` and `input()`, that's for sure!

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
Or `~/.notes` if you did not. Available commands:

```
note edit sample-note
     # Create or edit a note with provided TITLE.
     # Launches `NeoVim` and sets syntax to Markdown.

note list
     # Lists available notes.

note view sample-note
     # View a note with provided TITLE.
     # Launches `bat` and sets syntax to Markdown.

note delete sample-note
     # Deletes a note with provided TITLE.
     # Asks for confirmation as long as you don't pass `--force`!
```

## Development

```
make deps
make lint
make testreport
```

## TODO

- [ ] Config
  - [x] Note directory
  - [ ] Editor args
  - [ ] Viewer args
  - [x] TOML config

- [ ] Meta
  - [ ] Categories
  - [ ] Creation date
  - [ ] SQLite or JSON????

- [x] A sane Makefile _(without poetry bullshit)_
- [x] Tests
- [x] A sane README _(what's wrong with current iteration? mark as done.)_
- [x] CI/CD
- [x] Upload to PyPI

- [ ] Super Fancy Stuff Probably Never To Be Implemented
  - [ ] Version control with Git or whatever or just plain diff patch
    - [ ] SQLite database to keep meta
    - [ ] Probably an actual Git repo lol what???
  - [ ] Synchronization
