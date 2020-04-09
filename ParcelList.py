# 2019-2020 Programação II (LTI)
# Grupo 39
# 55371 Augusto Gouveia
# 54987 Miguel Fernandes


import copy
from Parcel import Parcel
from Time import Time
from Date import Date


class ParcelList:
    def __init__(self, givenList=None):
        if givenList is None:
            givenList = []
        self._parcels = copy.deepcopy(givenList)

    def readFile(self, fileName):
        """
        Reads the parcels' file and assigns each parcel to a sub-list, returning a list of all the parcels in the file.

        Requires: A string representing the file name.
        Ensures: A list representing the parcels.
        """

        file = open(fileName, 'r')

        for i in range(7):
            file.readline()

        while i := file.readline():
            if i != "\n":
                line = i.rstrip().split(", ")
                date = line[2].split("-")
                time = line[3].split(":")
                self.add(Parcel(line[0], line[1], Date(date[2], date[1], date[0]),
                                Time(time[0], time[1]), line[4], line[5], line[6]))

        file.close()

    def items(self):
        """
        Supports iteration over the current instance
        """
        for elem in self._parcels:
            yield elem

    def add(self, parcel):
        """
        Adds the given parcel to the parcel list.

        Requires: parcel is a Parcel-type object that represents the parcel to add to the parcel collection.
        Ensures: Added parcel to the parcel list.
        """
        self._parcels.append(parcel)
