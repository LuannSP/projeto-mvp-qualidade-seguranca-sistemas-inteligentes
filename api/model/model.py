import numpy as np
import pickle
import joblib
from model.preprocessor import PreProcessor

class Model:

    @staticmethod
    def load_model(path: str):
        """Carrega um modelo a partir de um arquivo, dependendo da extensão.

        Args:
            path (str): Caminho para o arquivo do modelo.

        Returns:
            model: Modelo carregado.
        
        Raises:
            Exception: Se o formato do arquivo não for suportado.
        """
        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                model = pickle.load(file)
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    @staticmethod
    def perform_predication(model, X_input):
        """Realiza a predição com base no modelo treinado.

        Args:
            model: Modelo treinado.
            X_input: Dados de entrada para a predição.

        Returns:
            numpy.ndarray: Resultados da predição.
        """
        return model.predict(X_input)
