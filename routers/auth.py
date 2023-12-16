from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import Session
from utils.jwt_manager import create_token

from models.user import User as UserModel

from schemas.user import User, UserCreate

# Creación de un router específico para las rutas de autenticación
auth_router = APIRouter()


# Ruta para registrar un nuevo usuario
@auth_router.post('/register', tags=['auth'], response_model=dict, status_code=200)
def registerUser(user: UserCreate):
    db = Session()

    existing_user = db.query(UserModel).filter(UserModel.email == user.email).first()

    if existing_user:
        result = JSONResponse(content={'message': 'Email already registered'}, status_code=400)
    else:
        user_data = user.model_dump()
        user_data['role'] = 'client'
        user_data['points'] = 100

        new_user = UserModel(**user_data)
        db.add(new_user)
        db.commit()
        result = JSONResponse(content={'message': 'User created successfully'}, status_code=201)

    return result


# Ruta para realizar el inicio de sesión
@auth_router.post('/login', tags=['auth'], response_model=dict, status_code=200)
def login(user: User):
    db = Session()
    query = db.query(UserModel).filter(UserModel.email == user.email, UserModel.password == user.password).first()

    if query:
        user_data = user.model_dump()
        user_data['id'] = query.id
        user_data['name'] = query.name
        user_data['role'] = query.role
        user_data['points'] = query.points

        # Creación de un token JWT con la información del usuario
        token = create_token(data=user_data)
        result = JSONResponse(content={'Message': 'Successfully logged', 'token': token }, status_code=200)
    else:
        result = JSONResponse(content={'Message': 'Invalid credentials' }, status_code=401)

    return result
