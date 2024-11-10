from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ManagerEmployee(BaseModel):
    employee_id: int
    name: str
    department: str

manager_employees = {}

@app.post("/manager/update_employee")
def update_employee(employee: ManagerEmployee):
    manager_employees[employee.employee_id] = employee
    return {"message": "Employee data updated in Manager"}

#@app.get("/manager/employees/{employee_id}")
#def get_managed_employee(employee_id: int):
 #   if employee_id in manager_employees:
  #      return manager_employees[employee_id]
   # raise HTTPException(status_code=404, detail="Managed employee not found")
@app.get("/employee-details/{employee_id}")
def get_employee_details(employee_id: int):
    # Assuming you are calling the employee service via HTTP
    response = requests.get(f"http://192.168.49.2:31011/employees/{employee_id}")
    if response.status_code == 200:
        employee_data = response.json()
        return {"employee_id": employee_id, "details": employee_data}
    return {"error": "Employee not found"}

