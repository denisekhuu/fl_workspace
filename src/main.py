# Setup MLflow
import mlflow
from random import random, randint
mlflow.start_run()

# Log params
mlflow.log_param("param1", randint(0, 100))

mlflow.log_metric("foo", random())
mlflow.log_metric("foo", random() + 1)
mlflow.log_metric("foo", random() + 2)


# End run
mlflow.end_run()