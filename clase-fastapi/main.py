from fastapi import FastAPI
from routers import users, products

app = FastAPI(
    title="TP1 - ABM Usuarios y Productos",
    version="1.0.0",
)

app.include_router(users.router)
app.include_router(products.router)


@app.get("/")
def read_root():
    mensaje = "Primer clase de FastAPI"
    return {"message": mensaje}
