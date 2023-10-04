# mlopsproject


## workflows

1.Update config.yaml
2.Update schema.yaml
3.Update params.yaml
4.Update the entity
5.Update the configuration manage in src config
6.Update the components
7.Update the pipeline
8.Update the main.py
9.Update the app.py



# How to run
### STEPS

Clone the repository
...bash
https://github.com/RatulAch/mlopsproject
..

### Step 1 - Create a conda environment afoer the repo

...bash
conda create -n mlops python=3.8
...

...bash
conda activate mlops
...

### Step 2 - install the requirements

...bash
# run app.py
...

now,
...bash
open up the local host and port
..


## MLflow

[Documentation link] https://mlflow.org/docs/latest/index.html

### cmd
-mlflow ui

###dagshub
[dugshub](https://dagshub.com)

MLFLOW_TRACKING_URI=https://dagshub.com/RatulAch/mlopsproject.mlflow \

MLFLOW_TRACKING_USERNAME=RatulAch \

MLFLOW_TRACKING_PASSWORD=aa2448f4281143bffb22078b7c6cccd706272881 \
python script.py



mlflow.set_tracking_uri('https://dagshub.com/RatulAch/mlopsproject.mlflow')



Run this to export as env variables

...bash
export MLFLOW_TRACKING_URI=https://dagshub.com/RatulAch/mlopsproject.mlflow \

export set MLFLOW_TRACKING_USERNAME=RatulAch \

export set MLFLOW_TRACKING_PASSWORD=aa2448f4281143bffb22078b7c6cccd706272881 \

...

