# 2019-2020 Programação II (LTI)
# Grupo 39
# 55371 Augusto Gouveia
# 54987 Miguel Fernandes

from Time import Time
from Date import Date


class Header:
    def __init__(self, fileName):
        """
        Reads the header from a given file and fills the object's variables

        Requires: A string representing the file name.
        Ensures: An object filled with the header's relevant information.
        """

        file = open(fileName, 'r')

        file.readline()
        hours = file.readline().strip().split("h")
        file.readline()
        date = file.readline().strip().split("-")
        file.readline()
        company = file.readline().replace("\n", '').strip(' ')
        self._hours = Time(int(hours[0]), int(hours[1]))
        self._date = Date(int(date[0]), int(date[1]), int(date[2]))
        self._company = company
        file.close()

    def getHours(self):
        """
        The time obtained from the header.

        Ensures: A time-type object representing the time obtained from the header.
        """
        return self._hours

    def getDate(self):
        """
        The date obtained from the header.

        Ensures: A date-type object representing the date obtained from the header.
        """
        return self._date

    def getCompany(self):
        """
        The company obtained from the header.

        Ensures: A string representing the company obtained from the header.
        """
        return self._company
