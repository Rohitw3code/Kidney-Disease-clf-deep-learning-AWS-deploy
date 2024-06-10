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
```
python3 setup.py install

Install Requirements

```
pip install -r requirements.txt

Set Enviroment
```
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
```
python main.py


Sure! Here is the raw markdown code for your README.md file:

markdown
Copy code
# Kidney Disease Classification with Deep Learning and AWS Deployment

This repository contains the code for kidney disease classification using deep learning, with tracking via MLflow and data version control using DVC. The project is prepared for deployment on AWS.

## Setup Instructions

### 1. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
2. Create Templates
bash
Copy code
python3 create-templates.py
3. Install Local Package
bash
Copy code
python3 setup.py install
This command will create an egg file which allows the package to be accessed from anywhere locally.

4. Install Requirements
bash
Copy code
pip install -r requirements.txt
5. Set Environment Variables
Run the following commands in the terminal to set up MLflow tracking:

bash
Copy code
export MLFLOW_TRACKING_URI="https://dagshub.com/rohitcode005/Kidney-Disease-clf-deep-learning-AWS-deploy.mlflow"
export MLFLOW_TRACKING_USERNAME="rohitcode005"
export MLFLOW_TRACKING_PASSWORD='b53fb19cf0cae0da766408cf05c522d04c7f8d66'
6. Initialize DVC
Initialize DVC in the project directory:

bash
Copy code
dvc init
7. Run the Code with DVC
To run the code using DVC, execute:

bash
Copy code
dvc repro
You can visualize the pipeline with:

bash
Copy code
dvc dag
8. Run the Code without DVC
If you want to run the code without using DVC, use:

```bash
python main.py

Before Deployment: Comment out the MLflow code as it is only used during development and not in production.
Additional Information
MLflow Tracking: This project uses MLflow for experiment tracking. Ensure the environment variables for MLflow are correctly set before running the experiments.
DVC: Data Version Control (DVC) is used to manage datasets and machine learning models. Make sure to have DVC installed and initialized in the project directory.

run flask application
```bash
python app.py