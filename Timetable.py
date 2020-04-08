# 2019-2020 Programação II (LTI)
# Grupo 39
# 55371 Augusto Gouveia
# 54987 Miguel Fernandes


class Timetable:
    def __init__(self):
        self._table = []

    def items(self):
        for item in self._table:
            yield item

    def add(self, assignment):
        self._table.append(assignment)

    def sort(self):
        ParcelsAssigned = []
        ParcelsCancelled = []
        finalTimetable = []
        for parcel in self._table:
            if parcel.getDrone() == "cancelled":
                ParcelsCancelled.append(parcel)
            else:
                ParcelsAssigned.append(parcel)
        ParcelsCancelled = sorted(ParcelsCancelled, key=lambda x: (x.getParcel()))  # sorts the cancelled parcels list
        # using the name as the key
        ParcelsAssigned = sorted(ParcelsAssigned, key=lambda x:
                                 (x.getDate().getDay(), x.getTime().getHours(),
                                  x.getTime().getMinutes(), x.getParcel()))
        # sorts the assigned parcels list using the date, time and name as keys

        # then aggregates both lists on one final list
        finalTimetable.extend(ParcelsCancelled)
        finalTimetable.extend(ParcelsAssigned)
        self._table = finalTimetable

    def writeFile(self, header, filenameinfo):
        """
        Creates a file representing the timetable.

        Requires: header is a Header-type object, representing the header's information.
        filenameinfo is a FileNameInfo-type object, representing the information retrieved from the drones' file name.
        Ensures: An output file representing the timetable.
        """
        fileNameDate = filenameinfo.getDate()
        fileNameTime = filenameinfo.getTime()
        fileName = "timetable" + str(fileNameTime.getHours()).zfill(2) + "h" \
                   + str(fileNameTime.getMinutes()).zfill(2) + "_" \
                   + str(fileNameDate.getYear()) + "y" + str(fileNameDate.getMonth()) + "m" \
                   + str(fileNameDate.getDay()) + ".txt "
        outFile = open(fileName, 'w')
        outFile.write("Time:\n")
        outFile.write(str(header.getHours()).replace(":", "h") + "\n")
        outFile.write("Day:\n")
        outFile.write(header.getDate().writeHeader() + "\n")
        outFile.write("Company:\n")
        outFile.write(header.getCompany() + "\n")
        outFile.write("Timeline:\n")
        for parcel in self.items():
            outFile.write(str(parcel) + "\n")
        outFile.close()
