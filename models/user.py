from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class User(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = 'Users'

    # Definición de columnas y sus tipos de datos
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String)
    points = Column(Float)