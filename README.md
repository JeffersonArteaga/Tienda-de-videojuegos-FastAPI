# Tienda-de-videojuegos-FastAPI
Este proyecto de FastAPI representa una Tienda de Videojuegos, diseñada para gestionar la compra y venta de videojuegos entre clientes y administradores. 

# Como instalar el proyecto

Primero, debemos crear un entorno virtual de python (venv), para ejecutar un entorno virtual debemos ejecutar el comando:
python -m venv venv

Luego, para activar el entorno virtual ejecutamos el comando:
```
.\venv\Scripts\activate
```

Una vez activado el entorno virtuaal, vamos a clonar el repositorio del proyecto en el directorio donde creaste tu entorno virtual, una vez clonado el repositorio,
vamos a instalar las dependecias de nuestro proyecto, estas estan especificadas en el archivo requirements.txt, para eso, vamos a ejecutar el siguiente comando:
```
pip install -r requirements.txt
```

Con esto, nuestro proyecto estara instalado localmente

# Como ejecutar el proyecto

Una vez instalado por completo, vamos a ir al directorio raiz donde instalamos nuestro proyecto y ejecutamos el ssiguiente comando:
uvicorn main:app --reload

Con esto, se iniciara nuestro servidor, por defecto se ejecutara en el puerto 8000, si deseas cambiar el puerto, ejecuta el comando de la siguiente manera:
```
uvicorn main:app --reload --port <elpuertoquedesees>
```

# Como interactuar con la herramienta docs

Para poder interacturar de una vez por todas con el proyecto, deberas de ir a la ruta localhost:<elpuertoqueescogiste>/docs#/default
Una vez alli ya podras hacer las peticiones disponibles a los endpoints que aparecen

# Funcionalidades Principales:
1. Registro y Autenticación de Usuarios:
Los usuarios pueden registrarse en la plataforma proporcionando su correo electrónico, contraseña y nombre.
La autenticación se realiza mediante JWT (JSON Web Tokens), lo que permite a los usuarios iniciar sesión de manera segura.

2. Roles de Usuario:
Se implementan roles de usuario, como "Cliente" y "Administrador". El acceso a ciertas funcionalidades está restringido según el rol.

3. Catálogo de Videojuegos:
El catálogo contiene información sobre varios videojuegos, como nombre, descripción, clasificación, categoría y precio.

4. Operaciones de Administrador:
Los administradores tienen acceso a operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar el catálogo de videojuegos.

5. Operaciones de Cliente:
Los clientes pueden recargar puntos en su cuenta, comprar videojuegos y ver la lista de videojuegos que han comprado.

6. Seguridad:
La aplicación utiliza esquemas de seguridad basados en JWT para proteger las rutas y funcionalidades específicas.
Estructura del Proyecto:

7. Routers:
Se han creado módulos para diferentes entidades, como usuarios, videojuegos y operaciones de clientes y administradores.

8. Schemas:
Se definen esquemas Pydantic para la validación y serialización de datos en las operaciones de la API.

9. Modelos:
Representan las entidades principales del sistema y están vinculados a la base de datos mediante SQLAlchemy.

10. Base de Datos:
La aplicación utiliza una base de datos SQLite para almacenar información sobre usuarios, videojuegos y compras.

11. Seguridad:
Se implementan mecanismos de seguridad con FastAPI Security para gestionar la autenticación y autorización de usuarios.