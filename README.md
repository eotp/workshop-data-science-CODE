# Materials for a Workshop on Data Science @ [CODE University Berlin](https://code.berlin/de/), March 12 and 19<sup>th</sup>, 2018




[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/eotp/workshop-data-science-CODE/master)

This repository contains materials for a workshop on __Exploratory Data Analysis and Predictive Modeling__ hosted at CODE University, Berlin, Germany.

In order to re-run the workshop materials we encourage you to use the [conda](https://conda.io/docs/) package manager. Once installed, create an environment and install all required dependencies on your machine by typing 

`conda env create -f environment.yml`

into your console. You activate your new environment by typing 

`source activate data-science` (on LINUX and Mac) or

`activate data-science` (on WINDOWS). 

Then you are ready to go (if you are stuck check out the [conda documentation site](https://conda.io/docs/user-guide/tasks/manage-environments.html#)). Alternatively, you may launch [binder](https://binderhub.readthedocs.io/en/latest/) to get a reproducible executable environment immediately in your browser. Simply click the _launch binder_ icon in the upper left corner, or go [here](https://mybinder.org/v2/gh/eotp/workshop-data-science-CODE/master).


***

The workshop focuses on data science with Python. We will introduce libraries/modules such as `numpy`, `scipy`, `statsmodels`, `pandas`, `scikit-learn`, `matplotlib`, and `seaborn`, among others.



All data sets, all code snippets, all [Jupyter](http://jupyter.org/) notebooks and the `environment.yml` file for reproducibility are available through this self contained repository.

The structure of this repository is outlined below:

    4learners
    │.git                  # git internals
    │.gitignore            # specify files/folders to be ignored by git
    └───data
    │   │...               # find all the raw data files
    └───figures
    │   │...               # saved figures go here
    └───notebooks
    │   └───_img
    │   │   │...           # rendered images are placed here
    │   │...               # find all Jupyter notebooks here
    │
    │README.md
    │environment.yml       # conda environment specifications for reproducibility
    └───src
        │...               # here go the code snippets and scripts
        └───_solutions
            │...           # solutions for coding challenges (don't cheat yourself ;-))


 ***
 
 




