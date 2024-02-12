from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

# Variables globales para llevar un registro de las llamadas a GET y POST
get_requests_count = 0
post_requests_count = 0

#se crea una clase con el esquema que se espera encontrar al llamar al método POST
class Date(BaseModel):
    date_with_minutes: bool

@app.post("/date")
async def root(date_class: Date):
    global post_requests_count
    actual_date = datetime.now()    
    post_requests_count += 1
    if date_class.date_with_minutes:
        return {'fecha' : actual_date.strftime("%Y-%m-%d %H:%M:%S")}
    else:
        return {'fecha': actual_date.strftime("%Y-%d-%m")}

@app.get("/count")
async def root():
    global get_requests_count, post_requests_count
    get_requests_count += 1
    return {"conteo": post_requests_count + get_requests_count}