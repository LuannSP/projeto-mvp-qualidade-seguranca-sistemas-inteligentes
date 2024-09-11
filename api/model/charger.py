import pandas as pd

class Charger:

    def data_loader(url: str, atributos: list):
        """ Carrega e retorna um DataFrame """
        return pd.read_csv(url, names=atributos, header=0,
                           skiprows=0, delimiter=',')
