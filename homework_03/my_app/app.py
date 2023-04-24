import uvicorn
from fastapi import FastAPI
from items import router as item_router
from users.views import router as user_router


app = FastAPI()
app.include_router(item_router, prefix="/items")
app.include_router(user_router, prefix="/users")


@app.get("/")
def Index():
    return {
        "message": "Index",
    }


@app.get("/hello")
def hello(name: str = "World"):
    return {
        "message": f"Hello {name}!",
    }


@app.get("/ping")
def pong():
    return {"message": "pong"}


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
