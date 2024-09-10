from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from model import *
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="API Advertising", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação",description="Redireciona para a documentação do Swagger.")
advertising_tag = Tag(name="Propaganda", description="XXXXX predição de vendas com base em investimentos publicitários em TV, rádio e jornal")

# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para Swagger.
    """
    return redirect('/openapi/swagger')

@app.post('/propaganda', tags=[advertising_tag],responses={"200": AdvertisingViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: AdvertisingSchema):
    tv = form.tv
    radio = form.radio
    jornal = form.jornal

    X_input = PreProcessor.prepare_form(form)
    model_path = './MachineLearning/pipelines/rf_advertising_pipeline.pkl'
    modelo = Pipeline.load_pipeline(model_path)
    resultado = int(Model.perform_prediction(modelo, X_input)[0])

    advertising = Advertising(
        tv=tv,
        radio=radio,
        jornal=jornal,
        resultado=resultado
    )

    try:
        session = Session()
        session.add(advertising)
        session.commit()
        return present_advertising(advertising), 200

    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        return {"message": error_msg}, 400

# # Rota de listagem de pacientes
# @app.get('/pacientes', tags=[paciente_tag],
#          responses={"200": PacienteViewSchema, "404": ErrorSchema})
# def get_pacientes():
#     """Lista todos os pacientes cadastrados na base
#     Args:
#        none

#     Returns:
#         list: lista de pacientes cadastrados na base
#     """
#     # Criando conexão com a base
#     session = Session()
#     # Buscando todos os pacientes
#     pacientes = session.query(Paciente).all()

#     if not pacientes:
#         # Se não houver pacientes
#         return {"pacientes": []}, 200
#     else:
#         print(pacientes)
#         return apresenta_pacientes(pacientes), 200

# # Métodos baseados em nome
# # Rota de busca de paciente por nome
# @app.get('/paciente', tags=[paciente_tag],
#          responses={"200": PacienteViewSchema, "404": ErrorSchema})
# def get_paciente(query: PacienteBuscaSchema):
#     """Faz a busca por um paciente cadastrado na base a partir do nome

#     Args:
#         nome (str): nome do paciente

#     Returns:
#         dict: representação do paciente e diagnóstico associado
#     """

#     paciente_nome = query.name
#     # criando conexão com a base
#     session = Session()
#     # fazendo a busca
#     paciente = session.query(Paciente).filter(Paciente.name == paciente_nome).first()

#     if not paciente:
#         # se o paciente não foi encontrado
#         error_msg = f"Paciente {paciente_nome} não encontrado na base :/"
#         return {"mesage": error_msg}, 404
#     else:
#         # retorna a representação do paciente
#         return apresenta_paciente(paciente), 200


# # Rota de remoção de paciente por nome
# @app.delete('/paciente', tags=[paciente_tag],
#             responses={"200": PacienteViewSchema, "404": ErrorSchema})
# def delete_paciente(query: PacienteBuscaSchema):
#     """Remove um paciente cadastrado na base a partir do nome

#     Args:
#         nome (str): nome do paciente

#     Returns:
#         msg: Mensagem de sucesso ou erro
#     """

#     paciente_nome = unquote(query.name)

#     # Criando conexão com a base
#     session = Session()

#     # Buscando paciente
#     paciente = session.query(Paciente).filter(Paciente.name == paciente_nome).first()

#     if not paciente:
#         error_msg = "Paciente não encontrado na base :/"
#         return {"message": error_msg}, 404
#     else:
#         session.delete(paciente)
#         session.commit()
#         return {"message": f"Paciente {paciente_nome} removido com sucesso!"}, 200

# if __name__ == '__main__':
#     app.run(debug=True)
