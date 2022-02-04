# Setup MLflow
import mlflow
from random import random, randint
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from joblib import dump
from minio import Minio
from minio.error import S3Error
import os


iris = load_iris()
type(iris)

x=iris.data
y=iris.target


# split the data into train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5)


# define a classifier
classifier=tree.DecisionTreeClassifier()
# fit the classifier
classifier.fit(x_train,y_train)
predictions=classifier.predict(x_test)


# estimate the accuracy of the model
print(accuracy_score(y_test,predictions))


filename = 'decisionTree.sav'
dump(classifier, filename)

# create a connection to server
minioClient = Minio('localhost:9000',
                     access_key='minio',
                     secret_key='minio123',
                     secure=False)

# open the file and put the object in bucket called example
with open('decisionTree.sav', 'rb') as file_data:
    file_stat = os.stat('decisionTree.sav')
    minioClient.put_object('mlflow', 'decisionTree.sav', file_data,
                    file_stat.st_size)

# List all object paths in bucket that begin with my-prefixname.
objects = minioClient.list_objects('mlflow', recursive=True)

for obj in objects:
    print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
          obj.etag, obj.size, obj.content_type)

# get the object from MinIO and safe it as newfile
print(minioClient.fget_object('mlflow', 'decisionTree.sav', "newfile"))

# use the downloaded object to do the predictions and print result
filename = 'newfile'
loaded_model = joblib.load(filename)
result = loaded_model.score(x_test, y_test)
print(result)

# mlflow.start_run()

# # Log params
# mlflow.log_param("param1", randint(0, 100))

# mlflow.log_metric("foo", random())
# mlflow.log_metric("foo", random() + 1)
# mlflow.log_metric("foo", random() + 2)


# # End run
# mlflow.end_run()