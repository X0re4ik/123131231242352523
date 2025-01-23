import uvicorn
from fastapi import FastAPI

from fastapi import status

from src.gigachat.auth import GigaChatAuth
from src.gigachat.driver import GigaChatDriver

from pydantic import BaseModel


class GigaChatMassage(BaseModel):
    message: str

GIGA_CHAT_TOKEN = "YWUxMzc0OTMtNGU0Mi00NTJjLWJlNGUtYjE4MTAyYTJkOTVkOjNlY2FiMzFmLWI2ZjEtNDdlNy04ZTZlLTNlODZmOTVhN2ZjNQ=="

app = FastAPI(
    docs_url="/api/v1/gigachat/doc",
    openapi_url="/api/v1/gigachat/openapi.json",
    redoc_url=None
)


@app.post("/api/v1/gigachat/")
async def root(giga_chat_message: GigaChatMassage):
    access_token = GigaChatAuth(GIGA_CHAT_TOKEN).get_access_token()

    answer = GigaChatDriver(access_token).get_answer(giga_chat_message.message)

    if answer is not None:
        return {"answer": answer, "status_code": status.HTTP_200_OK}
    return {"answer": answer, "status_code": status.HTTP_400_BAD_REQUEST}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
