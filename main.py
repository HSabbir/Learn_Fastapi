import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/')
def index():
    return {
        'data': {'name':'Sadek'}
    }

@api.get('/about')
def about():
    return {
        'data':'about'
    }

