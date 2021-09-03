#!/bin/bash
## This post project generation script only runs if pipenv is on the machine
command -v pipenv >/dev/null 2>&1 || { echo >&2 "pipenv not found.  Aborting startup script."; exit 1; }
## Main installs typical to a project
pipenv install ipython ipykernel pandas matplotlib notebook jupyterlab jupytext
## Add the first install script to the Pipfile
echo -e "\n[scripts]\nfirst_install = \"python .first_install.py\"" >> Pipfile
## Add script to render reports using AP nbconvert template
echo -e "\nexport_html_notebook = \"jupyter-nbconvert --to html --template ap_report --execute --output-dir ./data/html_reports/ --TemplateExporter.extra_template_basedirs=./.nbconvert_templates\"" >> Pipfile
## Run first_install script
## This is meant to be run when people first clone the project.
## We run it here to get the benefit of installing the ipython kernel.
pipenv run first_install

## Set kernels to run from where git was initialized (the project root)
## If git wasn't initialized, notebooks run from where the notebook file is (the default)

JUPYTER_DATA_DIR=$(jupyter --data-dir)
KERNEL_PATH=$JUPYTER_DATA_DIR/kernels/{{cookiecutter.project_slug}}
VENV_DIR=$(pipenv --venv)

## Replace the default kernel.json with one that points to kernel.sh
echo -e '{\n "argv": [' > $KERNEL_PATH/kernel.json
echo "  \"$KERNEL_PATH/kernel.sh\"," >> $KERNEL_PATH/kernel.json
echo -e '  "{connection_file}"\n ],\n "display_name": "{{cookiecutter.project_slug}}",\n "language":"python",\n "metadata":{\n "debugger":true\n }\n}' >> $KERNEL_PATH/kernel.json

## kernel.sh first changes directory to git root before invoking the default command to launch a kernel
echo -e '#!/bin/bash\ncd "$(git rev-parse --show-toplevel)"' > $KERNEL_PATH/kernel.sh
echo "exec $VENV_DIR/bin/python -m ipykernel_launcher -f \"\$1\"" >> $KERNEL_PATH/kernel.sh

## Execute permissions
chmod 777 $KERNEL_PATH/kernel.sh
