class House:

    def __init__(
            self,
            numberOfWindows=0,
            numberOfDoors=0,
            garageCarSize=0,
            hasAlarmSystem=False,
            hasPool=False):
        self.numberOfWindows = numberOfWindows
        self.numberOfDoors = numberOfDoors
        self.garageCarSize = garageCarSize
        self.hasAlarmSystem = hasAlarmSystem
        self.hasPool = hasPool

    def __str__(self):
        return f"numberOfWindows: {self.numberOfWindows}, \nnumberOfDoors: {self.numberOfDoors}, \nhasAlarmSystem: {self.hasAlarmSystem}, \nhasPool: {self.hasPool}"
