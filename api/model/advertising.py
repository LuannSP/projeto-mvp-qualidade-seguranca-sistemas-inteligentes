from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from model import Base

# Definição da tabela "advertising" para armazenar os dados de investimentos em propaganda e o resultado das vendas

class Advertising(Base):
    __tablename__ = 'advertising'
    
    id = Column(Integer, primary_key=True)  # Identificador único da entrada
    tv = Column("TV", Float)                # Investimento em TV (float para aceitar valores decimais)
    radio = Column("Radio", Float)          # Investimento em Rádio (float para aceitar valores decimais)
    jornal = Column("Jornal", Float)        # Investimento em Jornal (float para aceitar valores decimais)
    vendas = Column("Vendas", String(1))    # Classificação de vendas: 'B' = Baixo, 'M' = Médio, 'A' = Alto
    data_insercao = Column(DateTime, default=datetime.now())  # Data de inserção no banco

    def __init__(self, tv: float, radio: float, jornal: float, vendas: str, 
                 data_insercao: Union[DateTime, None] = None):
        """
        Cria uma instância de Advertising para armazenar dados de investimento e vendas.

        Arguments:
        tv: investimento em TV (ex: 1000.00)
        radio: investimento em Rádio (ex: 500.50)
        jornal: investimento em Jornal (ex: 300.75)
        vendas: classificação das vendas: 'B' = Baixo, 'M' = Médio, 'A' = Alto
        data_insercao: data de quando o registro foi inserido (opcional, se não fornecido, será a data atual)
        """
        self.tv = tv
        self.radio = radio
        self.jornal = jornal
        self.vendas = vendas

        # Se a data de inserção não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
