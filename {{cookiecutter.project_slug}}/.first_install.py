import os.path
import glob
from subprocess import check_output
from subprocess import run

run(['mkdir', './.venv'])

PYENV_VERSION = "".join(check_output(['pyenv', 'version-name']).decode('utf-8').split())
PYENV_PREFIX = "".join(check_output(['pyenv', 'prefix', f"{PYENV_VERSION}"]).decode('utf-8').split())

if os.path.isfile('./Pipfile'):
    run(['pipenv', 'install', '--dev'])
else:
    run(['pipenv', 'install', '--python', f"{PYENV_PREFIX}/bin/python", 'ipython', 'ipykernel', 'pandas', 'matplotlib', 'notebook', 'jupyterlab', 'altair', 'jupytext', 'jupyterlab_templates', 'itables', 'ap-altair-theme'])
    ## Add this script to the Pipfile, along with the rmarkdown export script
    with open('Pipfile', 'a') as pipfile:
        pipfile.write('\n[scripts]\nexport_rmarkdown = "Rscript .export_rmarkdown.R"')

VENV_DIR = "".join(check_output(['pipenv', '--venv']).decode('utf-8').split())
RETICULATE_PYTHON = check_output(['pipenv', 'run', 'which', 'python']).decode('utf-8')
TEMPLATE_PATHS = glob.glob('analysis/notebook_templates/*')

# Need to set the Jupyter data directory, this is where jupyter looks for kernels
with open ('.env', 'w') as env_fi:
    env_fi.write(f"JUPYTER_DATA_DIR={VENV_DIR}/share/jupyter/\n")
# Need to tell R which python executable to use. Necessary for exporting rmarkdown reports as html.
with open ('.Renviron', 'w') as Renv_fi:
    Renv_fi.write(f"RETICULATE_PYTHON={RETICULATE_PYTHON}")

# Generate ipynb for every markdown file in analysis
run(['pipenv', 'run', 'jupytext', '--set-formats', 'Rmd,ipynb', 'analysis/*.Rmd'])
# Install jupyter template extension and enable the template server
run(['pipenv', 'run', 'jupyter', 'labextension', 'install', 'jupyterlab_templates'])
run(['pipenv', 'run', 'jupyter', 'serverextension', 'enable', '--py', 'jupyterlab_templates'])
run(['mkdir', f"{VENV_DIR}/share/jupyter/notebook_templates"])
for path in TEMPLATE_PATHS:
    run(['cp', '-r', path, f"{VENV_DIR}/share/jupyter/notebook_templates/"])
# Git solution for changing cwd in analysis files to root of project
run(['pipenv', 'run', 'bash', '.set_kernel_path.sh'])
