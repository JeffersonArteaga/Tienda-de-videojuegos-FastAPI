from config.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime

class UserPurchases(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "UserPurchases"

    # Definición de columnas y sus tipos de datos
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idUser = Column(Integer, ForeignKey('Users.id'))
    idVideogame = Column(Integer, ForeignKey('Videogames.id'))
    purchase_date = Column(DateTime, default=datetime.utcnow())

