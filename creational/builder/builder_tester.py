from HouseBuilder import HouseBuilder

house = HouseBuilder().builder().withWindows(8).withDoors(
    4).withGarage(3).withAlarmSystem(True).withPool(True).build()

print(house)
