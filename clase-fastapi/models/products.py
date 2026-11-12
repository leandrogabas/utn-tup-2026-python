from typing import List, Optional
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int = Field(..., gt=0)
    nombre: str = Field(..., min_length=1)
    categoria: str = Field(..., min_length=1)
    precio: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)


class ProductUpdate(BaseModel):
    nombre: str = Field(..., min_length=1)
    categoria: str = Field(..., min_length=1)
    precio: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)


class ProductPatch(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1)
    categoria: Optional[str] = Field(None, min_length=1)
    precio: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)


class GetProductsResponse(BaseModel):
    products: List[Product]


class CreateProductResponse(BaseModel):
    message: str


class UpdateProductResponse(BaseModel):
    message: str
    product: Product


class DeleteProductResponse(BaseModel):
    message: str
