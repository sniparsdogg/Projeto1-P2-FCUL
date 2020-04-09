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
        """
        The name of the parcel.
        Ensures: A string representing the name of the parcel.
        """
        return self._name

    def getLocation(self):
        """
        The location of the parcel.

        Ensures: The name of the parcel.
        """
        return self._location

    def getDate(self):
        """
        The date requested for the delivery of the parcel.

        Ensures: A date-type object representing the date requested for the delivery of the parcel.
        """
        return self._date

    def getTime(self):
        """
        The time requested for the delivery of the parcel.

        Ensures: A time-type object representing the date requested for the delivery of the parcel.
        """
        return self._time

    def getDistance(self):
        """
        The distance of the parcel relative to the drone base.

        Ensures: An int number representing the distance of the parcel.
        """
        return self._distance

    def getWeight(self):
        """
        The weight of the parcel.

        Ensures: An int number representing the weight of the parcel.
        """
        return self._weight

    def getTimeRequired(self):
        """
        The minutes required to deliver the parcel.

        Ensures: An int number representing the minutes required to deliver the parcel.
        """
        return self._timeRequired
