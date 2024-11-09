from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Dummy data for employees
employees = {}

class Employee(BaseModel):
    name: str
    position: str
    department: str

#@app.post("/employees/")
#def create_employee(employee_id: int, employee: Employee):
 #   employees[employee_id] = employee
  #  return {"employee_id": employee_id, "employee": employee}

#@app.get("/employees/{employee_id}")
#def get_employee(employee_id: int):
 #   if employee_id in employees:
  #      return employees[employee_id]
   # return {"error": "Employee not found"}
# Create employee (use employee_id in the URL)
@app.post("/employees/{employee_id}")
def create_employee(employee_id: int, employee: Employee):
    employees[employee_id] = employee
    return {"employee_id": employee_id, "employee": employee}

# Get employee by ID
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    if employee_id in employees:
        return employees[employee_id]
    return {"error": "Employee not found"}

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: Employee):
    if employee_id in employees:
        employees[employee_id] = employee
        return {"employee_id": employee_id, "employee": employee}
    return {"error": "Employee not found"}

