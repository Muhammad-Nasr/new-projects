
from fastapi import FastAPI, Path, Depends
from typing import Optional, List
from models import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@app.post('/token')
def token(request: OAuth2PasswordRequestForm = Depends()):
    return {'aceess_token': request.username}

@app.get('/')
def get_token(token: str = Depends(oauth2_scheme)):
    return {'token': token}


class Item(BaseModel):
    name: str
    id: int


@app.get('/item')
def get(name: Optional[str] = None):
    return "inventory name {name}"


@app.get('/{id}')
def home(id: int = Path(None, description='the id of item', gt=0, lt=2)):
    return f"hello world {id} time"


@app.post('/')
def add(id:int, item: Item):
    data = {}
    data[id] = item
    return data
