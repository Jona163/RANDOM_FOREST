# Autor: Jonathan Hernández
# Fecha: 21 octubre 2024
# Descripción: Random Forests.
# GitHub: https://github.com/Jona163

from random import random
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from RandomForest import RandomForest

data = datasets.load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234
)
