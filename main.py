from asyncio import all_tasks

from fastapi import FastAPI, APIRouter

from config import collection
from database.models import Todo
from database.schemas import all_todos

app = FastAPI()
router = APIRouter()

@router.get("/")
async def homepage():
    data = collection.find( )
    print(data)
    return all_todos(data)

@router.post("/")
async def create_task(task: Todo):
    collection.insert_one(dict(task))
app.include_router(router)