from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"hello": "world"}


# PATH PARAMS
# You can declare multiple path and query params, order doesn't matter
# FastAPI identifies by name
@app.get("/files/{folder_path:path}")
def get_files(folder_path: str):
    return {"folder": folder_path}


@app.get("/items/{item_id}")
def get_item(item_id: str):
    return {"item": item_id}


# QUERY PARAMS
# When you declare other function params that are not part of path params,
# they are interpreted as quey params.

# Query params can be optional or non optional or can have default values


@app.get("/children/{parent_id}")
def get_children(parent_id: int, mother_id: int, adopted: bool = True, unborn: Union[bool, None] = None):
    return {"parent_id": parent_id,
            "mother_id": mother_id,
            "adopted": adopted,
            "unborn": unborn}
