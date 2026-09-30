# config.py
# All the fixed values of the project are kept here so that
# if the parking rates change we only need to edit this one file.

RATE_2_WHEELER = 60        # rupees per hour
RATE_3_4_WHEELER = 80      # rupees per hour
FLAT_RATE = 1800           # flat fare for long parking
FLAT_RATE_AFTER_HOURS = 12 # more than 12 hours -> flat fare
MAX_HOURS = 24             # parking not allowed beyond this

DATA_FILE = "data/tickets.csv"
LOG_FILE = "logs/parking.log"
