```markdown
# FastAPI CRUD con MongoDB

Este proyecto es una API creada con FastAPI para gestionar una agenda, permitiendo crear, leer, actualizar y eliminar citas almacenadas en una base de datos MongoDB.

## Descripción

La API permite gestionar citas con los siguientes campos:
- **ID**: Autogenerado por MongoDB
- **Fecha**
- **Título**
- **Descripción**

## Endpoints

### Crear una nueva cita

- **Ruta**: `/crear_cita`
- **Método**: `POST`
- **Descripción**: Crea una nueva cita y la guarda en la base de datos.
- **Entrada**: Modelo `CitaSinId`
- **Salida**: Modelo `Cita`

### Observar todas las citas

- **Ruta**: `/`
- **Método**: `GET`
- **Descripción**: Devuelve una lista de todas las citas guardadas en la base de datos.
- **Salida**: Lista de modelos `Cita`

### Obtener una cita por ID

- **Ruta**: `/cita_por_id/{id_parametro}`
- **Método**: `GET`
- **Descripción**: Devuelve una cita específica según su ID.
- **Entrada**: ID de la cita (string)
- **Salida**: Modelo `Cita`

### Actualizar una cita existente

- **Ruta**: `/actualizar_cita/{id_cita_mod}`
- **Método**: `PUT`
- **Descripción**: Actualiza una cita existente con nuevos datos.
- **Entrada**: ID de la cita a actualizar (string) y un modelo `CitaSinId` con los nuevos datos.
- **Salida**: Modelo `Cita` actualizado

### Eliminar una cita por ID

- **Ruta**: `/eliminar_cita/{id_cita_eliminar}`
- **Método**: `DELETE`
- **Descripción**: Elimina una cita según su ID.
- **Entrada**: ID de la cita (string)
- **Salida**: Mensaje de éxito o error

## Estructura del Proyecto

```plaintext
.
├── main.py
├── db
│   ├── client.py
│   ├── modelos
│   │   └── cita.py
│   └── esquemas
│       └── cita.py
├── requirements.txt
└── README.md
```

### main.py

Contiene la definición de los endpoints y las operaciones CRUD.

### db/client.py

Define la conexión con la base de datos MongoDB.

### db/modelos/cita.py

Define los modelos `CitaSinId` y `Cita` utilizando Pydantic.

### db/esquemas/cita.py

Define la función `cita_esquema` para transformar documentos de MongoDB en diccionarios compatibles con los modelos de Pydantic.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/abelito89/FastAPI_CRUD_MongoDB.git
   cd FastAPI_CRUD_MongoDB
   ```

2. Crea un entorno virtual e instala las dependencias:

   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows usa `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Asegúrate de tener MongoDB corriendo en tu máquina local en el puerto 27017.

4. Corre la aplicación:

   ```bash
   uvicorn main:app --reload
   ```

## Uso

Abre tu navegador y navega a `http://127.0.0.1:8000/docs` para ver la documentación interactiva generada por Swagger.

## Repositorio

El código fuente de este proyecto está disponible en [GitHub](https://github.com/abelito89/FastAPI_CRUD_MongoDB.git).
```
