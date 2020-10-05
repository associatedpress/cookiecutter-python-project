#!/bin/bash
command -v pipenv >/dev/null 2>&1 || { echo >&2 "pipenv not found.  Aborting startup script."; exit 1; }
## ipykernel requires the latest prompt-toolkit library
pipenv install "prompt-toolkit>=2.0.4"
pipenv install "importlib-metadata<2,>=0.12"
pipenv install ipykernel
pipenv install pandas
pipenv install matplotlib
pipenv install notebook
pipenv install jupyterlab
pipenv install jupytext

## This script will be run when someone clones into the project, it takes care
## of what this hook puts in place two lines later.
echo -e "\n[scripts]\nfirst_install = \"python .first_install.py\"" >> Pipfile
## These are the "two lines later"
echo "PYTHONSTARTUP=$PWD/.startup.py" >> .env
pipenv run python -m ipykernel install --user --name={{ cookiecutter.project_slug }}
