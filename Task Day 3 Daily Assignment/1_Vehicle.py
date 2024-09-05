from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def get_fuel_efficiency(self):
        pass
    @classmethod
    def from_name(cls,vehicle_name : str):
        if vehicle_name.lower() == "car":
            return Car()
        elif vehicle_name.lower() == "truck":
            return Truck()
        else:
            raise ValueError("Invalid Input")
    def describe(self):
        print(f"The type of vehicle is {self.__class__.__name__}")


class Car(Vehicle):
    def get_fuel_efficiency(self):
        return 25

class Truck(Vehicle):
    def get_fuel_efficiency(self):
        return 15
try:
    vehicle = Vehicle.from_name(input("Enter the type of vehicle : car/truck"))
    print(f"Fuel efficiency is {vehicle.get_fuel_efficiency()} miles per gallon")
    vehicle.describe()
except ValueError as e:
    print(f"Error : {e}")
