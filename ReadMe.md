# Welcome to MILETA!
MILETA is a Machine Learning Workspace Setup, which comes with 
* Tensorflow
* Lux
* MLFlow
* Minio 


# Get Started! 

You will need Docker and Docker Compose and you will find all the information you need here: https://docs.docker.com/desktop/windows/install/

# Running the Development Environment Server.

1. Before you start you need to clone this repository with 
    `git clone https://github.com/denisekhuu/ml_workspace.git`

2. Change to the ml_workspace in the terminal with 

    `cd ml_workspace`

3. Create a '.env' file with the right configuration: 

    ```
    AWS_ACCESS_KEY_ID= $MINIO ID$ 

    AWS_SECRET_ACCESS_KEY= $MINIO KEY$ 

    MYSQL_DATABASE= $MYSQL DATABASE NAME$ 

    MYSQL_USER= $MYSQL USER$ 

    MYSQL_PASSWORD= $MYSQL PASSWORD$ 

    MYSQL_ROOT_PASSWORD= $MYSQL ROOT PASSWORD$
    ```

4. Run `docker-compose up` and you will find the following servers

## Jupyter Notebook
    URL: `http://127.0.0.1:8888/?token=...` (token specified in the terminal)

* add files to the "src" folder to see them in the UI
## MlFlow
    URL: ´http://127.0.0.1:5000`

## Minio
    URL: ´http://127.0.0.1:9000`

You can create your python files in the Jupyter Notebook UI. 
If the conda environment with jupyter notebook isn't what you want, you can also create a local python virtual environment. 
# Create A Python Virtual Environment

1. Change to the ml_workspace in the terminal with 

    `cd ml_workspace`

2. Create a python virtual environment with
        https://docs.python.org/3/library/venv.html 

    On Windows run 

    `pip -m venv env`

    Activate it in the terminal with

    `./env/Scripts/activate`

3. Install Python Libraries 

    This predefined environment comes with:
    ```
        minio==7.1.3
        mlflow==1.23.1
        scikit-learn==1.0.2
        joblib==1.1.0
        tensorflow==2.8.0
        tensorflow-addons==0.15.0
    ```

    Install them with
    `pip install -r requirements.txt`

Now you have a virtual environment and a dockerized environment for your ML development. 

Wait-for-it.sh by vishnubob
https://github.com/vishnubob/wait-for-it
