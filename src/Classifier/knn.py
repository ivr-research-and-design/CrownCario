from . import classify as classify
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_splitfrom sklearn.metrics import confusion_matrix

import pickle #pickle is used to convert a python class to a file and vice versa

class KNN(classify.Classifier):
    def __init__(self, n):
        self.model = KNeighborsClassifier(n_neighbors=n, weights='distance')

    def train(self, trainingSets): 
        #TODO: trainingSets is the data we have analyzed paired with the correct 
        pass

    def classify(self, observation): 
        #TODO: 
        pass