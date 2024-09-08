from sqlalchemy import Column, Integer, DateTime, Float
from datetime import datetime
from typing import Union
from model import Base

# Definição da tabela "advertising" para armazenar os dados de investimentos em propaganda e o resultado das vendas

class Advertising(Base):
    __tablename__ = 'advertising'
    
    id = Column(Integer, primary_key=True)   # Identificador único da entrada
    tv = Column("TV", Float)                 # Investimento em TV (float para aceitar valores decimais)
    radio = Column("Radio", Float)           # Investimento em Rádio (float para aceitar valores decimais)
    jornal = Column("Jornal", Float)         # Investimento em Jornal (float para aceitar valores decimais)
    resultado = Column("Resultado", Integer) # Classificação de vendas como valor inteiro
    data_insercao = Column(DateTime, default=datetime.now())  # Data de inserção no banco

    def __init__(self, tv: float, radio: float, jornal: float, resultado: int, 
                 data_insercao: Union[DateTime, None] = None):
        """
        Cria uma instância de Advertising para armazenar dados de investimento e o resultado das vendas.

        Arguments:
        tv: investimento em TV (ex: 1000.00)
        radio: investimento em Rádio (ex: 500.50)
        jornal: investimento em Jornal (ex: 300.75)
        resultado: resultado do modelo como um valor inteiro
        data_insercao: data de quando o registro foi inserido (opcional, se não fornecido, será a data atual)
        """
        self.tv = tv
        self.radio = radio
        self.jornal = jornal
        self.resultado = resultado

        # Se a data de inserção não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
