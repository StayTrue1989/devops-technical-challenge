import os
from fastapi import FastAPI
from typing import Union
from mangum import Mangum

# Lines 7-10 change the path that is used to serve openapi.json, which will allow the documentation page to be generated without any issue.
stage = os.environ.get("STAGE", None)
openapi_prefix = f"/{stage}" if stage else "/"

app = FastAPI(openapi_prefix=openapi_prefix)  # Here is the magic

# Create FastAPI "app" object
app = FastAPI()

# Define the path operation function. Takes two arguments of type int or float.
@app.get("/sum/{value1}/{value2}")
def sum_values(value1: Union[int, float], value2: Union[int, float]):
    total_sum = value1 + value2
    return {"sum": total_sum}


handler = Mangum(app)
