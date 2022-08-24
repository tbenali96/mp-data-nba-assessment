mp-data-nba-assessment
==============================

Predict the career length of NBA players

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   └── models         <- Scripts to train models and then use trained models to make
    │       │                 predictions
    │       ├── predict_model.py
    │       └── train_model.py
    │
    │
    ├── visualizations     <- Vizualisations.
    │
    ├── test               <- Unit tests for the source code. 
    │
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

The following are some command lines to help use the source code of this project : 

Once you cloned the repository, you first need to create a virtual environment and make sure to download the right libraries. To do so, use :
```
make requirements
```
To launch the api, you use : 
```
make app
```
Once you launched the api, to test it, you need to go to [API](http://127.0.0.1:8000/docs). You can use the data/test/sample.csv as test file.
For our project, the data is stored in the repository. To build the features, you use :
```
make data
```
To train the model, you use :
```
make train
```
For the inference part, we are here working with a sample dataset. The following command will help make the inference on this particular dataset. 
But, in a production environment, we will have to make the dataset an argument for our inference function. 
```
make predict
```
To test and evaluate the coverage of our code, you can use :
```
make test
```
This command will start tests about each part of the source code and generates coverage reports. 
Ultimately, the objective of the tests is to create a CI/CD pipeline to validate the correctness of our source code. It is important to note that the tests 
that we created are only related to the code itself, not the Machine Learning artifacts. 
We can, for example, add other tests that evaluate the validity of the model before putting it into the production environment. 