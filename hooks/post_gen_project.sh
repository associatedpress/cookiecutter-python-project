#!/bin/bash
## This post project generation script only runs if pipenv is on the machine
command -v pipenv >/dev/null 2>&1 || { echo >&2 "pipenv not found.  Aborting startup script."; exit 1; }

## Run first_install script
#### This is meant to be run when people first clone the project.
#### Running it here to add jupyter data directory env variable, to set the RETICULATE_PYTHON r env
###### variable, to set up the jupyter lab template directory/enable its server,
###### and to set up the git solution for changing cwd in an analysis file.

python ./.first_install.py "{{cookiecutter.additional_packages_to_install}}"
