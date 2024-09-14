from pydantic import BaseModel
from typing import Optional, List
from model.advertising import Advertising
import json
import numpy as np


class AdvertisingSchema(BaseModel):
    """ Define como um novo dado de publicidade deve ser representado """
    tv: float = 100.0
    radio: float = 200.0
    jornal: float = 300.0

class AdvertisingViewSchema(BaseModel):
    """ Define como um dado de publicidade será retornado """
    id: int = 1
    tv: float = 100.0
    radio: float = 200.0
    jornal: float = 300.0
    resultado: int = 1 

class AdvertisingSearchSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca por publicidade """
    resultado: int = 1

class ListAdvertisingSchema(BaseModel):
    """ Define como uma lista de dados de publicidade será representada """
    advertising: List[AdvertisingViewSchema]

class AdvertisingDelSchema(BaseModel):
    """ Define como um dado de publicidade para deleção será representado """
    id: int = 1

# Apresenta apenas os dados de um dado de publicidade
def present_advertising(advertising: Advertising) -> dict:
    """ Retorna uma representação do dado de publicidade seguindo o schema definido em AdvertisingViewSchema """
    return {
        "id": advertising.id,
        "tv": advertising.tv,
        "radio": advertising.radio,
        "jornal": advertising.jornal,
        "resultado": advertising.resultado
    }

# Apresenta uma lista de dados de publicidade
def present_advertisings(advertisings: List[Advertising]) -> dict:
    """ Retorna uma representação de uma lista de dados de publicidade seguindo o schema definido em AdvertisingViewSchema """
    result = []
    for advertising in advertisings:
        result.append({
            "id": advertising.id,
            "tv": advertising.tv,
            "radio": advertising.radio,
            "jornal": advertising.jornal,
            "resultado": advertising.resultado
        })

    return {"advertising": result}
