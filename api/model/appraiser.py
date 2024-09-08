from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from model.model import Model


class Appraiser:

    def assess(model, X_test, Y_test):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        predictions = Model.perform_prediction(model, X_test)

        # Caso o seu problema tenha mais do que duas classes, altere o parâmetro average
        return accuracy_score(Y_test, predictions)
