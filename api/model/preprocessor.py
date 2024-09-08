from sklearn.model_selection import train_test_split
import pickle
import numpy as np

class PreProcessor:

    def separate_test_training(self, dataset, test_size, seed=7):
        """Realiza o pré-processamento dos dados, incluindo a divisão em conjuntos de treino e teste, 
        e a normalização dos dados.

        Args:
            dataset (pd.DataFrame): Conjunto de dados a ser processado.
            test_size (float): Percentual do conjunto de dados a ser usado como teste.
            seed (int): Semente para a reprodutibilidade.

        Returns:
            tuple: Conjuntos de dados de treino e teste (X_train, X_test, Y_train, Y_test).
        """
        # Dividir dados em treino e teste
        X_train, X_test, Y_train, Y_test = self.__prepare_holdout(dataset, test_size, seed)
        
        # Normalizar os dados de treino
        X_train = self.scaler(X_train)
        X_test = self.scaler(X_test)

        return X_train, X_test, Y_train, Y_test
    
    def __prepare_holdout(self, dataset, test_size, seed):
        """Divide os dados em conjuntos de treino e teste.

        Args:
            dataset (pd.DataFrame): Conjunto de dados a ser dividido.
            test_size (float): Percentual do conjunto de dados a ser usado como teste.
            seed (int): Semente para a reprodutibilidade.

        Returns:
            tuple: Conjuntos de dados de treino e teste (X_train, X_test, Y_train, Y_test).
        """
        data = dataset.values
        X = data[:, :-1]  # Todas as colunas exceto a última
        Y = data[:, -1]   # Última coluna como target
        return train_test_split(X, Y, test_size=test_size, random_state=seed)
    
    @staticmethod
    def prepare_form(form):
        """Prepara os dados recebidos do formulário para serem usados no modelo.

        Args:
            form: Objeto com os dados do formulário.

        Returns:
            np.ndarray: Dados preparados para predição.
        """
        X_input = np.array([
            form.tv,
            form.radio,
            form.jornal,
            form.vendas
        ])
        # Ajusta a forma dos dados para que o modelo possa fazer a predição
        return X_input.reshape(1, -1)
    
    @staticmethod
    def scaler(X):
        """Normaliza os dados usando um scaler previamente treinado.

        Args:
            X (np.ndarray): Dados a serem normalizados.

        Returns:
            np.ndarray: Dados normalizados.
        """
        scaler = pickle.load(open('./MachineLearning/scalers/minmax_scaler_advertising.pkl', 'rb'))
        return scaler.transform(X)
