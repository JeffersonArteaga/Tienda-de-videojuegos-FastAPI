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
