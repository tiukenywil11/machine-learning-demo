"""
Coding Exercise 1: Importing and Preprocessing a Dataset for Machine Learning
In this exercise, you will explore data preprocessing with Python.

Instructions:



Import the necessary Python libraries: You will need the pandas library for this exercise. Also import numpy and train_test_split from sklearn.model_selection.

Load the Iris dataset: The Iris dataset is stored in a CSV file named 'iris.csv'. Use the pandas function read_csv to load this file and store it in a DataFrame. Assign the DataFrame to a variable named dataset.

Identify the features and the dependent variable: The features (independent variables) in the Iris dataset are the lengths and widths of the petals and sepals, and the dependent variable is the species of the Iris. The features are stored in all columns except the last one in your DataFrame, and the dependent variable is stored in the last column.

Create the matrix of features (X) and the dependent variable vector (y): Use the iloc indexer in pandas to select these subsets of the data and store them in variables X and y respectively. You should use the .values attribute to extract the data as numpy arrays.

Print X and y: Finally, print the matrix of features (X) and the dependent variable vector (y) to verify their creation. You can use the print function for this.

"""

# Importing the necessary libraries
import numpy as np
import pandas as pd
import sklearn.model_selection as skl

# Loading the Iris dataset
dataset = pd.read_csv('iris.csv')

# Creating the matrix of features (X) and the dependent variable vector (y)
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

# Printing the matrix of features and the dependent variable vector
print(X)
print(y)