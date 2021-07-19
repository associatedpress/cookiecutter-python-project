#!/bin/bash
## This post project generation script only runs if pipenv is on the machine
command -v pipenv >/dev/null 2>&1 || { echo >&2 "pipenv not found.  Aborting startup script."; exit 1; }
## Main installs typical to a project
pipenv install ipykernel pandas matplotlib notebook jupyterlab jupytext
## Add the first install script to the Pipfile
echo -e "\n[scripts]\nfirst_install = \"python .first_install.py\"" >> Pipfile
## Add script to render reports using AP nbconvert template
echo -e "\nexport_html_notebook = \"jupyter-nbconvert --to html --template ap_report --execute --output-dir ./data/html_reports/ --TemplateExporter.extra_template_basedirs=./.nbconvert_templates\"" >> Pipfile
## Run first_install script
## This is meant to be run when people first clone the project.
## We run it here to get the benefit of installing the ipython kernel.
pipenv run first_install
