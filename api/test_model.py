from model import *

# To run: pytest -v test_model.py

# Instanciação das Classes
charger = Charger()
model = Model()
appraiser = Appraiser()

# Parâmetros    
url_dados = "./MachineLearning/data/advertising.csv"
colunas = ['TV', 'Radio', 'Jornal', 'Vendas','Resultado']

# Carga dos dados
dataset = Charger.data_loader(url_dados, colunas)
array = dataset.values
X = array[:,0:3]
y = array[:,4]
    
# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_modelo_lr():  
    # Importando o modelo de regressão logística
    lr_path = './MachineLearning/models/rf_advertising_classifier.pkl'
    modelo_lr = Model.load_model(lr_path)

    # Obtendo as métricas da Regressão Logística
    acuracia_lr = Appraiser.assess(modelo_lr, X, y)
    
    # Testando as métricas da Regressão Logística 
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_lr >= 0.78 
    # assert recall_lr >= 0.5 
    # assert precisao_lr >= 0.5 
    # assert f1_lr >= 0.5 
    
# # Método para testar pipeline Random Forest a partir do arquivo correspondente
# def test_modelo_rf():
#     # Importando pipeline de Random Forest
#     rf_path = './MachineLearning/pipelines/rf_advertising_pipeline.pkl'
#     modelo_rf = Pipeline.load_pipeline(rf_path)

#     # Obtendo as métricas do Random Forest
#     acuracia_rf = Appraiser.assess(modelo_rf, X, y)
    
#     # Testando as métricas do Random Forest
#     # Modifique as métricas de acordo com seus requisitos
#     assert acuracia_rf >= 0.78
#     # assert recall_rf >= 0.5 
#     # assert precisao_rf >= 0.5 
#     # assert f1_rf >= 0.5
#     # Método para testar modelo KNN a partir do arquivo correspondente
