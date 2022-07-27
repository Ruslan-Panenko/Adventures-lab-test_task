from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel

from parser import parce

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    user_name: str
    password: str


@app.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})


@app.get("/api/v1/posts")
async def get_posts():
    data = parce()
    return data


@app.post('/main', response_class=RedirectResponse)
async def main(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == 'admin' and password == 'password':
        return templates.TemplateResponse('main.html', {'request': request
                                                        })
