import numpy as np
import pickle

class Pipeline:
    
    def load_pipeline(path):
        """ Carrega o pipeline gerado durante o treinamento """
        with open(path, 'rb') as file:
             pipeline = pickle.load(file)
        return pipeline     
