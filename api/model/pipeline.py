import numpy as np
import pickle

class Pipeline:
    
    @staticmethod
    def load_pipeline(path: str):
        """Carrega o pipeline a partir de um arquivo pickle.

        Args:
            path (str): Caminho para o arquivo do pipeline.

        Returns:
            pipeline: Pipeline carregado.
        """
        with open(path, 'rb') as file:
            pipeline = pickle.load(file)
        return pipeline
