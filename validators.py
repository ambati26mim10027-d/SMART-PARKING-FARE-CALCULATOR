# validators.py
# Functions that check the input given by the user.
# Every function returns the cleaned value, or raises ValueError with a message.
from config import MAX_HOURS


def validate_name(name):
    name = str(name).strip()
    if name == "":
        raise ValueError("Name cannot be empty.")
    # allow only letters and spaces in the name
    if not name.replace(" ", "").isalpha():
        raise ValueError("Name should contain only letters and spaces.")
    return name


def validate_license_plate(plate):
    # remove spaces and dashes, and make it capital letters
    plate = str(plate).strip().upper().replace(" ", "").replace("-", "")
    if plate == "":
        raise ValueError("License plate cannot be empty.")
    if not plate.isalnum():
        raise ValueError("License plate can have only letters and numbers.")
    if len(plate) < 6 or len(plate) > 10:
        raise ValueError("License plate should be 6 to 10 characters long.")
    return plate


def validate_vehicle_type(vehicle_type):
    vehicle_type = str(vehicle_type).strip()
    if vehicle_type not in ("2", "3", "4"):
        raise ValueError("Invalid vehicle type. Enter 2, 3 or 4.")
    return vehicle_type


def validate_hours(hours):
    try:
        hours = float(hours)
    except ValueError:
        raise ValueError("Invalid input for hours. Please enter a number.")
    if hours <= 0:
        raise ValueError("Invalid hours. Hours must be greater than 0.")
    if hours > MAX_HOURS:
        raise ValueError("Parking not allowed for more than 24 hours.")
    return hours
