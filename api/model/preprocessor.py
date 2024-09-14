from sklearn.model_selection import train_test_split
import pickle
import numpy as np

class PreProcessor:

    def separrate_test_training(self, dataset, percentual_teste, seed=7):
        """ Cuida do pré-processamento """
        X_train, X_test, Y_train, Y_test = self.__prepare_holdout(dataset,
                                                                  percentual_teste,
                                                                  seed)
        return (X_train, X_test, Y_train, Y_test)
    
    def __prepare_holdout(self, dataset, percentual_teste, seed):
        """ Divide os dados em treino e teste usando holdout """
        data = dataset.values
        X = data[:,0:3]
        Y = data[:,3]
        return train_test_split(X, Y, test_size=percentual_teste, random_state=seed)
    
    def prepare_form(form):
        """ Prepara os dados recebidos do front-end para serem usados no nosso modelo """
        X_input = np.array([form.tv,
                            form.radio,
                            form.jornal,
                        ])
        X_input = X_input.reshape(1, -1)
        return X_input
    
    def load_scaler(X_train):
        """ Normalização dos dados """
        scaler = pickle.load(open('./MachineLearning/scalers/minmax_scaler_advertising.pkl', 'rb'))
        reescaled_X_train = scaler.transform(X_train)
        return reescaled_X_train    
