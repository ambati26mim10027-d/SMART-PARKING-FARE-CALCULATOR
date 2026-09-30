# vehicle.py
# A small class to hold the details of a vehicle and its owner.

class Vehicle:
    def __init__(self, owner_name, license_plate, vehicle_type):
        self.owner_name = owner_name
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def get_type_name(self):
        if self.vehicle_type == "2":
            return "2-wheeler"
        return "3/4-wheeler"
