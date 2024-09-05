from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    def __init__(self,name):
        self.name = name
    def describe(self):
        print("Name : "+self.name)
        print("Type : "+self.__class__.__name__)

class FullTimeEmployee(Employee):
    salary = 3000
    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, name,hours_worked,hourly_rate):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

full_time_employee = FullTimeEmployee("Arun")
part_time_employee = PartTimeEmployee("Amal",20,100)

print("Full Time Employee")
full_time_employee.describe()
print(f"Salary = {full_time_employee.calculate_salary()}")
print("Part Time Employee")
part_time_employee.describe()
print(f"Salary = {part_time_employee.calculate_salary()}")