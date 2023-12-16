from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base, Session

# Importar los routers que has definido
from routers.auth import auth_router
from routers.videogames import videogame_router
from routers.users import user_router
from routers.client import client_router

from models.user import User as UserModel

# Crear una instancia de FastAPI
app = FastAPI()

# Establecer un título para tu aplicación FastAPI
app.title = 'Mi tienda de videojuegos'

# Crear las tablas en la base de datos utilizando SQLAlchemy
Base.metadata.create_all(bind=engine)

# Incluir los routers en la aplicación
app.include_router(auth_router)
app.include_router(videogame_router)
app.include_router(user_router)
app.include_router(client_router)

# Iniciar la sesión de la base de datos
db = Session()

# Verificar si ya existe un usuario administrador
admin_user = db.query(UserModel).filter_by(email='admin@example.com').first()

if not admin_user:
    # Si no existe, crear un usuario administrador
    admin_data = {
        'name': 'Admin',
        'email': 'admin@example.com',
        'password': 'admin_password',  # Asegúrate de usar contraseñas seguras en la práctica
        'role': 'Admin',
        'points': 1000  # Otra información específica del usuario administrador
    }

    new_admin = UserModel(**admin_data)
    db.add(new_admin)
    db.commit()

    print("Usuario administrador creado con éxito.")

# Cerrar la sesión de la base de datos
db.close()


# Definir una ruta para la página de inicio
@app.get('/', tags=['home'])
def message():
    # Responder con contenido HTML
    return HTMLResponse(content='''
                    <h1>En términos de front, no hay front</h1>
                  ''', status_code=200)