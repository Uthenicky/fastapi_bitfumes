from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# query params


@app.get('/')
def Index(limit, jenis: bool):
    if jenis:
        return {
            'msg': f'data dilimit sebanyak = {limit}',
        }
    else:
        return {
            'msg': 'params salah',
        }


# path
@app.get('/blog/{id}')
def Show(id: int):
    return {
        'data': id,
    }


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog/create_blog/')
def CreateBlog(request: Blog):
    return request
