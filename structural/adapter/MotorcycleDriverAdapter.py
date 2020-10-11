from Car import Car

class MotorcycleDriverAdapter(Car):

    def __init__(self, motorcycle):
        self.motorcycle = motorcycle

    def press_gas_pedal(self):
        self.motorcycle.apply_throttle()