from MotorcycleDriverAdapter import MotorcycleDriverAdapter
from Motorcycle import Motorcycle
from Driver import Driver
from Car import Car

motorcycle = Motorcycle()
car = Car()

driver = Driver()

driver.accelerate(car)
driver.accelerate(MotorcycleDriverAdapter(motorcycle))
