from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from model.model import Model

class Appraiser:

    @staticmethod
    def assess(model, X_test, Y_test):
        """
        Avalia o desempenho do modelo com base em métricas de precisão.

        Arguments:
        model: O modelo de machine learning a ser avaliado.
        X_test: Dados de entrada para o teste.
        Y_test: Valores reais para comparação com as previsões.

        Returns:
        A acurácia do modelo nas predições.
        """
        
        # Fazendo previsões com o modelo fornecido
        predictions = Model.perform_predication(model, X_test)
        
        # Calculando e retornando a acurácia das previsões
        return accuracy_score(Y_test, predictions)
