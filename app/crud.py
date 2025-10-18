from db import get_database
from schema import EmployeeCreate
from bson import ObjectId

db = get_database()
collection = db["employees"]

# helper function
def employee_helper(emp):
    if not emp:
        return None
    emp["_id"] = str(emp["_id"])
    return emp

async def create_employee(employee: EmployeeCreate):
    emp = employee.dict()
    result = await collection.insert_one(emp)
    new_emp = await collection.find_one({"_id": result.inserted_id})
    return employee_helper(new_emp)

async def get_all_employees():
    employees = await collection.find().to_list(100)
    return [employee_helper(emp) for emp in employees]

async def get_employee(emp_id: str):
    emp = await collection.find_one({"_id": ObjectId(emp_id)})
    return employee_helper(emp)

async def update_employee(emp_id: str, data: dict):
    await collection.update_one({"_id": ObjectId(emp_id)}, {"$set": data})
    updated = await collection.find_one({"_id": ObjectId(emp_id)})
    return employee_helper(updated)

async def delete_employee(emp_id: str):
    result = await collection.delete_one({"_id": ObjectId(emp_id)})
    return result.deleted_count > 0
