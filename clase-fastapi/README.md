# TP1 - API REST con FastAPI: ABM de Usuarios y Productos

Proyecto correspondiente al **Trabajo Práctico 1** de la materia **Programación IV (UTN - TUP)**. Implementa una API RESTful en memoria utilizando **FastAPI** y **Pydantic v2**, abarcando el CRUD completo de las entidades `User` y `Product`.

## Estructura del Proyecto

```text
clase-fastapi/
├── main.py                # Punto de entrada de la aplicación FastAPI
├── models/
│   ├── users.py           # Esquemas Pydantic para Usuarios
│   └── products.py        # Esquemas Pydantic para Productos
├── routers/
│   ├── users.py           # Endpoints CRUD y filtrado de Usuarios
│   └── products.py        # Endpoints CRUD y filtrado de Productos
├── requirements.txt       # Dependencias del proyecto
├── setup.cfg              # Configuración de pycodestyle (PEP 8)
└── pyrightconfig.json     # Configuración de chequeo estático de tipos
```

## Instrucciones de Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/leandrogabas/utn-tup-2026-python.git
cd utn-tup-2026-python/clase-fastapi
```

### 2. Crear y activar el entorno virtual

```bash
# Creación del entorno virtual
python -m venv .venv

# Activación en Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Activación en Windows (CMD)
.venv\Scripts\activate.bat

# Activación en Linux / macOS
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Levantar el servidor de desarrollo

```bash
fastapi dev main.py
```

*(Alternativamente con Uvicorn: `uvicorn main:app --reload`)*

---

## Acceso a la Documentación Interactiva (Swagger UI)

Con el servidor en ejecución, la API estará disponible en `http://127.0.0.1:8000`:

- **Swagger UI (Interactivo):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc (Documentación alternativa):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Desde `/docs` se pueden ejecutar y probar directamente todos los endpoints (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) mediante el botón **"Try it out"**.

## Resumen de Endpoints

### Usuarios (`/user`)
| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| `GET` | `/user` | Lista todos los usuarios. Permite filtrar por query param `?is_active=true` o `?is_active=false`. |
| `GET` | `/user/{id}` | Obtiene un usuario específico por su `id`. |
| `POST` | `/user` | Crea un nuevo usuario validando unicidad de `id`. |
| `PUT` | `/user/{id}` | Reemplaza íntegramente los datos de un usuario existente. |
| `PATCH` | `/user/{id}` | Modifica parcialmente los campos enviados de un usuario. |
| `DELETE` | `/user/{id}` | Elimina un usuario por su `id`. |

### Productos (`/product`)
Entidad compuesta por 5 campos: `id` (`int`), `nombre` (`str`), `categoria` (`str`), `precio` (`float`), `stock` (`int`).

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| `GET` | `/product` | Lista todos los productos. Permite filtrar por query param `?categoria=...`. |
| `GET` | `/product/{id}` | Obtiene un producto específico por su `id`. |
| `POST` | `/product` | Crea un nuevo producto validando tipos, restricciones numéricas y unicidad de `id`. |
| `PUT` | `/product/{id}` | Reemplaza todos los atributos del producto especificado. |
| `PATCH` | `/product/{id}` | Actualiza parcialmente los atributos del producto. |
| `DELETE` | `/product/{id}` | Elimina un producto por su `id`. |
