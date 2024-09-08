# import pytest
# import numpy as np
# from model import Charger, Model, Appraiser

# # Para rodar: pytest -v test_model.py

# # Instanciação das Classes
# charger = Charger()
# model = Model()
# appraiser = Appraiser()

# # Parâmetros
# url_data = "./MachineLearning/data/advertising.csv"
# column = ['TV', 'Radio', 'Jornal', 'Vendas']

# # Carga dos dados
# dataset = charger.data_loader(url_data, column)
# array = dataset.values
# X = array[:, 0:-1]
# y = array[:, -1]


# def test_modelo_lr():
#     # Importando o modelo de regressão logística
#     lr_path = './MachineLearning/models/rf_advertising_classifier.pkl'

#     # Carregar o modelo
#     modelo_lr = Model.load_model(lr_path)

#     # Obtendo as métricas do modelo
#     metrics = Appraiser.assess(modelo_lr, X, y)

#     # Testando as métricas do modelo
#     assert metrics['accuracy'] >= 0.78
#     assert metrics['recall'] >= 0.5
#     assert metrics['precision'] >= 0.5
#     assert metrics['f1'] >= 0.5

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

# Método para testar modelo KNN a partir do arquivo correspondente
# def test_modelo_knn():
#     # Importando modelo de KNN
#     knn_path = './MachineLearning/models/diabetes_knn.pkl'
#     modelo_knn = Model.load_model(knn_path)

#     # Obtendo as métricas do KNN
#     acuracia_knn = Appraiser.assess(modelo_knn, X, y)

#     # Testando as métricas do KNN
#     # Modifique as métricas de acordo com seus requisitos
#     assert acuracia_knn >= 0.78
#     # assert recall_knn >= 0.5
#     # assert precisao_knn >= 0.5
#     # assert f1_knn >= 0.5
