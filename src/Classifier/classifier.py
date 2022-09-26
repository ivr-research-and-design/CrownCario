# Code acquired from https://github.com/neurotech-uiuc/R-Cario/blob/main/Classifier/classify.py
# from RSO NeuroTechX of the University of Illinois at Urbana-Champaign

from abc import ABC, abstractmethod # for abstract class

class Classifier(ABC):
    def __init__(self, modelfile):
        self.modelfile = modelfile
        super().__init__()

    # trainingData -> Array of observations
    @abstractmethod
    def train(self, trainingData):
        pass

    @abstractmethod
    def classify(self, observation):
        pass