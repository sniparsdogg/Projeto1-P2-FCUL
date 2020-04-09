# 2019-2020 Programação II (LTI)
# Grupo 39
# 55371 Augusto Gouveia
# 54987 Miguel Fernandes


from Time import Time
from Date import Date


class FileNameInfo:
    def __init__(self, fileName):
        if fileName[:6] == "drones":
            self._date = Date(int(fileName[20:].strip(".txt")), int(fileName[17:19]), int(fileName[12:16]))
            self._time = Time(int(fileName[6:8]), int(fileName[9:11]))
        if fileName[:6] == "parcel":
            self._date = Date(int(fileName[21:].strip(".txt")), int(fileName[18:20]), int(fileName[13:17]))
            self._time = Time(int(fileName[7:9]), int(fileName[10:12]))

    def getDate(self):
        """
        The date on the filename.

        Ensures: The date on the filename.
        """
        return self._date

    def getTime(self):
        """
        The time on the filename.

        Ensures: The time on the filename.
        """
        return self._time
