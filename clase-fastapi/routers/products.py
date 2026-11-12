from typing import Optional
from fastapi import APIRouter, HTTPException, status
from models.products import (
    Product,
    ProductUpdate,
    ProductPatch,
    GetProductsResponse,
    CreateProductResponse,
    UpdateProductResponse,
    DeleteProductResponse,
)

router = APIRouter(tags=["Products"])

productos: list[Product] = [
    Product(
        id=1,
        nombre="Teclado Mecanico",
        categoria="Perifericos",
        precio=85000.50,
        stock=15,
    ),
    Product(
        id=2,
        nombre="Monitor 24 Pulgadas",
        categoria="Monitores",
        precio=210000.00,
        stock=8,
    ),
]


@router.get("/product")
def get_products(categoria: Optional[str] = None) -> GetProductsResponse:
    if categoria is None:
        return GetProductsResponse(products=productos)
    filtered = [
        p for p in productos if p.categoria.lower() == categoria.lower()
    ]
    return GetProductsResponse(products=filtered)


@router.get("/product/{id}")
def get_product_by_id(id: int) -> Product:
    for product in productos:
        if product.id == id:
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Producto no encontrado",
    )


@router.post("/product", status_code=status.HTTP_201_CREATED)
def create_product(product: Product) -> CreateProductResponse:
    if any(p.id == product.id for p in productos):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El ID del producto ya existe",
        )
    productos.append(product)
    return CreateProductResponse(message="producto creado")


@router.put("/product/{id}")
def update_product(id: int, payload: ProductUpdate) -> UpdateProductResponse:
    for idx, product in enumerate(productos):
        if product.id == id:
            updated_product = Product(
                id=id,
                nombre=payload.nombre,
                categoria=payload.categoria,
                precio=payload.precio,
                stock=payload.stock,
            )
            productos[idx] = updated_product
            return UpdateProductResponse(
                message="producto actualizado",
                product=updated_product,
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Producto no encontrado",
    )


@router.patch("/product/{id}")
def patch_product(id: int, payload: ProductPatch) -> UpdateProductResponse:
    for idx, product in enumerate(productos):
        if product.id == id:
            update_data = payload.model_dump(exclude_unset=True)
            updated_product = product.model_copy(update=update_data)
            productos[idx] = updated_product
            return UpdateProductResponse(
                message="producto modificado parcialmente",
                product=updated_product,
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Producto no encontrado",
    )


@router.delete("/product/{id}")
def delete_product(id: int) -> DeleteProductResponse:
    for product in productos:
        if product.id == id:
            productos.remove(product)
            return DeleteProductResponse(message="producto borrado")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Producto no encontrado",
    )
