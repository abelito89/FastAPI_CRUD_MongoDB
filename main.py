"""
     API para Gestionar una Agenda:

Crea un modelo Pydantic para representar una cita con los siguientes campos:
ID (autogenerado)
Fecha
Hora
Título
Descripción
Define un endpoint para crear nuevas citas usando el modelo de Pydantic como entrada.
Crea un endpoint para recuperar una cita por su ID.
Crea un endpoint para actualizar una cita existente.
Crea un endpoint para eliminar una cita por su ID.
    """
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict
import uuid #para generar id automáticos

app = FastAPI()

class CitaSinId(BaseModel):
    Fecha: str
    Titulo: str
    Descripcion: str


class Cita(BaseModel):
    ID: uuid.UUID = Field(default_factory=uuid.uuid4, alias="id")# Utilizamos `Field` con `default_factory` para que el ID se autogenere automáticamente.
    Fecha: str
    Titulo: str
    Descripcion: str

lista_de_citas = []

@app.post('/crear_cita', response_model=Cita) # crea nueva cita y la agrega a la lista
async def crear_cita(nueva_cita:CitaSinId) -> Cita:
    cita_con_id = Cita(**nueva_cita.dict())
    lista_de_citas.append(cita_con_id)
    return cita_con_id

@app.get('/', response_model= dict)
async def observar_lista() -> dict:
    return {"lista": lista_de_citas}

@app.get('/cita_por_id/{id_cita}', response_model=Cita)
async def devolver_cita_segun_id(id_cita:uuid.UUID) -> Cita:
    for cita in lista_de_citas:
        if cita.ID == id_cita:
            return cita
    raise HTTPException(status_code=404, detail="No se ha encontrado ninguna cita con el ID proporcionado")

@app.put('/actualizar_cita/{id_cita_modificar}', response_model=Cita)
async def actualizar_cita(id_cita_modificar:uuid.UUID, nueva_cita:CitaSinId) -> Cita:
    for i,cita in enumerate(lista_de_citas):
        if cita.ID == id_cita_modificar:
            cita_modificada = Cita(id = id_cita_modificar, **nueva_cita.dict())
            lista_de_citas[i] = cita_modificada          
            return cita_modificada
    raise HTTPException(status_code=404, detail="No se encontró ninguna cita con el ID proporcionado")
    
@app.delete('/eliminar_cita/{id_cita_eliminar}')
async def eliminar_cita(id_cita_eliminar:uuid.UUID) -> Dict:
    for i,cita in enumerate(lista_de_citas):
        if cita.ID == id_cita_eliminar:
            del lista_de_citas[i]
            return {"mensaje":"Cita eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="No se encontró ninguna cita con el ID proporcionado")