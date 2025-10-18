from pydantic import BaseModel, Field
from typing import Optional

class EmployeeBase(BaseModel):
    name: str
    age: int
    department: str

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: str = Field(alias="_id")

    class Config:
        populate_by_name = True
