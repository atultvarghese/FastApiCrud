from fastapi import FastAPI, HTTPException
import crud
from schema import EmployeeCreate, Employee

app = FastAPI(title="Employee CRUD API")

@app.post("/employees", response_model=Employee)
async def create_employee(employee: EmployeeCreate):
    new_emp = await crud.create_employee(employee)
    return new_emp

@app.get("/employees", response_model=list[Employee])
async def list_employees():
    return await crud.get_all_employees()

@app.get("/employees/{emp_id}", response_model=Employee)
async def get_employee(emp_id: str):
    emp = await crud.get_employee(emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@app.put("/employees/{emp_id}", response_model=Employee)
async def update_employee(emp_id: str, employee: EmployeeCreate):
    updated = await crud.update_employee(emp_id, employee.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated

@app.delete("/employees/{emp_id}")
async def delete_employee(emp_id: str):
    deleted = await crud.delete_employee(emp_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"status": "deleted"}
