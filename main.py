import datetime
from sys import path
from fastapi import FastAPI, Request, Form, BackgroundTasks
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import icalendar
import os
import uuid

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse, status_code=200)
def read_item(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

def loesche_file(file:str):
    if os.path.exists(file):
        os.remove(file)

@app.post("/createTermin", status_code=200)
def create_file(
    background_tasks: BackgroundTasks,
    startTermin: datetime.datetime = Form(...),
    endeTermin: datetime.datetime = Form(...),
    betreffTermin: str = Form(...),
):

    #Kalender erstellen
    cal = icalendar.Calendar()
    cal.add('version','2.0')

    #Event erstellen
    event = icalendar.Event()
    event.add('summary',betreffTermin)
    event.add('dtstart',startTermin)
    event.add('dtend',endeTermin)
    event.add('dtstamp',datetime.datetime.now())

    cal.add_component(event)

    file_name = f"tmp/{uuid.uuid4()}.ics"
    with open(file_name,'wb') as f:
        f.write(cal.to_ical())
    
    #filename erstellen
    background_tasks.add_task(loesche_file, file_name)

    return FileResponse(file_name)

if __name__ == '__main__':
    uvicorn.run('main:app',port=8000,host='0.0.0.0')
