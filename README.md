# Pynote

[![codecov](https://codecov.io/gh/Euromance/pynote/branch/master/graph/badge.svg?token=aRfAPtBzsP)](https://codecov.io/gh/Euromance/pynote)

Note taking app.
Uses `NeoVim` and `bat` to edit and show notes respectively by default.
Markdown is also enforced with default settings.

Didn't see any point in not using `NeoVim` or `bat` since they are awesome
and have syntax highlighting and line numbers and less/cat behaviour and stuff.
Better than `print(file.read())` and `input()`, that's for sure!

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

```
make deps
make lint
make testreport
```

## TODO

- [x] Config
  - [x] Note directory
  - [x] Editor args
  - [x] Viewer args
  - [x] TOML config

- [x] A sane Makefile _(without poetry bullshit)_
- [x] Tests
- [x] A sane README _(what's wrong with current iteration? mark as done.)_
- [x] CI/CD
- [x] Upload to PyPI

- [ ] Super Fancy Stuff _Probably_ **Never** To Be Implemented
  - [ ] Version control with Git or whatever or just plain diff patch
    - [ ] SQLite database to keep meta
    - [ ] Probably an actual Git repo lol what???
  - [ ] Meta _(not really fancy just what for???)_
    - [ ] Categories
    - [ ] Creation date
    - [ ] SQLite or JSON????
  - [ ] Synchronization

## Questions nobody asked

**Why there won't be version control?**  
Cause it's a note taking app. Write note, view one or delete it. KISS.

**Why there won't be meta?**  
Cause why? `$ stat ~/.notes/my-note` to see access and modify and change and birth dates. Although categories might seem helpful at a glance, they're not _that_ helpful!. Even if you have like 200 notes. Just name your notes something like `category-note` and autocompletion will help you.

**Why there won't be synchronization?**  
Why turn it into yet another SaaS? Initialize a private GitHub repo and here you go: version control, synchronization across devices, and all other fancy stuff. Just automate it with a couple of shell scripts, edit the source code to add some on command hooks to sync and you're good to go.
