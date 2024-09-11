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
advertising_tag = Tag(name="Propaganda", description="Adição, visualização, remoção e previsão de vendas com base em investimentos em TV, rádio e jornal.")

# Rota Inicial
@app.get('/', tags=[home_tag])
def home():
    """ Redireciona para Swagger """
    return redirect('/openapi/swagger')

# Rota para inserir um novo registro
@app.post('/propaganda', tags=[advertising_tag],responses={"200": AdvertisingViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: AdvertisingSchema):
    """ Adiciona um novo registro de investimento publicitário à base de dados
    Realiza a predição de vendas com base nos valores investidos em TV, rádio e jornal, 
    e armazena o registro no banco de dados.

    Args:
        tv (float): valor investido em propagandas de TV
        radio (float): valor investido em propagandas de rádio
        jornal (float): valor investido em propagandas de jornal

    Returns:
        dict: representação do registro de investimento publicitário e a predição de vendas associada
    """
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
        error_msg = "Erro ao inserir um registro."
        return {"message": error_msg}, 400

# Rota de listagem de investimentos
@app.get('/propagandas', tags=[advertising_tag],responses={"200": AdvertisingViewSchema, "404": ErrorSchema})
def get_advertisings():
    """ Lista todos os registros de investimentos publicitários cadastrados na base de dados.
    
    Args:
        none

    Returns:
        list: lista de investimentos publicitários cadastrados, incluindo valores de TV, rádio, jornal e o resultado previsto.
    """
    session = Session()
    pacientes = session.query(Advertising).all()

    if not pacientes:
        return {"advertisings": []}, 200
    else:
        return present_advertisings(pacientes), 200

# Rota de remoção de investimentos por id.
@app.delete('/propaganda', tags=[advertising_tag], responses={"200": AdvertisingViewSchema, "404": ErrorSchema})
def delete_paciente(query: AdvertisingDelSchema):
    """ Remove um investimento publicitário cadastrado na base a partir do ID.

    Args:
        id (int): ID do investimento publicitário

    Returns:
        dict: Mensagem de sucesso ou erro
    """
    advertising_id = query.id  # Removido unquote pois o id é numérico
    session = Session()
    advertising = session.query(Advertising).filter(Advertising.id == advertising_id).first()

    if not advertising:
        error_msg = "Investimento não encontrado no banco de dados."
        return {"message": error_msg}, 404
    else:
        session.delete(advertising)
        session.commit()
        return {"message": f"Investimento com o id: {advertising_id} removido com sucesso."}, 200

# Rota de busca de investimentos por resultado
@app.get('/propaganda', tags=[advertising_tag], responses={"200": ListAdvertisingSchema, "404": ErrorSchema})
def get_advertising_by_result(query: AdvertisingSearchSchema):
    """ Faz a busca por todos os investimentos publicitários cadastrados na base com o resultado especificado.

    Args:
        resultado (str): resultado do investimento publicitário

    Returns:
        dict: lista de investimentos publicitários associados ao resultado
    """
    advertising_result = query.resultado
    session = Session()
    advertisings = session.query(Advertising).filter(Advertising.resultado == advertising_result).all()

    if not advertisings:
        return {"advertisings": []}, 200
    else:
        return present_advertisings(advertisings), 200

if __name__ == '__main__':
    app.run(debug=True)
