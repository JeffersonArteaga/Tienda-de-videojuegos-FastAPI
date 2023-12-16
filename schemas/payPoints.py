from pydantic import BaseModel, Field

# Definición de la clase PayPoints utilizando Pydantic
class PayPoints(BaseModel):
    # Atributo de la clase PayPoints con restricciones
    mount: float = Field(..., gt=0)