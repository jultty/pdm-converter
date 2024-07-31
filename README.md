# pdm-converter

A decimal-to-binary visual converter.

This application was developed as the capstone project for the Programming for Mobile Devices course in the São Paulo Federal Institute's Jacareí campus' Systems Analysis and Development undergraduate program.

## Running

This project was developed using [Poetry](https://python-poetry.org/) and [pyenv](https://github.com/pyenv/pyenv).

Provided you have both set up, you can run it with the following steps:

```sh
# clone this repository
git clone https://github.com/jultty/pdm-converter
cd pdm-converter

# install python 3.11 (if you don't have it)
pyenv install 3.11.6

# create a virtual environment
poetry env use python 3.11

# install dependencies
poetry install

# run
poetry run flet run main.py
```

If you'd rather run the flet CLI tool directly, you can source the environment:

```sh
source "$(poetry env info -p)"/bin/activate
```

The steps above and the application were tested only on Void Linux. The development environment runs zsh 5.9, Python 3.11.6, Poetry 1.8.3 and pyenv 2.4.1.
