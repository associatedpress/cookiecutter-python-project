import os
from subprocess import check_output
from subprocess import run

with open ('.env', 'w') as env_fi:
    env_fi.write(f"PYTHONSTARTUP={os.getcwd()}/.startup.py\n")
# Need to tell R which python executable to use
with open ('.Renviron', 'w') as Renv_fi:
    Renv_fi.write(f"RETICULATE_PYTHON={check_output(['pipenv', 'run', 'which', 'python']).decode('utf-8')}")

run(['pipenv', 'install', '--dev'])
# Install the ipython kernel with the project name
run(['python', '-m', 'ipykernel', 'install', '--user', '--name={{ cookiecutter.project_slug }}'])
run(['jupyter', 'lab', 'build'])
# Generate ipynb for every markdown file in analysis
run(['jupytext', '--set-formats', 'md,ipynb', 'analysis/*.md'])
# Enable template server
run(['jupyter', 'labextension', 'install', 'jupyterlab_templates'])
run(['jupyter', 'serverextension', 'enable', '--py', 'jupyterlab_templates'])
run(['bash', '.set_kernel_path.sh'])
