from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from config.database import Session
from middlewares.jwt_bearer_admin import JWTBearerAdmin
from models.user import User as UserModel
from schemas.user import User, UserCreate, UserUpdated

# Creación de un router específico para las rutas relacionadas con usuarios
user_router = APIRouter()


# Ruta para obtener todos los usuarios
@user_router.get('/users', tags=['users'], response_model=List[User], status_code=200, dependencies=[Depends(JWTBearerAdmin())])
def getUsers() -> List[User]:
    db = Session()
    result = db.query(UserModel).all()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


# Ruta para crear un nuevo usuario (con rol de administrador)
@user_router.post('/users', tags=['users'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearerAdmin())])
def createUseradmin(user: UserCreate):
    db = Session()
    existing_user = db.query(UserModel).filter(UserModel.email == user.email).first()

    if existing_user:
        result = JSONResponse(content={'message': 'Email already registered'}, status_code=400)
    else:
        # Creación de un nuevo usuario con rol de administrador y puntos iniciales
        user_data = user.model_dump()
        user_data['role'] = 'Admin'
        user_data['points'] = 100

        new_user = UserModel(**user_data)
        db.add(new_user)
        db.commit()
        result = JSONResponse(content={'message': 'User created successfully'}, status_code=201)

    return result


# Ruta para actualizar un usuario existente
@user_router.put('/users/{id}', tags=['users'], response_model=dict, dependencies=[Depends(JWTBearerAdmin())])
def updateUser(id: int, user: UserUpdated):
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()

    if not result:
        return JSONResponse(content={"message": "User not found"}, status_code=404)

    # Actualización de los atributos del usuario
    result.name = user.name
    result.password = user.password
    result.email = user.email
    result.points = user.points

    db.commit()
    return JSONResponse(content={'Message': 'User updated successfully'}, status_code=200)


# Ruta para eliminar un usuario existente
@user_router.delete('/users/{id}', tags=['users'], response_model=dict, dependencies=[Depends(JWTBearerAdmin())])
def deleteUser(id: int):
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()

    if not result:
        response = JSONResponse(content={"message": "User not found"}, status_code=404)
    else:
        db.delete(result)
        db.commit()
        response = JSONResponse(content={"message": "User deleted successfully"}, status_code=200)

    return response
