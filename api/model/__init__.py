from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# Importando os elementos definidos no modelo
from model.base import Base
from model.advertising import Advertising
from model.model import Model
from model.pipeline import Pipeline
from model.preprocessor import PreProcessor
from model.appraiser import Appraiser
from model.charger import Charger

# Define o caminho do banco de dados
db_path = "database/"

# Verifica e cria o diretório do banco de dados, se não existir
os.makedirs(db_path, exist_ok=True)

# Define a URL de conexão para o banco de dados SQLite
db_url = f'sqlite:///{db_path}advertising.sqlite3'

# Cria a engine para conectar ao banco de dados
engine = create_engine(db_url, echo=False)

# Instancia um criador de sessões para interagir com o banco de dados
Session = sessionmaker(bind=engine)

# Cria o banco de dados se ele ainda não existir
if not database_exists(engine.url):
    create_database(engine.url)

# Cria as tabelas no banco de dados com base nos modelos definidos, se não existirem
Base.metadata.create_all(engine)
