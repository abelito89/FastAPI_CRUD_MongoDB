def cita_esquema(nueva_cita) -> dict:
    return {"id": str(nueva_cita["_id"]), "Fecha": nueva_cita["Fecha"], "Titulo": nueva_cita["Titulo"], "Descripcion": nueva_cita["Descripcion"]}