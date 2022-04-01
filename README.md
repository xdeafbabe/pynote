# Pynote

[![codecov](https://codecov.io/gh/Euromance/pynote/branch/master/graph/badge.svg?token=aRfAPtBzsP)](https://codecov.io/gh/Euromance/pynote)

Note taking app.
Uses `NeoVim` and `bat` to edit and show notes respectively by default.
Markdown is also enforced with default settings.

## Notice

Playing around with `zsh` I found out that this app is so stupidly
overkill. I have rewritten it in 21 lines of `zsh` script. Enjoy!

```sh
mkdir -p $HOME/.notes

function mknote { nvim +'set ft=markdown' $HOME/.notes/$1 }
function rmnote { rm $HOME/.notes/$1 }
function vinote { bat $HOME/.notes/$1 -l md --file-name $1 }
function lsnote { ls $HOME/.notes }

function _notecomp {
	local dirs;
	dirs=();

	ls --color=never --width=1 $HOME/.notes | sort | while read line; do
		dirs[$(($#dirs+1))]="$line"
	done

	_describe -t notes "note" dirs
}

compdef _notecomp mknote
compdef _notecomp rmnote
compdef _notecomp vinote
```

Although it doesn't have any unit tests or configuration support,
it does exactly the same as default configuration of `pynote` would do.
It even has autocompletion!

_Sweet Jesus, sometimes I wish I knew bash._

But this repo still might be an example on how to integrate tests and linting,
how to build a package and upload it to PyPi. Keep in mind that `setup.py` approach is
kind of outdated now in favor of `pyproject.toml`. I haven't learnt it yet though.

And on `Makefile`... I like it. It's damn awesome. It's much more powerful than
`"scripts"` section in `package.json` and there's no alternative I'm aware of in Python.

## Installation

```sh
pip install pynote
```

## Configuration

Configuration is optional. The app will work with no config file at all
or with some lines purged. It's okay as long as it's a valid TOML file.

```sh
cp ./pynote.cfg.example ~/.pynote.cfg
$EDITOR ~/.pynote.cfg
```

## Usage

Notes will be saved to the directory you specified in config.
`~/.notes` by default. Available commands:

```sh
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

```sh
make deps
make lint
make testreport
```
