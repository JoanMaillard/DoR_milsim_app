from typing import Union
import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
script_dir = os.path.dirname(__file__)
static_filepath = os.path.join(script_dir, "static/")
print(static_filepath)
app.mount("/", StaticFiles(directory=static_filepath, html=True), name="static")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}