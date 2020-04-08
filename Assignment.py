# 2019-2020 Programação II (LTI)
# Grupo 39
# 55371 Augusto Gouveia
# 54987 Miguel Fernandes


class Assignment:
    def __init__(self, date, time, pName, dName):
        self._date = date
        self._time = time
        self._parcel = pName
        self._drone = dName

    def __str__(self):
        return str(self._date) + ", " + str(self._time) + ", " + str(self._parcel) + ", " + str(self._drone)

    def getDate(self):
        return self._date

    def getTime(self):
        return self._time

    def getParcel(self):
        return self._parcel

    def getDrone(self):
        return self._drone
