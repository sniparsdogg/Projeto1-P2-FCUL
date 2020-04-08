# 2019-2020 Programação II (LTI)
# Grupo 39
# 55371 Augusto Gouveia
# 54987 Miguel Fernandes


class Parcel:
    def __init__(self, name, location, date, time, distance, weight, timeRequired):
        self._name = name
        self._location = location
        self._date = date
        self._time = time
        self._distance = int(distance)
        self._weight = int(weight)
        self._timeRequired = int(timeRequired)

    def __str__(self):
        return self._name + ", " + self._location + ", " + str(self._date) + ", " + str(self._time)\
               + ", " + str(self._distance) + ", " + str(self._weight) + ", " + str(self._timeRequired)

    def getName(self):
        return self._name

    def getLocation(self):
        return self._location

    def getDate(self):
        return self._date

    def getTime(self):
        return self._time

    def getDistance(self):
        return self._distance

    def getWeight(self):
        return self._weight

    def getTimeRequired(self):
        return self._timeRequired
