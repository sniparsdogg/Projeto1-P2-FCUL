# 2019-2020 Programação II (LTI)
# Grupo 39
# 55371 Augusto Gouveia
# 54987 Miguel Fernandes


class Drone:
    def __init__(self, name=None, location=None, maxWeight=0, maxDistance=0, mileage=0,
                 batteryLife=0, date=None, time=None):
        self._name = name
        self._location = location
        self._maxWeight = int(maxWeight)
        self._maxDistance = int(maxDistance)
        self._mileage = float(mileage)
        self._batteryLife = float(batteryLife)
        self._date = date
        self._time = time

    def __str__(self):
        return self._name + ", " + self._location + ", " + str(self._maxWeight) + ", " + str(self._maxDistance) \
               + ", " + str(self._mileage) + ", " + str(self._batteryLife) + ", " + str(self._date)\
               + ", " + str(self._time)

    def getName(self):
        return self._name

    def getLocation(self):
        return self._location

    def getMaxWeight(self):
        return self._maxWeight

    def getMaxDistance(self):
        return self._maxDistance

    def getMileage(self):
        return self._mileage

    def getBatteryLife(self):
        return self._batteryLife

    def getDate(self):
        return self._date

    def getTime(self):
        return self._time

    def setTime(self, time):
        self._time = time

    def setDate(self, date):
        self._date = date

    def setMileage(self, mileage):
        self._mileage = mileage

    def setBatteryLife(self, batteryLife):
        self._batteryLife = batteryLife

    def updateMileage(self, distance):
        self.setMileage(self.getMileage() + distance)

    def updateBatteryLife(self, distance):
        self.setBatteryLife(self.getBatteryLife() - distance)

    def checkpoint(self, parcel):
        parcelLocation = parcel.getLocation()
        droneLocation = self.getLocation()
        returnTrip = 2
        kilometer = 1000
        if parcelLocation == droneLocation:  # the drone must be located in the \
            # same zone as the request
            totalDistance = parcel.getDistance() * returnTrip
            droneRange = self.getBatteryLife() * kilometer
            if totalDistance <= droneRange:  # the drone must have enough battery life to \
                # get to the request location and come back
                parcelWeight = parcel.getWeight()
                droneMaxWeight = self.getMaxWeight()
                if parcelWeight <= droneMaxWeight:  # the drone must be able to \
                    # take the weight of the package
                    deliveryDistance = parcel.getDistance()
                    droneMaxDistance = self.getMaxDistance()
                    if deliveryDistance <= droneMaxDistance:  # the distance of the request \
                        # can't be bigger than the drone's max distance
                        return True  # if it meets all these requirements, the drone is \
                        # assigned to its respective parcel
        return False
