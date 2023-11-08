from datetime import datetime


class Employee:

    def __init__(self, name, dob, base_salary):
        self.name = name
        self.dob = datetime.strptime(dob, '%d.%m.%Y').date()
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"


class Accountant:
    employees: dict[int: Employee]

    def __init__(self, employees: dict[int: Employee] = None):
        self.employees = employees or {}

    def add_employee(self, employee: Employee):
        if not isinstance(employee, Employee):
            raise ValueError("Неверный тип объекта. Необходимо ввести объект типа Employee")
        employee_id = len(self.employees) + 1
        self.employees[employee_id] = employee

    def calculate_net_salary(self, employee_id: int):
        if employee_id not in self.employees:
            raise ValueError(f"Сотрудник с ID {employee_id} не найден.")
        tax_rate = 0.25
        return int(self.employees[employee_id].base_salary * (1 - tax_rate))


employee = Employee("Rob", "13.12.2001", 40_000)
accountant = Accountant()
accountant.add_employee(employee)
print(accountant.calculate_net_salary(1))
