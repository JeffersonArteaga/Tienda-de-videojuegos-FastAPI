from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token

class JWTBearerAdmin(HTTPBearer):
    async def __call__(self, request: Request):
        # Llama al método __call__ de la clase base (HTTPBearer) para realizar la autenticación básica.
        auth = await super().__call__(request)
        
        # Valida el token JWT utilizando la función validate_token del módulo utils.jwt_manager.
        data = validate_token(auth.credentials)
        
        # Comprueba si el rol del usuario en los datos decodificados es 'Admin'.
        if data['role'] != 'Admin':
            # Si el usuario no tiene el rol de 'Admin', lanza una excepción HTTPException con un código 401 (No autorizado).
            raise HTTPException(status_code=401, detail="Invalid user")