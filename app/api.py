from fastapi import BackgroundTasks, FastAPI, Query
import vertaler

### How to run from cli -> uvicorn api:app --reload

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/nederlands/")
async def translate(message: str = Query(default=None, max_length=50)):
    straat_taal = vertaler.main(message)
    return {"vertaling": straat_taal}

