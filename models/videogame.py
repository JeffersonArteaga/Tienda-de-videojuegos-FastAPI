from config.database import Base
from sqlalchemy import Column, Integer, Float, String

class Videogame(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = 'Videogames'

    # Definición de columnas y sus tipos de datos
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    overview = Column(String)
    rating = Column(Float)
    category = Column(String)
    price = Column(Float)
