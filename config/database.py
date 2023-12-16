import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define el nombre del archivo de base de datos SQLite y establece la ruta relativa al directorio actual.
sql_file_name = "../database.sqlite"

# Obtiene el directorio base del archivo actual utilizando os.path.realpath(__file__).
# os.path.realpath(__file__) devuelve la ruta completa del archivo actual.
base_dir = os.path.dirname(os.path.realpath(__file__))

# Construye la URL de la base de datos SQLite combinando el prefijo "sqlite:///" con la ruta completa al archivo de base de datos.
database_url = f'sqlite:///{os.path.join(base_dir, sql_file_name)}'

# Crea un motor de base de datos utilizando la URL de la base de datos SQLite y activa la opción echo para imprimir consultas SQL.
engine = create_engine(database_url, echo=True)

# Configura una fábrica de sesiones utilizando el motor de la base de datos creado anteriormente.
Session = sessionmaker(bind=engine)

# Crea una clase base declarativa que se utilizará como base para definir modelos de SQLAlchemy.
Base = declarative_base()
