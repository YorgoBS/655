import pandas as pd
import numpy as np
import sklearn # pip3 install scikit-learn
from sklearn import svm , preprocessing
import pickle

class Detect:
    
    
    def __init__(self, datafile ,weights = 'INSERT PICKLE FILE HERE'):
        self.df = pd.read_csv(datafile)
        self.df = self.df.fillna(self.df.median()).clip(-1e11,1e11)
        self.X = self.df.values
        self.loaded_model = pickle.load(open(weights, 'rb'))

    def predict(self):
        result = self.loaded_model.predict(self.X)
        list_result = result.tolist()
        # for index in range(len(list_result)):
            # if list_result[index] == -1:
            #     list_result[index] = "Malicious"
            # elif list_result[index] == 1:
            #     list_result[index] = "Safe"
            # else:
            #     pass
            

        return list_result