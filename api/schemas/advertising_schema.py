from pydantic import BaseModel
from typing import Optional, List
from model.advertising import Advertising
import json
import numpy as np


class AdvertisingSchema(BaseModel):
    """ Define como um novo dado de publicidade deve ser representado """
    tv: str = 100.0
    radio: int = 200.0
    jornal: int = 300.0
    vendas: str = "B"  # Classificação das vendas: 'A' para Alto, 'M' para Médio, 'B' para Baixo


class AdvertisingViewSchema(BaseModel):
    """ Define como um dado de publicidade será retornado """
    id: int = 1
    tv: str = 100.0
    radio: int = 200.0
    jornal: int = 300.0
    vendas: str = "B"  # Classificação das vendas: 'A' para Alto, 'M' para Médio, 'B' para Baixo


class AdvertisingBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca por publicidade """
    tv: Optional[str] = None
    radio: Optional[int] = None
    jornal: Optional[int] = None
    vendas: Optional[str] = None


class ListaAdvertisingSchema(BaseModel):
    """ Define como uma lista de dados de publicidade será representada """
    advertising: List[AdvertisingViewSchema]


class AdvertisingDelSchema(BaseModel):
    """ Define como um dado de publicidade para deleção será representado """
    id: int = 1

# Apresenta apenas os dados de um dado de publicidade
def present_advertising(advertising: Advertising):
    """ Retorna uma representação do dado de publicidade seguindo o schema definido em
        AdvertisingViewSchema.
    """
    return {
        "id": advertising.id,
        "tv": advertising.tv,
        "radio": advertising.radio,
        "jornal": advertising.jornal,
        "vendas": advertising.vendas
    }

# Apresenta uma lista de dados de publicidade
def present_advertisings(advertisings: List[Advertising]):
    """ Retorna uma representação de uma lista de dados de publicidade seguindo o schema definido em
        AdvertisingViewSchema.
    """
    result = []
    for advertising in advertisings:
        result.append({
            "id": advertising.id,
            "tv": advertising.tv,
            "radio": advertising.radio,
            "jornal": advertising.jornal,
            "vendas": advertising.vendas
        })

    return {"advertising": result}
