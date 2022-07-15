import os
import glob
from subprocess import check_output
from subprocess import run

VENV_DIR = "".join(check_output(['pipenv', '--venv']).decode('utf-8').split())
RETICULATE_PYTHON = check_output(['pipenv', 'run', 'which', 'python']).decode('utf-8')
TEMPLATE_PATHS = glob.glob('analysis/notebook_templates/*')
# Install the necessary packages
run(['pipenv', 'install', '--dev'])

# Need to set the Jupyter data directory, this is where jupyter looks for kernels
with open ('.env', 'w') as env_fi:
    env_fi.write(f"JUPYTER_DATA_DIR={VENV_DIR}/share/jupyter/\n")
# Need to tell R which python executable to use. Necessary for exporting rmarkdown reports as html.
with open ('.Renviron', 'w') as Renv_fi:
    Renv_fi.write(f"RETICULATE_PYTHON={RETICULATE_PYTHON}")

# Need to build jupyter lab after installing jupyter plugins (like jupytext)
run(['jupyter', 'lab', 'build'])
# Generate ipynb for every markdown file in analysis
run(['jupytext', '--set-formats', 'Rmd,ipynb', 'analysis/*.md'])
# Install jupyter template extension and enable the template server
run(['jupyter', 'labextension', 'install', 'jupyterlab_templates'])
run(['jupyter', 'serverextension', 'enable', '--py', 'jupyterlab_templates'])
run(['mkdir', f"{VENV_DIR}/share/jupyter/notebook_templates"])
for path in TEMPLATE_PATHS:
    run(['cp', '-r', path, f"{VENV_DIR}/share/jupyter/notebook_templates/"])
# Git solution for changing cwd in analysis files to root of project
run(['pipenv', 'run', 'bash', '.set_kernel_path.sh'])
