from House import House


class HouseBuilder:

    def __init__(self):
        pass

    def builder(self):
        return self

    def withWindows(self, numberOfWindows=0):
        self.numberOfWindows = numberOfWindows
        return self

    def withDoors(self, numberOfDoors=0):
        self.numberOfDoors = numberOfDoors
        return self

    def withGarage(self, garageCarSize=0):
        self.garageCarSize = garageCarSize
        return self

    def withAlarmSystem(self, hasAlarmSystem=0):
        self.hasAlarmSystem = hasAlarmSystem
        return self

    def withPool(self, hasPool=0):
        self.hasPool = hasPool
        return self

    def build(self):
        return House(
            self.numberOfWindows,
            self.numberOfDoors,
            self.garageCarSize,
            self.hasAlarmSystem,
            self.hasPool)
