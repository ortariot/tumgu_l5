
import asyncio

from db.models.models import Roles
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

PG_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"

class RoleService():

    def __init__(self, db_url):
        self.db_url = db_url


    def get_async_session(self) -> AsyncSession:

        engine =  create_async_engine(self.db_url)


        return sessionmaker(
            engine,
            class_ = AsyncSession,
            expire_on_commit=False
        )


    async def add_role(self, name, level):

        session = self.get_async_session()

        role = Roles(name=name, level=level)

        async with session() as db:
            db.add(role)
            await db.commit()

            return role



    async def get_roles(self):

        session = self.get_async_session()

        async with session() as db:

            roles = await db.execute(select(Roles))
            return roles.scalars().all()


    async def get_role(self, id):

        session = self.get_async_session()

        async with session() as db:

            roles = await db.execute(select(Roles).where(Roles.id==id))
            return roles.scalars().one()



role_service = RoleService(PG_URL)



if __name__ == "__main__":
    role_service = RoleService(PG_URL)

    res = role_service.get_roles()

    print(res)
