from pydantic import BaseModel, Field

class CitaSinId(BaseModel):
    Fecha: str
    Titulo: str
    Descripcion: str


class Cita(BaseModel):
    id: str
    Fecha: str
    Titulo: str
    Descripcion: str