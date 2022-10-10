from fastapi import BackgroundTasks, FastAPI, Query
import uvicorn
import sys
sys.path.append('../')
import app.vertaler as vertaler


### How to run from cli -> uvicorn api:app --reload

app = FastAPI()

def run_me():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/nederlands/")
async def translate(message: str = Query(default=None, max_length=50)):
    straat_taal = vertaler.main(message)
    return {"vertaling": straat_taal}

