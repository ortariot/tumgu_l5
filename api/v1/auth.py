from datetime import datetime, timedelta, UTC
from http import HTTPStatus

from fastapi import APIRouter, Response, HTTPException

from schemes.scheme import AuthUser
from services.tokenservice import create_token

auth_router = APIRouter()


@auth_router.post("/auth/", status_code=HTTPStatus.ACCEPTED)
async def auth_user(input: AuthUser, resp: Response):

    # проверить существование юзера
    # user = await user_service.get(input.login)
    # if not user:
    #     raise HTTPException(
    #                      status_code = HTTPStatus.BadRequest,
    #                      detail ="неверный логин или пароль"
    # )

    #  проверка пароля
    # если пароль неверный то вернём HTTPException

    exp_time  = datetime.now(UTC) + timedelta(minutes=30)

    my_data ={
        "login": "maxim",
        "role": "admin",
        "exp": exp_time,
        "type": "access"
    }

    my_token = create_token(my_data)

    resp.set_cookie(key="access_token", value=my_token)

    return {"status": "ok"}
