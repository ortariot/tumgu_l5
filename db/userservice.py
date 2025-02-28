
import asyncio

from models import User, Roles
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


class UserService():

    def __init__(self, db_url):
        self.db_url = db_url

    def get_async_session(self) -> AsyncSession:

        engine =  create_async_engine(self.db_url)


        return sessionmaker(
            engine,
            class_ = AsyncSession,
            expire_on_commit=False
        )


    async def get_user(self, id):
        session = self.get_async_session()

        async with session() as db:

            user = await db.execute(select(User).where(User.id==id))
            # return user.one()
            return user.scalars().one()
            


    async def add_user(self, login, password, role):

        session = self.get_async_session()

        user = User(login=login, password=password, role=role)

        async with session() as db:
            db.add(user)
            await db.commit()

            return user
        

    async def update_user(self, id, **kwargs):
        
        session = self.get_async_session()

        async with session() as db:
            user = await db.execute(select(User).where(User.id==id))

            user = user.scalars().one()
            

            print(user)

            for key, value in kwargs.items():
                setattr(user, key, value)

            await db.commit()

            return user
        
    
    async def del_user(self, id):
        session = self.get_async_session()

        async with session() as db:
            user = await db.execute(delete(User).where(User.id==id))

            await db.commit()

            return user



async def runner():
    PG_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"

    role_service = RoleService(PG_URL)

    user_service = UserService(PG_URL)

    # res = await role_service.add_role(name="super", level=6)
    # res = await role_service.get_roles()
    # res = await role_service.get_role(1)

    # res = await user_service.add_user(login="admin", password='user', role=1)

    res = await user_service.get_user(1)

    # res = await user_service.update_user(1, login='user2')
    # res = await user_service.del_user(1)


    print(res.roles.name)



if __name__ == "__main__":

    asyncio.run(runner())
    