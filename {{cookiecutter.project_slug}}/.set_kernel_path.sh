#!/bin/bash

## Set kernels to run from where git was initialized (the project root)
## If git wasn't initialized, notebooks run from where the notebook file is (the default)

JUPYTER_DATA_DIR=$(jupyter --data-dir)
KERNEL_PATH=$JUPYTER_DATA_DIR/kernels/python3 ## python3 is hardcoded, is there a way to print the name out?
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
