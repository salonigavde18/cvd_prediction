# -*- coding: utf-8 -*-
"""CVD_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oUHF5APQ6aDb3J0YuIPvzv3ze07jIgse

Importing the dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data collection and processing"""

#loading the csv data to Pandas df
heart_data = pd.read_csv('/content/heart_disease_data.csv')

#print few rows of the dataset
heart_data.head()

#no of rows and columns in the dataset
heart_data.shape

#getting some info about the data
heart_data.info()

#checking for null values
heart_data.isnull().sum()

#stats of the data
heart_data.describe()

#checking distribution of target variables
heart_data['target'].value_counts()

"""1--> Heart issue/disease
0--> Healthy heart

Splitting the feature and target
"""

x = heart_data.drop(columns='target', axis=1)
y = heart_data['target']

print(x)

print(y)

"""Ssplitting the data into training data and test data"""

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, stratify=y, random_state=2)

print(x.shape, x_train.shape, x_test.shape)

"""Model training....

Logistic Regression
"""

model = LogisticRegression()

#training the LogisticRegression model with training data
model.fit(x_train, y_train)

"""Model evaluation

Accuracy score
"""

#accuracy on the training data
x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)

print('Accuracy on training data: ', training_data_accuracy)

#accuracy on the test data
x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)

print('Accuracy on test data:', test_data_accuracy)

"""Building a Predictive System"""

input_data = (67,1,0,160,286,0,0,108,1,1.5,1,3,2)

# change the input data to a numpy array
input_data_as_array = np.asarray(input_data)

# reshape the numpy array as we're predicting for only data sample only
input_data_reshaped = input_data_as_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if prediction[0] == 0:
  print("The person does not have any cardiovascular disease.")
else:
  print("The person has cardiovascular disease.")
