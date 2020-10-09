from Truck import Truck
from Sedan import Sedan

class VehicleFactory:

    def __init__(self):
        pass

    def create_vehicle(self, type):
        return Truck() if type=="Truck" else Sedan()



print(VehicleFactory().create_vehicle("Truck"))

print(VehicleFactory().create_vehicle("Sedan"))