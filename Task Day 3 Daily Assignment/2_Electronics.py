from abc import ABC, abstractmethod

class ElectronicDevice(ABC):
    @abstractmethod
    def power_usage(self):
        pass
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def describe(self):
        print("Brand : "+self.brand)
        print("Model : "+self.model)
    @classmethod
    def from_type(cls,device_type : str):
        if device_type.lower() == "laptop":
            return Laptop("Dell","Inspiron")

        elif device_type.lower() == "smartphone":
            return Smartphone("Apple","15 Pro")
        else:
            raise ValueError("Invalid Input")

class Laptop(ElectronicDevice):
    screen_size = 15
    def power_usage(self):
        return 50
class Smartphone(ElectronicDevice):
    battery_life = 10
    def power_usage(self):
        return 10
try:
    string = input("Enter the type of device : laptop/smartphone")
    device = ElectronicDevice.from_type(string)
    power = device.power_usage()
    print(f"Power consumption per hour of usage is {power} watts per hour")
    device.describe()
except ValueError as e:
    print(f"Error : {e}")