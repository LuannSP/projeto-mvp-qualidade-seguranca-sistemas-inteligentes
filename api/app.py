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
advertising_tag = Tag(name="Propaganda", description="Adição, visualização, remoção e predição de vendas com base em investimentos publicitários em TV, rádio e jornal")

# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para Swagger.
    """
    return redirect('/openapi/swagger')




charger = Charger()
model = Model()
appraiser = Appraiser()
   
url_dados = "./MachineLearning/data/advertising.csv"
colunas = ['TV', 'Radio', 'Jornal','Resultado']

dataset = Charger.data_loader(url_dados, colunas)
array = dataset.values
X = array[:,0:3]
y = array[:,3]

# lr_path = './MachineLearning/models/rf_advertising_classifier.pkl'
# modelo_lr = Model.load_model(lr_path)

# acuracia_lr = Appraiser.assess(modelo_lr, X, y)

# print(acuracia_lr)

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


# # Rota de adição de paciente
# @app.post('/paciente', tags=[paciente_tag],
#           responses={"200": PacienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
# def predict(form: PacienteSchema):
#     """Adiciona um novo paciente à base de dados
#     Retorna uma representação dos pacientes e diagnósticos associados.

#     Args:
#         name (str): nome do paciente
#         preg (int): número de vezes que engravidou: Pregnancies
#         plas (int): concentração de glicose no plasma: Glucose
#         pres (int): pressão diastólica (mm Hg): BloodPressure
#         skin (int): espessura da dobra cutânea do tríceps (mm): SkinThickness
#         test (int): insulina sérica de 2 horas (mu U/ml): Insulin
#         mass (float): índice de massa corporal (peso em kg/(altura em m)^2): BMI
#         pedi (float): função pedigree de diabetes: DiabetesPedigreeFunction
#         age (int): idade (anos): Age

#     Returns:
#         dict: representação do paciente e diagnóstico associado
#     """
#     # TODO: Instanciar classes

#     # Recuperando os dados do formulário
#     name = form.name
#     preg = form.preg
#     plas = form.plas
#     pres = form.pres
#     skin = form.skin
#     test = form.test
#     mass = form.mass
#     pedi = form.pedi
#     age = form.age

#     # Preparando os dados para o modelo
#     X_input = PreProcessador.preparar_form(form)
#     # Carregando modelo
#     model_path = './MachineLearning/pipelines/rf_diabetes_pipeline.pkl'
#     # modelo = Model.carrega_modelo(ml_path)
#     modelo = Pipeline.carrega_pipeline(model_path)
#     # Realizando a predição
#     outcome = int(Model.preditor(modelo, X_input)[0])

#     paciente = Paciente(
#         name=name,
#         preg=preg,
#         plas=plas,
#         pres=pres,
#         skin=skin,
#         test=test,
#         mass=mass,
#         pedi=pedi,
#         age=age,
#         outcome=outcome
#     )

#     try:
#         # Criando conexão com a base
#         session = Session()

#         # Checando se paciente já existe na base
#         if session.query(Paciente).filter(Paciente.name == form.name).first():
#             error_msg = "Paciente já existente na base :/"
#             return {"message": error_msg}, 409

#         # Adicionando paciente
#         session.add(paciente)
#         # Efetivando o comando de adição
#         session.commit()
#         # Concluindo a transação
#         return apresenta_paciente(paciente), 200

#     # Caso ocorra algum erro na adição
#     except Exception as e:
#         error_msg = "Não foi possível salvar novo item :/"
#         return {"message": error_msg}, 400


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
