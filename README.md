# Kidney Disease Classification with Deep Learning and AWS Deployment

This repository contains the code for kidney disease classification using deep learning, with tracking via MLflow and data version control using DVC. The project is prepared for deployment on AWS.

## Setup Instructions

### 1. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate

Create Templates

```bash
python3 create-templates.py

Install
```bash
python3 setup.py install

Install Requirements

```bash
pip install -r requirements.txt

Set Enviroment

```bash
export MLFLOW_TRACKING_URI="https://dagshub.com/rohitcode005/Kidney-Disease-clf-deep-learning-AWS-deploy.mlflow"
export MLFLOW_TRACKING_USERNAME="rohitcode005"
export MLFLOW_TRACKING_PASSWORD=''

DVC code

```bash
dvc init
dvc repro
dev dag

Run the Code without DVC
If you want to run the code without using DVC, use:

```bash
python main.py

