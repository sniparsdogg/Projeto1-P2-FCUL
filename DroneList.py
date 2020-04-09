# 2019-2020 Programação II (LTI)
# Grupo 39
# 55371 Augusto Gouveia
# 54987 Miguel Fernandes


import copy
from Drone import Drone
from Date import Date
from Time import Time


class DroneList:
    def __init__(self, givenList=None):
        if givenList is None:
            givenList = []
        self._drones = copy.deepcopy(givenList)

    def readFile(self, fileName):
        """
        Reads the drones' file and assigns each drone to this collection.

        Requires: A string representing the file name.
        Ensures: A collection filled with the drones on the file.
        """

        file = open(fileName, 'r')

        for i in range(7):
            file.readline()

        while i := file.readline():
            if i != "\n":
                line = i.rstrip().split(", ")
                date = line[6].split("-")
                time = line[7].split(":")
                self.add(Drone(line[0], line[1], line[2], line[3], line[4], line[5],
                               Date(date[2], date[1], date[0]), Time(time[0], time[1])))

        file.close()

    def items(self):
        """
        Supports iteration over the current instance
        """
        for elem in self._drones:
            yield elem

    def sort(self):
        """
        Sorts the colllection as desired for the drone file.

        Ensures: An ordered drone collection.
        """
        self._drones = sorted(self._drones, key=lambda x: (x.getDate().getDay(),
                                                           x.getTime().getHours(),
                                                           x.getTime().getMinutes(),
                                                           -x.getBatteryLife(),
                                                           x.getName()))

    def append(self, drone):
        """
        Appends a drone to the drone list.

        Requires: drone is a Drone-type object that represents the drone to add to the collection.
        Ensures: Drone added to the drone list.
        """
        self._drones.append(drone)

    def length(self):
        """
        How many drones are in the collection.

        Returns: The size of the drone list.
        """
        return len(self._drones)

    def add(self, drone):
        self._drones.append(drone)

    def updateDrone(self, newDrone):
        for drone in self._drones:
            if drone.getName() == newDrone.getName():
                drone = newDrone

    def bestDrone(self):
        """
        Sorts the collection by date/time, battery life, mileage and lexicographically.
        Returns the best drone available in this collection.

        Ensures: An object representing the best drone available.
        """
        self._drones = sorted(self._drones, key=lambda x: (x.getDate().getDay(),
                                                           x.getTime().getHours(),
                                                           x.getTime().getMinutes(),
                                                           -x.getBatteryLife(),
                                                           x.getMileage(),
                                                           x.getName()))
        return copy.deepcopy(self._drones[0])

    def writeFile(self, header, filenameinfo):
        """
        Creates a file representing the updated drone list.

        Requires: header is a Header-type object, representing the header's information.
        filenameinfo is a FileNameInfo-type object, representing the information retrieved from the drones' file name.
        Ensures: An output file representing the updated drone list.
        """
        # TODO: https://stackoverflow.com/a/23199263
        time = filenameinfo.getTime().sumMinutes(30)
        date = filenameinfo.getDate()
        fileName = "drones" + str(time.getHours()).zfill(2) + "h" + str(time.getMinutes()).zfill(2) \
                   + "_" + str(date.getYear()) + "y" + str(date.getMonth()).zfill(2) \
                   + "m" + str(date.getDay()) + ".txt"
        outFile = open(fileName, 'w')
        outFile.write("Time:\n")
        outFile.write(str(time.getHours()).zfill(2) + "h" + str(time.getMinutes()).zfill(2) + "\n")
        outFile.write("Day:\n")
        outFile.write(header.getDate().writeHeader() + "\n")
        outFile.write("Company:\n")
        outFile.write(header.getCompany() + "\n")
        outFile.write("Drones:\n")
        for drone in self.items():
            outFile.write(str(drone) + "\n")
        outFile.close()
