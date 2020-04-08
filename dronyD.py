# 2019-2020 Programação II (LTI)
# Grupo 39
# 55371 Augusto Gouveia
# 54987 Miguel Fernandes


import sys
from Drone import Drone
from DroneList import DroneList
from ParcelList import ParcelList
from Timetable import Timetable
from Assignment import Assignment
from FileNameInfo import FileNameInfo
from Header import Header


def allocate(fileNameDrones, fileNameParcels):
    """
    Assign given drones to given parcels.
    
    Requires: fileNameDrones, fileNameParcels are str, with the names
    of the files representing the list of drones and parcels, respectively,
    following the format indicated in the project sheet.
    Ensures: Two output files, respectively, with the listing of scheduled
    transportation of parcels and the updated listing of drones, following the format
    and naming convention indicated in the project sheet.
    """

    fileNameInfo = FileNameInfo(fileNameDrones)

    droneList = DroneList()
    droneList.readFile(fileNameDrones)  # this is the drones collection with info from the drone file
    parcelsList = ParcelList()
    parcelsList.readFile(fileNameParcels)  # this is the parcels collection with info from the parcel file
    header = Header(fileNameDrones) # this will be the header info
    droneAssignment = Timetable()  # this will be the timetable

    for parcel in parcelsList.items():
        # assign the available drones for each delivery
        availableDroneList = DroneList()  # a new drone collection is created for each parcel in order to know
        # what drones can deliver this parcel
        for drone in droneList.items():
            if drone.checkpoint(parcel):  # the drone will go through a series of checks
                # if this function returns true, it means it can deliver the parcel
                availableDroneList.append(drone)  # the drone is added to the respective parcel

        if availableDroneList.length() >= 1:  # if there is at least one drone assigned then
            # we will use the best drone available (first drone)
            delivery = availableDroneList.bestDrone()  # sorts the collection and returns the best drone

            # The delivery date/hour will the the latest one between the request date/hour and the drone availability
            if delivery.getTime() < parcel.getTime() or delivery.getDate() < parcel.getDate():
                delivery.setTime(parcel.getTime())
                delivery.setDate(parcel.getDate())

            # we need to verify if the time needed to deliver the parcel exceeds the closing time (20:00)
            # if it does, then the date/time is set to the next day at the opening time (08:00)
            deliveryDate = delivery.getDate()
            deliveryTime = delivery.getTime()
            delivery.setDate(deliveryDate.finalDate(delivery.getTime(), parcel.getTimeRequired()))
            delivery.setTime(deliveryTime.finalTimeCustomer(parcel.getTimeRequired()))

            # now we enter the date, time, name of the parcel and name of the drone assigned to an Assignment object
            # which is then added to the timetable collection
            newAssignment = Assignment(delivery.getDate(), delivery.getTime(),
                                       parcel.getName(), delivery.getName())
            droneAssignment.add(newAssignment)

            # now we need to update the mileage and range on the drone assigned

            kilometer = 1000
            returnTrip = 2

            # we add the total distance of the trip in kilometers to the drone's mileage
            # and subtract the same value to the drone's battery life
            newMileage = delivery.getMileage() + (parcel.getDistance() * returnTrip) / kilometer
            newRange = delivery.getBatteryLife() - (parcel.getDistance() * returnTrip) / kilometer

            # here we're going to search for every drone on the original drone list for the one
            # that was assigned to the delivery and update its available date, time, mileage and battery life
            for drone in droneList.items():
                if delivery.getName() == drone.getName():  # if this is the drone assigned, we want to update its:
                    drone.setDate(delivery.getDate().finalDate(delivery.getTime(),
                                                               parcel.getTimeRequired()))  # date,
                    drone.setTime(delivery.getTime().finalTimeDrone(parcel.getTimeRequired()))  # time,
                    drone.setMileage(round(newMileage, 1))  # mileage
                    drone.setBatteryLife(round(newRange, 1))  # and battery life
                    droneList.updateDrone(drone)  # finally, we update the drone's values on the original drone list

        else:  # if no drone was assigned to the delivery we're going to inform the timetable of such
            newAssignment = Assignment(parcel.getDate(), parcel.getTime(), parcel.getName(), "cancelled")
            droneAssignment.add(newAssignment)
    # now we need to order these collections
    # the timetable will be ordered by status, assigned date/hour and lexicographically, both ascending
    droneAssignment.sort()
    # the drone collection will be ordered by availability and lexicographically, ascending,
    # and by remaining battery life, descending
    droneList.sort()

    # finally, these collections will write the files
    droneAssignment.writeFile(header, fileNameInfo)
    droneList.writeFile(header, fileNameInfo)

    # and we're done!


inputFileName1, inputFileName2 = sys.argv[1:]

try:
    # these lines will extract the relevant header information from the files
    headerDrones = Header(inputFileName1)
    headerParcels = Header(inputFileName2)

    # these lines will extract the date and time from the file names
    droneFileName = FileNameInfo(inputFileName1)
    parcelsFileName = FileNameInfo(inputFileName2)

    # the program runs two assertion tests to make sure the header info is consistent with the file name info
    # if not, it throws an input error
    assert droneFileName.getDate() == headerDrones.getDate() \
        and droneFileName.getTime() == headerDrones.getHours(), \
        "Input error: name and header inconsistent in file " + inputFileName1 + "."

    assert parcelsFileName.getDate() == headerParcels.getDate() \
        and parcelsFileName.getTime() == headerParcels.getHours(), \
        "Input error: name and header inconsistent in file " + inputFileName2 + "."

    # the program runs one more assertion test to make sure the headers from the drones and parcels files are consistent
    # with each other
    # if not, it throws an input error
    assert headerDrones.getHours() == headerParcels.getHours() \
        and headerDrones.getDate() == headerDrones.getDate() \
        and headerDrones.getCompany() == headerParcels.getCompany(), \
        "Input error: inconsistent files " + inputFileName1 + " and " + inputFileName2 + "."

    # if everything checks out, it begins to assign the drones to the parcels
    allocate(inputFileName1, inputFileName2)

# if an error is thrown, the program will print the message error to the screen
except AssertionError as error:
    print(error)
