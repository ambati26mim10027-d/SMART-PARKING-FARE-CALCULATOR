# ticket.py
# A parking ticket is created after the fare is calculated.
from datetime import datetime


class Ticket:
    def __init__(self, ticket_id, vehicle, hours, fare, date_time=None):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.hours = hours
        self.fare = fare
        # if no time is given we use the current time
        if date_time is None:
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.date_time = date_time

    def to_row(self):
        # order of this list must match the header in storage.py
        return [self.ticket_id, self.date_time, self.vehicle.owner_name,
                self.vehicle.license_plate, self.vehicle.vehicle_type,
                self.hours, self.fare]

    def show(self):
        print("\n------ PARKING TICKET ------")
        print("Ticket No     :", self.ticket_id)
        print("Date & Time   :", self.date_time)
        print("Driver Name   :", self.vehicle.owner_name)
        print("License Plate :", self.vehicle.license_plate)
        print("Vehicle Type  :", self.vehicle.get_type_name())
        print("Hours Parked  :", self.hours)
        print("Total Fare    : Rs.", self.fare)
        print("----------------------------")
