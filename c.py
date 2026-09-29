import math

def calculate_parking_fare(vehicle_type, n_hours):
    # Clean the vehicle type input
    vehicle_type = str(vehicle_type).strip()
    
    # Check hour conditions and rules
    if n_hours <= 0:
        print("Invalid hours. Hours must be greater than 0.")
        return
    elif n_hours > 24:
        print("Parking not allowed for more than 24 hours.")
        return
    elif n_hours > 12:
        print("Total Parking Fare: ₹1800")
        return 1800
        
    # Assign rates based on vehicle type
    if vehicle_type == '2':
        hourly_rate = 60
    elif vehicle_type == '3' or vehicle_type == '4':
        hourly_rate = 80
    else:
        print("Invalid vehicle type.")
        return
        
    # Process partial hours and calculate fare using a loop
    rounded_hours = math.ceil(n_hours)
    total_fare = 0
    
    for hour in range(1, rounded_hours + 1):
        total_fare += hourly_rate
        
    print(f"Total Parking Fare: ₹{total_fare}")
    return total_fare

def main():
    name = input("What is your name? ")
    license_plate = input("License_plate_number: ")
    
    print(f"\nDriver Name: {name}")
    print(f"License Plate number: {license_plate}")
    
    vehicle_type = input("Enter vehicle type ('2' for 2-wheeler, '3' or '4' for 3/4-wheeler): ")
    
    try:
        n_hours = float(input("Enter hours parked: "))
        calculate_parking_fare(vehicle_type, n_hours)
    except ValueError:
        print("Invalid input for hours. Please enter a numeric value.")

if __name__ == "__main__":
    main()