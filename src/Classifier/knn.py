from . import classify as classify
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

import pickle 

class KNN(classify.Classifier):
    def __init__(self, n):
        self.model = KNeighborsClassifier(n_neighbors=n, weights='distance')

    def train(self, trainingSets): 
        #TODO:
        ()

    def classify(self, observation): 
        #TODO:
        ()
