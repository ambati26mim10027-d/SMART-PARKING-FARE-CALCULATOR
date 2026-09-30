# main.py
# Entry point of the Smart Parking Fare Calculator.
# Run it from the project folder:  python src/main.py
import validators
import fare_calculator
import storage
import report
from vehicle import Vehicle
from ticket import Ticket
from logger_setup import get_logger

logger = get_logger()


def ask_until_valid(message, check_function):
    # keeps asking until the user gives a proper value
    while True:
        value = input(message)
        try:
            return check_function(value)
        except ValueError as error:
            print("Error:", error)
            logger.warning("Invalid input: %s", error)


def new_parking_entry():
    name = ask_until_valid("What is your name? ", validators.validate_name)
    plate = ask_until_valid("License plate number: ", validators.validate_license_plate)
    v_type = ask_until_valid("Vehicle type ('2' for 2-wheeler, '3' or '4' for 3/4-wheeler): ",
                             validators.validate_vehicle_type)
    hours = ask_until_valid("Hours parked: ", validators.validate_hours)

    fare = fare_calculator.calculate_fare(v_type, hours)

    vehicle = Vehicle(name, plate, v_type)
    ticket = Ticket(storage.get_next_ticket_id(), vehicle, hours, fare)
    ticket.show()
    storage.save_ticket(ticket)
    logger.info("Ticket %s saved for %s, fare %s", ticket.ticket_id, plate, fare)


def search_vehicle():
    plate = input("Enter license plate to search: ")
    records = storage.load_tickets()
    report.print_records(report.search_by_plate(records, plate))


def main():
    print("=== Smart Parking Fare Calculator ===")
    logger.info("Program started")
    while True:
        print("\n1. New parking entry")
        print("2. View all tickets")
        print("3. Search by license plate")
        print("4. Summary report")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            new_parking_entry()
        elif choice == "2":
            report.print_records(storage.load_tickets())
        elif choice == "3":
            search_vehicle()
        elif choice == "4":
            report.print_summary(storage.load_tickets())
        elif choice == "5":
            print("Thank you. Bye!")
            logger.info("Program closed")
            break
        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
