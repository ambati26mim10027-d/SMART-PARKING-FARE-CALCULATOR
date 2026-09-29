# Parking Fare Calculator

## Overview
This is a simple Python program that works out how much someone has to pay for parking. The user types in their name, their license plate number, what type of vehicle they have, and how many hours they parked for. The program then works out the total fare and prints it on the screen.

## Features
- Asks the driver for their name and license plate number
- Works out the parking fare based on vehicle type:
  - 2-wheelers: ₹60 per hour
  - 3 or 4-wheelers: ₹80 per hour
- Rounds part-hours up to the next full hour (so 1.5 hours counts as 2 hours)
- Charges a flat rate of ₹1800 if you park for more than 12 hours
- Stops you from parking for more than 24 hours
- Checks that the hours entered are a valid number greater than 0
- Checks that the vehicle type entered is valid ('2', '3', or '4')

## Technologies/Tools Used
- Python 3
- The built-in `math` module (used to round hours up)

## Steps to Install & Run
1. Make sure Python 3 is installed on your computer.
2. Save the code in a file called `parking_fare.py`.
3. Open a terminal (or command prompt) in the folder where you saved the file.
4. Run this command:
   ```
   python parking_fare.py
   ```
5. Follow the instructions on the screen: enter your name, license plate number, vehicle type, and hours parked.

## Instructions for Testing
Try running the program with these examples to check it works properly:

| Test | What to enter | What should happen |
|------|----------------|---------------------|
| Normal 2-wheeler | Vehicle type `2`, hours `3` | Fare shows as ₹180 |
| Normal 4-wheeler | Vehicle type `4`, hours `2` | Fare shows as ₹160 |
| Part-hour | Vehicle type `2`, hours `2.5` | Rounds up to 3 hours, fare ₹180 |
| Long stay | Vehicle type `3`, hours `13` | Flat fare of ₹1800 |
| Too long | Vehicle type `2`, hours `25` | Message saying parking isn't allowed |
| Zero hours | Vehicle type `2`, hours `0` | Message saying hours must be greater than 0 |
| Wrong vehicle type | Vehicle type `9`, hours `3` | Message saying the vehicle type is invalid |
| Wrong input | Type letters instead of a number for hours | Message asking for a valid number |

## Screenshots
*(Optional — add a screenshot here showing the program running in the terminal, from entering your name to seeing the final fare.)*
