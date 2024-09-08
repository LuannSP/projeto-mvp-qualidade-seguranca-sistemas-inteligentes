import pandas as pd

class Charger:

    @staticmethod
    def data_loader(url: str, attributes: list) -> pd.DataFrame:
        """Carrega um DataFrame a partir de uma URL CSV.
        
        Args:
            url (str): URL do arquivo CSV.
            attributes (list): Lista de nomes das colunas para o DataFrame.

        Returns:
            pd.DataFrame: DataFrame carregado com os dados do CSV.
        """
        return pd.read_csv(url, names=attributes, header=0, skiprows=0, delimiter=',')
