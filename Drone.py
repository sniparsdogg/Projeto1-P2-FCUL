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
        """
        The name of the drone.
        Returns: A string representing the name of the drone.
        """
        return self._name

    def getLocation(self):
        """
        The location of the drone.
        Returns: A string representing the location of the drone.
        """
        return self._location

    def getMaxWeight(self):
        """
        The max weight that the drone can carry.
        Returns: An int representing the max weight that the drone can carry.
        """
        return self._maxWeight

    def getMaxDistance(self):
        """
        The max distance that the drone can travel.
        Returns: An int representing the max distance that the drone can travel.
        """
        return self._maxDistance

    def getMileage(self):
        """
        The total distance that the drone already travelled.
        Returns: A float representing the total distance that the drone already travelled.
        """
        return self._mileage

    def getBatteryLife(self):
        """
        The battery life that's left on the drone.
        Returns: A float representing the remaining battery life of this drone.
        """
        return self._batteryLife

    def getDate(self):
        """
        The date at which the drone is ready to fly.
        Returns: A date-type object representing the date at which the drone is ready to fly.
        """
        return self._date

    def getTime(self):
        """
        The time at which the drone is ready to fly.
        Returns: A time-type object representing the time at which the drone is ready to fly.
        """
        return self._time

    def setTime(self, time):
        """
        Setter of the drone's time.

        Requires: time is a Time-type object that represents the time to update.
        Ensures: Updated time on the drone.
        """
        self._time = time

    def setDate(self, date):
        """
        Setter of the drone's date.

        Requires: date is a Date-type object that represents the date to update.
        Ensures: Updated date on the drone.
        """
        self._date = date

    def setMileage(self, mileage):
        """
        Setter of the drone's mileage.

        Requires: mileage is a float number that represents the mileage to update.
        Ensures: Updated mileage on the drone.
        """
        self._mileage = mileage

    def setBatteryLife(self, batteryLife):
        """
        Setter of the drone's battery life.

        Requires: batteryLife is a float number that represents the battery life to update.
        Ensures: Updated battery life on the drone.
        """
        self._batteryLife = batteryLife

    def checkpoint(self, parcel):
        """
        Checks if this drone can deliver the given parcel.

        Requires: parcel is a Parcel-type object.
        Ensures: boolean that represents if this drone can or not deliver the parcel.
        """
        parcelLocation = parcel.getLocation()
        droneLocation = self.getLocation()
        if parcelLocation == droneLocation:  # the drone must be located in the \
            # same zone as the request
            returnTrip = 2
            kilometer = 1000
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
                        return True  # if it meets all these requirements, this drone can \
                        # assigned to the given parcel
        return False  # this drone can't be assigned to the given parcel
