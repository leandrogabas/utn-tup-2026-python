from typing import Optional
from fastapi import APIRouter, HTTPException, status
from models.users import (
    User,
    UserUpdate,
    UserPatch,
    GetUsersResponse,
    CreateUserResponse,
    UpdateUserResponse,
    DeleteUserResponse,
)

router = APIRouter(tags=["Users"])

usuarios: list[User] = [
    User(id=1, name="juan perez", is_active=True),
    User(id=2, name="pepe sanchez", is_active=False),
]


@router.get("/user")
def get_users(is_active: Optional[bool] = None) -> GetUsersResponse:
    if is_active is None:
        return GetUsersResponse(users=usuarios)
    filtered = [u for u in usuarios if u.is_active == is_active]
    return GetUsersResponse(users=filtered)


@router.get("/user/{id}")
def get_user_by_id(id: int) -> User:
    for user in usuarios:
        if user.id == id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado",
    )


@router.post("/user", status_code=status.HTTP_201_CREATED)
def create_user(user: User) -> CreateUserResponse:
    if any(u.id == user.id for u in usuarios):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El ID del usuario ya existe",
        )
    usuarios.append(user)
    return CreateUserResponse(message="usuario creado")


@router.put("/user/{id}")
def update_user(id: int, payload: UserUpdate) -> UpdateUserResponse:
    for idx, user in enumerate(usuarios):
        if user.id == id:
            updated_user = User(
                id=id,
                name=payload.name,
                is_active=payload.is_active,
            )
            usuarios[idx] = updated_user
            return UpdateUserResponse(
                message="usuario actualizado",
                user=updated_user,
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado",
    )


@router.patch("/user/{id}")
def patch_user(id: int, payload: UserPatch) -> UpdateUserResponse:
    for idx, user in enumerate(usuarios):
        if user.id == id:
            update_data = payload.model_dump(exclude_unset=True)
            updated_user = user.model_copy(update=update_data)
            usuarios[idx] = updated_user
            return UpdateUserResponse(
                message="usuario modificado parcialmente",
                user=updated_user,
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado",
    )


@router.delete("/user/{id}")
def delete_user(id: int) -> DeleteUserResponse:
    for user in usuarios:
        if user.id == id:
            usuarios.remove(user)
            return DeleteUserResponse(message="usuario borrado")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado",
    )
