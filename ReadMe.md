# Welcome to MILETA!
MILETA is a Machine Learning Workspace Setup, which comes with 
* Tensorflow
* Lux
* MLFlow
* Minio 


# Get Started! 

You will need Docker and Docker Compose and you will find all the information you need here: https://docs.docker.com/desktop/windows/install/

# Running the Development Environment.

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

## MlFlow
    URL: ´http://127.0.0.1:5000`

## Minio
    URL: ´http://127.0.0.1:9000`

