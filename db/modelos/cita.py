from pydantic import BaseModel, Field
import uuid #para generar id automáticos

class CitaSinId(BaseModel):
    Fecha: str
    Titulo: str
    Descripcion: str


class Cita(BaseModel):
    id: str
    Fecha: str
    Titulo: str
    Descripcion: str