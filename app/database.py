# # app/database.py
# import os
# from sqlmodel import SQLModel
# from sqlmodel.ext.asyncio.session import AsyncSession
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

# DATABASE_URL = os.getenv("DATABASE_URL")  # Ensure this uses psycopg

# engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=False)


# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.create_all)

# async def get_session() -> AsyncSession:
#     async_session = AsyncSession(engine)
#     try:
#         yield async_session
#     finally:
#         await async_session.close()
