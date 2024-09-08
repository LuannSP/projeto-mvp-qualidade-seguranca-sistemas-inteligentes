import numpy as np
import pickle
import joblib
from model.preprocessor import PreProcessor
from typing import Any


class Model:

    # TODO: Guardar model como atributo e o preditor receber as entradas.
    # TODO: preditor -> realiza_predicao

    def load_model(path):
        """Carrega o modelo de um arquivo .pkl"""
        try:
            # Verifica se o arquivo termina com .pkl
            if path.endswith('.pkl'):
                with open(path, 'rb') as file:
                    model = pickle.load(file)
                    return model
            else:
                raise Exception(
                    'Formato de arquivo não suportado. Use um arquivo .pkl.')

        # Tratamento de erros comuns
        except FileNotFoundError:
            print(f"Erro: Arquivo {path} não encontrado.")
        except pickle.UnpicklingError:
            print(f"Erro: O arquivo {
                  path} parece estar corrompido ou não é um arquivo pickle válido.")
        except Exception as e:
            print(f"Erro ao carregar o modelo: {e}")

        return None

    def perform_prediction(model, X_input):
        """Realiza a predição de um paciente com base no modelo treinado
        """
        diagnosis = model.predict(X_input)
        return diagnosis
