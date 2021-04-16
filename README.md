# Pynote

Note taking app. Build it with poetry and install locally.
Requires `NeoVim` and `bat` as those are my file editor and viewer of choice.
Might later make editing and viewing configurable with custom commands and args and stuff.

## Usage

Notes will be saved to `~/.notes` directory. Available commands:

```shell
note edit    # Create or edit an existing note.
             # Launches `NeoVim` and sets syntax to Markdown.

note list    # Lists available notes.

note view    # View an existing note.
             # Launches `bat` and sets syntax to Markdown.

note delete  # Deletes an existing note.
```

## TODO

- [ ] Config
  - [ ] Note directory
  - [ ] Editor args
  - [ ] Viewer args
  - [ ] TOML config

- [ ] Meta
  - [ ] Categories
  - [ ] Creation date
  - [ ] SQLite or JSON????

- [ ] A sane Makefile
- [ ] Tests
- [ ] A sane README
- [ ] CI/CD
- [ ] Upload to PyPI

- [ ] Super Fancy Stuff Probably Never To Be Implemented
  - [ ] Version control with Git or whatever or just plain diff patch
    - [ ] SQLite database to keep meta
    - [ ] Probably an actual Git repo lol what???
  - [ ] Synchronization
