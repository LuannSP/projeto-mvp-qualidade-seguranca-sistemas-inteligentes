from model import *
from sklearn.preprocessing import MinMaxScaler

# To run: pytest -v test_model.py

# Instanciação das Classes
carregador = Charger()
modelo = Model()
avaliador = Appraiser()

# Parâmetros
url_dados = "./MachineLearning/data/advertising.csv"
colunas = ['TV', 'Radio', 'Jornal', 'Resultado']

# Carga dos dados
dataset = Charger.data_loader(url_dados, colunas)
array = dataset.values
X = array[:, 0:3]
y = array[:, 3]

# Método para testar o modelo
def test_modelo_lr():
    lr_path = './MachineLearning/models/rf_advertising_classifier.pkl'
    modelo_lr = Model.load_model(lr_path)
    scaler = MinMaxScaler().fit(X)
    rescaledX = scaler.transform(X)
    acuracia_lr = Appraiser.assess(modelo_lr, rescaledX, y)

    assert acuracia_lr >= 0.75

# Método para testar pipeline Random Forest
def test_modelo_rf():
    rf_path = './MachineLearning/pipelines/rf_advertising_pipeline.pkl'
    modelo_rf = Pipeline.load_pipeline(rf_path)
    acuracia_rf = Appraiser.assess(modelo_rf, X, y)

    assert acuracia_rf >= 0.75
