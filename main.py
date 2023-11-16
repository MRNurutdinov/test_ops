from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter

from api.handlers import user_router

app = FastAPI(title="Test Xops")

main_api_router = APIRouter()

# подключаем роутеры
main_api_router.include_router(user_router)
app.include_router(main_api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
