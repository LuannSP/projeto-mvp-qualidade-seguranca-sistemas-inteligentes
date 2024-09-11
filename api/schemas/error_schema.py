from pydantic import BaseModel

class ErrorSchema(BaseModel):
    """ Define a estrutura da mensagem de erro retornada """
    message: str
