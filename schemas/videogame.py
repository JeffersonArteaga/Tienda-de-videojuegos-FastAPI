from pydantic import BaseModel, Field

# Definición de la clase Videogame utilizando Pydantic
class Videogame(BaseModel):
    # Atributos de la clase Videogame con sus tipos y restricciones
    name: str  # Nombre del videojuego (tipo: str)
    overview: str  # Descripción general del videojuego (tipo: str)
    rating: float = Field(..., ge=0, le=5)  # Calificación del videojuego (tipo: float)
    category: str  # Categoría del videojuego (tipo: str)
    price: float = Field(..., gt=0)  # Precio del videojuego (tipo: float)

