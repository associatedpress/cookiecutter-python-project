#!/bin/bash
command -v pipenv >/dev/null 2>&1 || { echo >&2 "pipenv not found.  Aborting startup script."; exit 1; }
echo "PYTHONSTARTUP=$PWD/.startup.py" >> .env
pipenv install
pipenv install ipykernel
pipenv install pandas
pipenv install matplotlib
pipenv run python -m ipykernel install --user --name={{ cookiecutter.project_slug }}
