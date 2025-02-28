import uvicorn
from fastapi import FastAPI

from api.v1.role import role_router

app = FastAPI(title="my_api")

app.include_router(role_router, prefix="/api/v1/roles")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
    
