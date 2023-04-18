# AP Python Cookiecutter

This is a project template powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter) for use with [datakit-project](https://github.com/associatedpress/datakit-project/).

**Structure**

```
.
├── README.md
├── analysis
│   └── archive
├── data
│   ├── documentation
│   ├── html_reports
│   ├── manual
│   ├── processed
│   ├── public
│   └── source
├── etl
├── publish
└── scratch
```

- `README.md`
  - Project-specific readme with boilerplate for data projects.
- `analysis`
  - This is where we keep all of our jupyter ipython notebooks that contain analysis for the project.
    - Notebooks in this folder can ingest data from either `data/source` (if that data comes from the source in a workable format) or `data/processed` (if the data required some prep).
    - Dataframes from analysis notebooks should be written out to `data/processed`
  - `analysis/archive`: Notebooks that leave the scope of the project but should also remain in the project history will be placed here.
  - Note that only `.Rmd` linked to `.ipynb` via `Jupytext` are commited, `.ipynb` are in the `.gitignore` because `.ipynb` metadata frequently disrupts version control whenever a notebook is opened or interacted with, while `.Rmd` files only keep track of code.
- `data`
  - This is the directory used with our `datakit-data` plugin.
  - `data/documentation`
    - Documentation on data files should go here - data dictionaries, manuals, interview notes.
  - `data/html_reports`
    - Contains rendered html of our analysis notebooks, the results of calling `pipenv run export_rmarkdown` on a notebook.
  - `data/manual`
    - Contains data that has been manually altered (e.g. excel workbooks with inconsistent string errors requiring eyes on every row).
  - `data/processed`
    - Contains data that has either been transformed from an `etl` script or output from an `analysis` jupyter notebook.
    - Data that has been transformed from an `etl` script will follow a naming convention: `etl_{file_name}.[csv,json...]`
  - `data/public`
    - Public-facing data files go here - data files which are 'live'.
  - `data/source`: contains raw, untouched data.
- `etl`
  - This is where we keep python scripts involved with collecting data and prepping it for analysis.
  - These files should be scripts, they should not be jupyter notebooks.
- `publish`
  - This directory holds all the documents in the project that will be public facing (e.g. data.world documents).
- `scratch`
  - This directory contains output that will not be used in the project in its final form.
  - Common cases are filtered tables or quick visualizations for reporters
  - This directory is not git tracked.

**Our `.gitignore`**

```
*.vim
.env
.Renviron
.venv
.quarto
.DS_Store
.ipynb_checkpoints

analysis/*.ipynb
analysis/archive/*.ipynb
!analysis/notebook_templates/*.ipynb

data/
!data/source/.gitkeep
!data/manual/.gitkeep
!data/processed/.gitkeep
!data/html_reports/.gitkeep
!data/public/.gitkeep
!data/documentation/.gitkeep

scratch/
!scratch/.gitkeep
```

## Usage

These steps assume configuration for [datakit-project](https://github.com/associatedpress/datakit-project) are complete.

- If you'd like to keep a local version of this template on your computer, git clone this repository to where your cookiecutters live:

```
cd path/to/.cookiecutters
git clone git@github.com/associatedpress/cookiecutter-python-project.git
```

- Now, when starting a new project with `datakit-project`, reference the cookiecutter in your filesystem. This creates a `pipenv` virtual environment and a ipython kernel for jupyter notebooks that will have the name of the `project_slug`.

```
datakit project create --template path/to/.cookiecutters/cookiecutter-python-project`
```

If you'd like to avoid specifying the template each time, you can edit `~/.datakit/plugins/datakit-project/config.json` to use this template by default:

```
 {"default_template": "/path/to/.cookiecutters/cookiecutter-python-project"}
```

### Full virtual environment setup. From package management to rendering analyses.

This python template should get AP data journalists set up quickly with a virtual environment, allowing them to clone a project and quickly install all the packages required to run ETL and analysis files. 

**Setup**

*This is the required setup to get the full python package management functionality provided by this template:*

- [Pyenv](https://github.com/pyenv/pyenv) to manage our python installations. `brew install pyenv`

  - We need to install a python with shared libraries via `pyenv` using the option `--enable-shared`. This gives us the ability to interact with our R install, should we ever wish to write R code in an R cell in Jupyter, or use R from a python instance using the python library `rpy2`. If we were to install version 3.9.13, for example: `env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.9.13`.

- [Pipenv](https://pipenv.pypa.io/en/latest/) to manage the python packages necessary for our project. We switch to our python with shared libraries we installed earlier (in this case version 3.9.13) with `pyenv global 3.9.13` and then pip install pipenv `python -m pip install pipenv`. It is possible to brew install pipenv, but those who maintain pipenv do not maintain that brew install of the software. They suggest pip installing.

- [Quarto](https://quarto.org/) to render our analysis notebooks. To install, we use the [CLI installer](https://quarto.org/docs/get-started/) available on their site.

- Finally, we install `datakit` on the pyenv python with shared libraries. The config files we set up when we first installed datakit will work with datakit installs across different versions of python. `python -m pip install datakit-gitlab datakit-project datakit-data`.

**Workflow**

*Starting a new project*
- `datakit project create` will kick off the typical datakit cookiecutter project creation, but this template runs an additional script after constructing the AP analysis folder tree. Briefly, this script sets up the project for pipenv and installs our typical analysis packages. You can find this script in your project: `.first_install.py`. A more detailed description for this script will come with an update to the README.

- Once the project is created we `cd` into it and run `pipenv shell` Before running `jupyter lab`. Or, we run `pipenv run jupyter lab`. It's up to you which commands to use here. Some people like to have a subshell running via `pipenv shell`, knowing that any command they run in that open subshell will make use of the pipenv environment. Other people like to type in the command every time they want to use the virtual environment with `pipenv run [terminal command]`.

- Whenever we need to install a package, we use `pipenv install [some_package]`.

- We don't git track `.ipynb` notebooks. Instead, we use [Jupytext](https://jupytext.readthedocs.io/en/latest/) to link our `.ipynb` files to git-tracked `.Rmd` files. This makes `git diff`s much more useful. `git status` shouldn't say our analysis changed because we ran a cell again. This makes sure it doesn't.

- When we start an analysis notebook, we use the folder tree in Jupyter Lab to get to our analysis folder and open a new Launcher Window (`shift + command + L`). Under the "Notebook" section, we select the option called "Template". This brings up a dropdown selection menu. Select `ap_data_team` on the top dropdown, and `quarto.ipynb` on the bottom. This should bring up another option to select your ipython kernel. Select the kernel named after your project.
  - At this point, you have an analysis notebook file that is linked to an `.Rmd` with the same name. The first time you save your `.ipynb` file, you'll see that `.Rmd` appear alongside your `.ipynb` file. If you ever rename the `.ipynb`, the name of the `.Rmd` will change to match it.
  - You can still create a typical `.ipynb` analysis without the template (and without the paired `.Rmd`). Just keep in mind that without a paired `.Rmd` the analysis will not be git-tracked, unless you add an exception for the `.ipynb` file in the `.gitignore`.

- While we are coding our analysis, we have the ability through Quarto to preview the rendered html file. Run `quarto preview path/to/analysis.ipynb`.

- When we're ready to render and share our analysis, we make sure Quarto executes the cells in the notebook to render fresh output. Run `quarto render path/to/analysis.ipynb --to html --execute`.

*Cloning a project*

- When you're in the directory where you keep your analysis projects, clone the python project: `git clone git@some.git.domain:path/to/git_project.git`
- `cd` into the project and run `python .first_install.py`
  - This step will create the projects virtual environment, install all necessary packages included in the `Pipfile` using the major python version defined in the `Pipfile`, and use the `.Rmd` files in the project to generate `.ipynb` files to work with. 


**Legacy rmarkdown rendering**

Before we started using Quarto, this template generated R-style html reports via rmarkdown. We did this because rmarkdown generated better tables and more beautiful reports. To achieve it, we would actually pass the Jupytext-paired `.Rmd` file to rmarkdown via an Rscript. This required writing R cells in our analyses to get R style tables. For Altair charts, we'd have to pass the chart json to an R library that knew how to deal with vega charts. These cells wouldn't run until we rendered the report. This is the main reason for switching to Quarto, which allows us to have notebook output that matches what we'll see in the rendered report, and the result is just as beautiful. However, there may come a time, when we find rendering an `.Rmd` via rmarkdown useful. For that reason, we are keeping the rmarkdown rendering script. Keep in mind that to make use of it, you'll need to start an analysis with the Jupyter notebook template `rmarkdown.ipynb`. Then you can render an analysis using that template with `pipenv run export_rmarkdown path/to/analysis.Rmd`.

## Configuration

You can set the default name, email, etc. for a project in the `cookiecutter.json` file.
