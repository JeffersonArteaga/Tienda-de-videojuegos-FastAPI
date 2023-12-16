from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        # Llama al método __call__ de la clase base (HTTPBearer) para realizar la autenticación básica.
        auth = await super().__call__(request)
        
        # Valida el token JWT utilizando la función validate_token del módulo utils.jwt_manager.
        data = validate_token(auth.credentials)
        
        # Si la validación del token no es exitosa (data es None), lanza una excepción HTTPException con un código 401 (No autorizado).
        if data is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        else:
            # Si la validación del token es exitosa, devuelve los datos decodificados del token.
            return data

        