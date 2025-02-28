from http import HTTPStatus

from fastapi import APIRouter

from db.models.models import Roles
from db.roleservice import role_service

from schemes.scheme import Role, ResponseRole

role_router = APIRouter()


@role_router.post("/create_role/", status_code=HTTPStatus.ACCEPTED)
async def create_role(input: Role):
    role = await role_service.add_role(input.name, input.level)

    return role



@role_router.get(
    "/get_role/{id}",
    status_code=HTTPStatus.OK,
    response_model=ResponseRole
)
async def get_role(id: int):
    return await role_service.get_role(id)


@role_router.get("/get_roles/", status_code=HTTPStatus.OK)
async def get_roles():
    return await role_service.get_roles()