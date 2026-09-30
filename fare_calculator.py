# fare_calculator.py
# Main logic of the project: works out the parking fare.
import math
import config


def get_hourly_rate(vehicle_type):
    if vehicle_type == "2":
        return config.RATE_2_WHEELER
    elif vehicle_type == "3" or vehicle_type == "4":
        return config.RATE_3_4_WHEELER
    else:
        raise ValueError("Invalid vehicle type.")


def calculate_fare(vehicle_type, hours):
    # check the vehicle type first so wrong types never get a fare
    rate = get_hourly_rate(vehicle_type)

    if hours <= 0:
        raise ValueError("Invalid hours. Hours must be greater than 0.")
    if hours > config.MAX_HOURS:
        raise ValueError("Parking not allowed for more than 24 hours.")

    # more than 12 hours (and up to 24) is a flat fare
    if hours > config.FLAT_RATE_AFTER_HOURS:
        return config.FLAT_RATE

    # partial hour is counted as a full hour, e.g. 2.1 hours -> 3 hours
    rounded_hours = math.ceil(hours)

    total_fare = 0
    for hour in range(rounded_hours):
        total_fare = total_fare + rate
    return total_fare
