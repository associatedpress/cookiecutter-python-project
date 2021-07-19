import os

with open ('.env', 'w') as env_fi:
    env_fi.write(f"PYTHONSTARTUP={os.getcwd()}/.startup.py\n") 

os.system('pipenv install --dev')
# Install the ipython kernel with the project name
os.system('python -m ipykernel install --user --name={{ cookiecutter.project_slug }}')
os.system('jupyter lab build')
# Generate ipynb for every markdown file in analysis
os.system('jupytext --set-formats md,ipynb analysis/*.md')