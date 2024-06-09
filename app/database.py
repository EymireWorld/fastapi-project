from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from app.settings import DB_HOST, DB_PORT, DB_NAME, DB_PASSWORD, DB_USERNAME


engine = create_async_engine(
    f'postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)
SessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


async def get_session():
    session = SessionLocal()

    try:
        yield session
    finally:
        await session.close()
