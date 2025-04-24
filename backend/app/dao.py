
from app.model import Passwords
from sqlalchemy import insert, select

from app.database import Base, async_session_maker


class BaseDao:
    model = None

    @classmethod
    async def add_by_csv(cls, rows):
        async with async_session_maker() as session:
            for row in rows:
                # Преобразование данных согласно типам столбцов
                processed_row = {
                    "id": int(row["id"]),
                    "password": str(row["password"]),
                    "hashed_password": str(row["hashed_password"]),
                }
                query = insert(Base.metadata.tables["passwords"]).values(**processed_row)
                await session.execute(query)
            await session.commit()

    @classmethod
    async def get_password(cls, input_hashed_password: str):
        async with async_session_maker() as session:
            query = (select(Passwords.password).
                     select_from(Passwords)
                     .where(Passwords.hashed_password == input_hashed_password))

            result = await session.execute(query)
            return result.mappings().all()
