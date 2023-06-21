import asyncio
import aiohttp
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from models import Session, Base, async_engine, User, Post, Session


async def create_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(session: Session, users: list[dict]):
    for user_data in users:
        user = User(
            id=int(user_data["id"]),
            name=user_data["name"],
            username=user_data["username"],
            email=user_data["email"]
        )
        session.add(user)
    await session.commit()


async def create_posts(session: Session, posts: list[dict]):
    for post_data in posts:
        post = Post(
            user_id=int(post_data["userId"]),
            title=post_data["title"],
            body=post_data["body"],
        )
        session.add(post)
    await session.commit()

async def async_main():
    async with Session() as session:
        async with async_engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
        async with async_engine.begin() as connection:
            users: list[dict]
            posts: list[dict]
            users, posts = await asyncio.gather(
                fetch_users_data(), fetch_posts_data()
            )
            await create_user(session=session, users=users)
            await create_posts(session=session, posts=posts)
            await session.commit()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
