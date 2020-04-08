# 2019-2020 Programação II (LTI)
# Grupo 39
# 55371 Augusto Gouveia
# 54987 Miguel Fernandes


class Time:
    def __init__(self, hours, minutes):
        self._hours = int(hours)
        self._minutes = int(minutes)

    def __str__(self):
        return str(self._hours).zfill(2) + ":" + str(self._minutes).zfill(2)

    def __eq__(self, other):
        return (self.getHours() == other.getHours()) and (self.getMinutes() == other.getMinutes())

    def __lt__(self, other):
        if self.getHours() == other.getHours():
            if self.getMinutes() < other.getMinutes():
                return True
            return False
        if self.getHours() < other.getHours():
            return True
        return False

    def getHours(self):
        return self._hours

    def getMinutes(self):
        return self._minutes

    def setHours(self, hours):
        self._hours = hours

    def setMinutes(self, minutes):
        self._minutes = minutes

    def sumMinutes(self, minutes):
        """
        Sums given minutes to a given time.

        Requires: The minutes to sum.
        Ensures: An updated time.
        """
        add_minutes = int(minutes)
        add_hours = 0

        final_hours = self.getHours()
        final_minutes = self.getMinutes()

        if add_minutes >= 60:
            while add_minutes >= 60:
                add_minutes -= 60
                add_hours += 1
        final_hours += add_hours
        final_minutes += add_minutes
        if final_minutes >= 60:
            final_minutes -= 60
            final_hours += 1

        return Time(final_hours, final_minutes)

    def finalTimeCustomer(self, minutes):
        """
        Returns the final time for the timetable.

        Requires: minutes is an int number. representing the minutes to sum.
        Ensures: The time at which the drone will start the parcel delivery.
        """

        deliveryHours = self.getHours()
        deliveryMinutes = self.getMinutes()

        if self.sumMinutes(minutes).getHours() >= 20 and self.sumMinutes(minutes).getMinutes() > 0:
            deliveryHours = 8
            deliveryMinutes = 0

        finalTime = Time(deliveryHours, deliveryMinutes)
        return finalTime

    def finalTimeDrone(self, minutes):
        """
        Returns the final time for the updated drone table.

        Requires: minutes is an int number, representing the minutes to sum.
        Ensures: The time at which the drone will be available for another delivery.
        """
        deliveryHours = self.sumMinutes(minutes).getHours()
        deliveryMinutes = self.sumMinutes(minutes).getMinutes()

        if deliveryHours >= 20 and deliveryMinutes > 0:
            newTime = Time(8, 0)
            deliveryHours = newTime.sumMinutes(minutes).getHours()
            deliveryMinutes = newTime.sumMinutes(minutes).getMinutes()

        finalTime = Time(deliveryHours, deliveryMinutes)
        return finalTime
