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
        Reads the drones' file and assigns each drone to a sub-list, returning a list of all the drones in the file.

        Requires: A string representing the file name
        Ensures: A list representing the drones.
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
        self._drones = sorted(self._drones, key=lambda x: (x.getDate().getDay(),
                                                           x.getTime().getHours(),
                                                           x.getTime().getMinutes(),
                                                           -x.getBatteryLife(),
                                                           x.getName()))

    def append(self, drone):
        self._drones.append(drone)

    def length(self):
        return len(self._drones)

    # TODO: find a way to append drones

    def add(self, drone):
        self._drones.append(drone)

    def updateDrone(self, newDrone):
        for drone in self._drones:
            if drone.getName() == newDrone.getName():
                drone = newDrone

    def bestDrone(self):
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

        Requires: header and droneList are lists, each representing the header's information and the updated drone list,
        respectively. date and hour are strings, each representing the date and time to use on the file, respectively.
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
