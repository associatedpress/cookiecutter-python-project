import os
from subprocess import check_output

with open ('.env', 'w') as env_fi:
    env_fi.write(f"PYTHONSTARTUP={os.getcwd()}/.startup.py\n") 
# Need to tell R which python executable to use
with open ('.Renviron', 'w') as Renv_fi:
    Renv_fi.write(f"RETICULATE_PYTHON={check_output(['pipenv', 'run', 'which', 'python']).decode('utf-8')}")

os.system('pipenv install --dev')
# Install the ipython kernel with the project name
os.system('python -m ipykernel install --user --name={{ cookiecutter.project_slug }}')
os.system('jupyter lab build')
# Generate ipynb for every markdown file in analysis
os.system('jupytext --set-formats md,ipynb analysis/*.md')
# Enable template server
os.system('jupyter labextension install jupyterlab_templates')
os.system('jupyter serverextension enable --py jupyterlab_templates')