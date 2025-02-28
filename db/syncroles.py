from sqlalchemy import select, delete, create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Roles, Base


class SyncRoleService():

    def __init__(self, db_url):
        self.db_url = db_url


    def get_session(self):

        engine =  create_engine(self.db_url)

        return sessionmaker(bind=engine, autoflush=False, autocommit=False)


    def create_db(self):
        engine = create_engine(self.db_url)
        Base.metadata.create_all(bind=engine)



    def add_role(self, name, level):

        session = self.get_session()

        role = Roles(name=name, level=level)

        with session() as db:
            db.add(role)
            db.commit()
            db.refresh(role)

            return role


    def get_roles(self):

        session = self.get_session()

        with session() as db:

            roles = db.execute(select(Roles))
            return roles.scalars().all()



if __name__ == "__main__":
    PG_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

    SQL_LITE = "sqlite:///./test.db"

    # role_service = SyncRoleService(PG_URL)
    role_service = SyncRoleService(SQL_LITE)

    # role_service.create_db()

    res = role_service.get_roles()

    # res = role_service.add_role("user", 1)

    print(res)