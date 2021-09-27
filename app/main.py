import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
TEMPLATE_DIR = BASE_DIR / "templates"

app =  FastAPI()
templates = Jinja2Templates(directory=TEMPLATE_DIR)

@app.get('/', response_class=HTMLResponse) #http GET
def home_view(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home.html", context)

@app.post('/') #http POST
def home_detail_view():
    return {"hello": "world"}