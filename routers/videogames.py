from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from middlewares.jwt_bearer_admin import JWTBearerAdmin
from typing import List

from models.videogame import Videogame as VideogameModel
from schemas.videogame import Videogame

# Creación de un router específico para las rutas relacionadas con videojuegos
videogame_router = APIRouter()


# Ruta para obtener todos los videojuegos
@videogame_router.get('/videogames', tags=['videogames'], response_model=List[Videogame], status_code=200)
def getVideogames() -> List[Videogame]:
    db = Session()
    result = db.query(VideogameModel).all()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


# Ruta para crear un nuevo videojuego
@videogame_router.post('/videogames', tags=['videogames'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearerAdmin())])
def createVideogame(videogame: Videogame):
    db = Session()
    new_videogame = VideogameModel(**videogame.model_dump())
    db.add(new_videogame)
    db.commit()
    return JSONResponse(content={'Message': 'Videogame created successfully'}, status_code=201)


# Ruta para actualizar un videojuego existente
@videogame_router.put('/videogames/{id}', tags=['videogames'], response_model=dict, dependencies=[Depends(JWTBearerAdmin())])
def updateVideogame(id: int, videogame: Videogame):
    db = Session()
    result = db.query(VideogameModel).filter(VideogameModel.id == id).first()

    if not result:
        return JSONResponse(content={"message": "Videogame not found"}, status_code=404)

    # Actualización de los atributos del videojuego
    result.name = videogame.name
    result.overview = videogame.overview
    result.rating = videogame.rating
    result.category = videogame.category
    result.price = videogame.price

    db.commit()
    return JSONResponse(content={'Message': 'Videogame updated successfully'}, status_code=200)


# Ruta para eliminar un videojuego existente
@videogame_router.delete('/videogames/{id}', tags=['videogames'], response_model=dict, dependencies=[Depends(JWTBearerAdmin())])
def deleteVideogame(id: int):
    db = Session()
    result = db.query(VideogameModel).filter(VideogameModel.id == id).first()

    if not result:
        response = JSONResponse(content={"message": "Videogame not found"}, status_code=404)
    else:
        db.delete(result)
        db.commit()
        response = JSONResponse(content={"message": "Videogame deleted successfully"}, status_code=200)

    return response
