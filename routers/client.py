from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from datetime import datetime

from models.user import User as UserModel
from models.userPurchases import UserPurchases as UserPurchasesModel
from models.videogame import Videogame as VideogameModel

from schemas.payPoints import PayPoints
from schemas.videogame import Videogame

# Creación de un router específico para las rutas relacionadas con el cliente
client_router = APIRouter()


# Ruta para recargar puntos en la cuenta del usuario
@client_router.put('/payPoints', tags=['client'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def payPoints(paypoint: PayPoints, current_user: dict = Depends(JWTBearer())):
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == current_user['id']).first()

    if not result:
        return JSONResponse(content={"message": "User not found"}, status_code=404)

    # Recarga de puntos en la cuenta del usuario
    result.points += paypoint.mount
    db.commit()

    return JSONResponse(content={'message': 'Successful recharge'}, status_code=200)


# Ruta para realizar la compra de un videojuego
@client_router.post('/buyVideogame/{id}', tags=['client'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def buyVideogame(id: int, current_user: dict = Depends(JWTBearer())):
    db = Session()
    purchase_data = {}
    result_videogame = db.query(VideogameModel).filter(VideogameModel.id == id).first()
    result_user = db.query(UserModel).filter(UserModel.id == current_user['id']).first()

    if result_videogame is None:
        return JSONResponse(content={'Message': 'Videogame not found'}, status_code=404)

    if (result_user.points < result_videogame.price):
        return JSONResponse(content={'Message': 'Insufficient funds'}, status_code=402)

    # Realización de la compra y actualización de puntos del usuario
    result_user.points -= result_videogame.price
    purchase_data['idUser'] = current_user['id']
    purchase_data['idVideogame'] = result_videogame.id

    new_purchase = UserPurchasesModel(**purchase_data)
    db.add(new_purchase)
    db.commit()

    return JSONResponse(content={'Message': 'Successful payment'}, status_code=201)


# Ruta para obtener la lista de videojuegos comprados por el usuario
@client_router.get('/videogamesUser', tags=['client'], response_model=List[Videogame], status_code=200, dependencies=[Depends(JWTBearer())])
def getVideogamesUser(current_user: dict = Depends(JWTBearer())) -> List[Videogame]:
    db = Session()
    result = db.query(UserPurchasesModel).filter(UserPurchasesModel.idUser == current_user['id']).all()

    if not result:
        response = JSONResponse(content={'Message': "The user hasn't purchased any video games"}, status_code=200)
    else:
        response = JSONResponse(content=jsonable_encoder(result), status_code=200)

    return response
