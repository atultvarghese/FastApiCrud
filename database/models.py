from datetime import datetime

from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    description: str
    completed: bool
    deleted: bool
    updated: int = int(datetime.timestamp(datetime.now()))
    created: int = int(datetime.timestamp(datetime.now()))


