from jwt import encode, decode

# Clave secreta para firmar y verificar los tokens
pwd = '1234567890'

# Función para crear un token
def create_token(data, secret=pwd):
    """
    Crea un token JWT a partir de los datos proporcionados.

    :param data: Datos a incluir en el token.
    :param secret: Clave secreta para firmar el token (por defecto es '1234567890').
    :return: Token JWT.
    """
    return encode(payload=data, key=secret, algorithm='HS256')

# Función para validar un token
def validate_token(token):
    """
    Valida un token JWT.

    :param token: Token JWT a validar.
    :return: Datos decodificados del token si es válido.
    """
    return decode(token, pwd, algorithms=['HS256'])
