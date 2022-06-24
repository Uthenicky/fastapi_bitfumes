from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {
        'msg': 'tesss',
        'data': {
            'page': 'Home',
        }
    }


@app.get('/about')
def about():
    return {
        'msg': 'tesss',
        'data': {
            'page': 'about',
        }
    }
