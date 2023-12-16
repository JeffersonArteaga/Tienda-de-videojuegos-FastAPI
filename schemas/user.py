from pydantic import BaseModel, Field

# Definición de la clase User utilizando Pydantic
class User(BaseModel):
    # Atributos de la clase User con sus tipos
    email: str  # Correo electrónico del usuario (tipo: str)
    password: str  # Contraseña del usuario (tipo: str)

# Definición de la clase UserCreate que hereda de User
class UserCreate(User):
    # Atributo adicional para la creación de usuario
    name: str  # Nombre del usuario (tipo: str)

# Definición de la clase UserUpdated que hereda de UserCreate
class UserUpdated(UserCreate):
    # Atributo adicional para la actualización de usuario
    points: float = Field(..., gt=0)  # Puntos del usuario (tipo: float)