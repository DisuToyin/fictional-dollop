
from re import T
import uvicorn

from fastapi import FastAPI
from starlette.requests import Request

# Create the application
app = FastAPI()






@app.get("/grade")
async def get_() -> dict:
    return {
        "slackUsername": "AICO",
        "backend": True,
        "age": 55,  
        "bio": "readiness"
    }




if __name__ == "__main__":
    uvicorn.run("main:app", port=7001, reload=True)
