#!/bin/bash
## This post project generation script only runs if pipenv is on the machine
command -v pipenv >/dev/null 2>&1 || { echo >&2 "pipenv not found.  Aborting startup script."; exit 1; }

## Main installs typical to a project
pipenv install --python $(pyenv version-name) ipython ipykernel pandas matplotlib notebook jupyterlab altair jupytext jupyterlab_templates

## Add the first install script to the Pipfile and rmarkdown export script
echo -e "\n[scripts]\nfirst_install = \"python .first_install.py\"\nexport_rmarkdown = \"Rscript .export_rmarkdown.R\"" >> Pipfile

## Run first_install script
#### This is meant to be run when people first clone the project.
#### Running it here to add jupyter data directory env variable, to set the RETICULATE_PYTHON r env
###### variable, to set up the jupyter lab template directory/enable its server,
###### and to set up the git solution for changing cwd in an analysis file.
pipenv run first_install
