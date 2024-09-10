from sklearn.model_selection import train_test_split
import pickle
import numpy as np

class PreProcessor:

    def separrate_test_training(self, dataset, percentual_teste, seed=7):
        """ Cuida de todo o pré-processamento. """
        # limpeza dos dados e eliminação de outliers

        # feature selection

        # divisão em treino e teste
        X_train, X_test, Y_train, Y_test = self.__prepare_holdout(dataset,
                                                                  percentual_teste,
                                                                  seed)
        # normalização/padronização
        
        return (X_train, X_test, Y_train, Y_test)
    
    def __prepare_holdout(self, dataset, percentual_teste, seed):
        """ Divide os dados em treino e teste usando o método holdout.
        Assume que a variável target está na última coluna.
        O parâmetro test_size é o percentual de dados de teste.
        """
        data = dataset.values
        X = data[:,0:3]
        Y = data[:,3]
        return train_test_split(X, Y, test_size=percentual_teste, random_state=seed)
    
    def prepare_form(form):
        """ Prepara os dados recebidos do front para serem usados no modelo. """
        X_input = np.array([form.tv,
                            form.radio,
                            form.jornal,
                        ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        X_input = X_input.reshape(1, -1)
        return X_input
    
    def load_scaler(X_train):
        """ Normaliza os dados. """
        # normalização/padronização
        scaler = pickle.load(open('./MachineLearning/scalers/minmax_scaler_advertising.pkl', 'rb'))
        reescaled_X_train = scaler.transform(X_train)
        return reescaled_X_train    
