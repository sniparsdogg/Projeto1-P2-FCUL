# 2019-2020 Programação II (LTI)
# Grupo 39
# 55371 Augusto Gouveia
# 54987 Miguel Fernandes


class Date:
    def __init__(self, day, month, year):
        self._day = int(day)
        self._month = int(month)
        self._year = int(year)

    def __str__(self):
        return str(self._year) + "-" + str(self._month) + "-" + str(self._day).zfill(2)

    def __eq__(self, other):
        return (self.getYear() == other.getYear()) and (self.getMonth() == other.getMonth()) \
            and (self.getDay() == other.getDay())

    def __lt__(self, other):
        if self.getYear() == other.getYear():
            if self.getMonth() == other.getMonth():
                if self.getDay() < other.getDay():
                    return True
                return False
            if self.getMonth() < other.getMonth():
                return True
            return False
        if self.getYear() < other.getYear():
            return True
        return False

    def getDay(self):
        """
        The day component of the date.
        Returns: An int representing the day.
        """
        return self._day

    def getMonth(self):
        """
        The month component of the date.
        Returns: An int representing the month.
        """
        return self._month

    def getYear(self):
        """
        The year component of the date.
        Returns: An int representing the year.
        """
        return self._year

    def writeHeader(self):
        """
        Returns a string representing the date's correct format for the header.
        """
        return str(self.getDay()) + "-" + str(self.getMonth()) + "-" + str(self.getYear())

    def finalDate(self, time, minutes):
        """
        Returns the final date/time for the timetable.

        Requires: time is a Time-type object, representing the time assigned to deliver the parcel.
        minutes is an int, representing the minutes to sum.
        Ensures: The date at which the drone will start the parcel delivery / is ready for the next delivery.
        """
        deliveryYear = self.getYear()
        deliveryMonth = self.getMonth()
        deliveryDay = self.getDay()

        if time.sumMinutes(minutes).getHours() >= 20 and time.sumMinutes(minutes).getMinutes() > 0:
            deliveryDay += 1

            if deliveryDay > 30:
                deliveryDay = 1
                deliveryMonth += 1

            if deliveryMonth > 12:
                deliveryMonth = 1
                deliveryYear += 1

        finalDate = Date(deliveryDay, deliveryMonth, deliveryYear)
        return finalDate
