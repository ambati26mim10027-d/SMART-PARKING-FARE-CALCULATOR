# report.py
# Simple reports made from the saved tickets.


def search_by_plate(records, plate):
    plate = plate.strip().upper().replace(" ", "").replace("-", "")
    found = []
    for r in records:
        if r["license_plate"] == plate:
            found.append(r)
    return found


def summary(records):
    # returns a dictionary with totals
    result = {"total_tickets": 0, "total_earnings": 0,
              "two_wheeler_earnings": 0, "other_earnings": 0,
              "highest_fare": 0}
    for r in records:
        fare = int(r["fare"])
        result["total_tickets"] += 1
        result["total_earnings"] += fare
        if r["vehicle_type"] == "2":
            result["two_wheeler_earnings"] += fare
        else:
            result["other_earnings"] += fare
        if fare > result["highest_fare"]:
            result["highest_fare"] = fare
    return result


def print_records(records):
    if len(records) == 0:
        print("No records found.")
        return
    print("\nID | Date & Time         | Name | Plate | Type | Hours | Fare")
    for r in records:
        print(r["ticket_id"], "|", r["date_time"], "|", r["name"], "|",
              r["license_plate"], "|", r["vehicle_type"], "|",
              r["hours"], "|", r["fare"])


def print_summary(records):
    s = summary(records)
    print("\n------ SUMMARY REPORT ------")
    print("Total tickets          :", s["total_tickets"])
    print("Total earnings         : Rs.", s["total_earnings"])
    print("2-wheeler earnings     : Rs.", s["two_wheeler_earnings"])
    print("3/4-wheeler earnings   : Rs.", s["other_earnings"])
    print("Highest single fare    : Rs.", s["highest_fare"])
