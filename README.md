# Kidney Disease Classification with Deep Learning and AWS Deployment

This repository contains the code for kidney disease classification using deep learning, with tracking via MLflow and data version control using DVC. The project is prepared for deployment on AWS.

## Setup Instructions

### 1. Create and Activate Virtual Environment

## Create Templates

```
python3 create-templates.py
```

## Install
```
python3 setup.py install
```

## Install Requirements

```
pip install -r requirements.txt
```

## Set Enviroment
```
export MLFLOW_TRACKING_URI="https://dagshub.com/rohitcode005/Kidney-Disease-clf-deep-learning-AWS-deploy.mlflow"
export MLFLOW_TRACKING_USERNAME="rohitcode005"
export MLFLOW_TRACKING_PASSWORD=''
```

### DVC 
```
dvc init
dvc repro
dev dag
```
### Run the Code without DVC
### If you want to run the code without using DVC, use:

```
python main.py
```
