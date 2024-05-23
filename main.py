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
# from pydantic import BaseModel, Field
from typing import List, Dict
from db.modelos.cita import Cita, CitaSinId
import uuid #para generar id automáticos
from db.client import db_client
from db.esquemas.cita import cita_esquema
from bson import ObjectId #para poder convertir los strings id a ObjectId, que son los tipos que tienen los id generados por mongodb

app = FastAPI()

@app.post('/crear_cita', response_model=Cita) # crea nueva cita y la agrega a la lista
async def crear_cita(nueva_cita:CitaSinId) -> Cita:
    #cita_con_id = Cita(**nueva_cita.dict())
    cita_dict = dict(nueva_cita) # convierto la cita en un diccionario para pasarselo como documento a mongodb, que solo entiende JSON
    id = db_client.local.citas.insert_one(cita_dict).inserted_id #en esta línea estoy insertando la cita en la base de datos y a la vez quedándome con el id
    nueva_cita = cita_esquema(db_client.local.citas.find_one({"_id": id})) #esto es un JSON que viene de la bd y hay q transformalo a objeto Cita con función importada desde el módulo esquemas
    return Cita(**nueva_cita)

@app.get('/', response_model= List[Cita])
async def observar_total_citas() -> List[Cita]:
    lista_de_citas = []
    for doc in db_client.local.citas.find():
        lista_de_citas.append(cita_esquema(doc))
    #return lista_de_citas
    return lista_de_citas

@app.get('/cita_por_id/{id_parametro}', response_model=Cita)
async def devolver_cita_segun_id(id_parametro:str) -> Cita:
    id_cita = ObjectId(id_parametro)
    cita_encontrada = Cita(**cita_esquema(db_client.local.citas.find_one({"_id": id_cita})))
    
    if cita_encontrada:
        return cita_encontrada 
    raise HTTPException(status_code=404, detail="No se ha encontrado ninguna cita con el ID proporcionado")

@app.put('/actualizar_cita/{id_cita_mod}', response_model=Cita)
async def actualizar_cita(id_cita_mod:str, nueva_cita:CitaSinId) -> Cita:
    id_cita_modificar = ObjectId(id_cita_mod)
    nueva_cita_dict = dict(nueva_cita)
    documento_modificado = cita_esquema(db_client.local.citas.find_one_and_replace({"_id": id_cita_modificar}, nueva_cita_dict,return_document=True))
    cita_modificada = Cita(**documento_modificado)
    if cita_modificada:             
            return cita_modificada
    raise HTTPException(status_code=404, detail="No se encontró ninguna cita con el ID proporcionado")
    
@app.delete('/eliminar_cita/{id_cita_eliminar}', response_model=Dict)
async def eliminar_cita(id_cita_eliminar:str) -> Dict:
    print("Tipo de dato de id_cita_eliminar:",type(id_cita_eliminar))
    id_eliminar = ObjectId(id_cita_eliminar)
    print("Tipo de dato de id_eliminar:",type(id_eliminar))
    cita_eliminada = db_client.local.citas.find_one_and_delete({"_id": id_eliminar})
    if cita_eliminada:
        return {"mensaje":"Cita eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="No se encontró ninguna cita con el ID proporcionado")