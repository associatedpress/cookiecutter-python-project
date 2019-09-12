## AP Python Cookiecutter
---
**Project Structure**
```
├── analysis
│   └── archive
├── data
│   ├── html_reports
│   ├── manual
│   ├── processed
│   └── source
├── etl
├── publish
└── scratch
```
---

**Structure description**
- `analysis`
  - This is where we keep all of our jupyter ipython notebooks that contain analysis for the project.
    - Notebooks in this folder can ingest data from either `data/source` (if that data comes from the source in a workable format) or `data/processed` (if the data required some prep).
    - Dataframes from analysis notebooks should be written out to `data/processed`
  - `analysis/archive`: Notebooks that leave the scope of the project but should also remain in the project history will be placed here.

- `etl`
  - This is where we keep python scripts involved with collecting data and prepping it for analysis.
  - These files should be scripts, they should not be jupyter notebooks.

- `data`
  - This is the directory used with our `datakit-data` plugin.
  - `data/source`: contains raw, untouched data.
  - `data/processed`
    - Contains data that has either been transformed from an `etl` script or output from an `analysis` jupyter notebook.
    - Data that has been transformed from an `etl` script will follow a naming convention: `etl_{file_name}.[csv,json...]`
  - `data/manual`
    - Contains data that has been manually altered (e.g. excel workbooks with inconsistent string errors requiring eyes on every row).
  - `data/html_reports`
    - Contains rendered html of our analysis notebooks, the results of calling `jupyter nbconvert` on a notebook.

- `publish`
  - This directory holds all the documents in the project that will be public facing (e.g. data.world documents).

- `scratch`
  - This directory contains output that will not be used in the project in its final form.
  - Common cases are filtered tables or quick visualizations for reporters
  - This directory is not git tracked.
---

**Our `.gitignore`**

```
*.vim
.DS_Store

.ipynb_checkpoints

data/
!data/source/.gitkeep
!data/manual/.gitkeep
!data/processed/.gitkeep
!data/html_reports/.gitkeep

scratch/
!scratch/.gitkeep
```
