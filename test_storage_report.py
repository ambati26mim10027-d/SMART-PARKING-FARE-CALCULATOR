import sys, os, unittest, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import storage
import report
from vehicle import Vehicle
from ticket import Ticket


class TestStorageAndReport(unittest.TestCase):
    def setUp(self):
        # use a temporary file so real data is not touched
        self.folder = tempfile.mkdtemp()
        self.path = os.path.join(self.folder, "test_tickets.csv")

    def make_ticket(self, tid, plate, v_type, hours, fare):
        return Ticket(tid, Vehicle("Test", plate, v_type), hours, fare)

    def test_no_file_gives_empty_list(self):
        self.assertEqual(storage.load_tickets(self.path), [])

    def test_save_and_load(self):
        storage.save_ticket(self.make_ticket(1, "TN09AB1234", "2", 2, 120), self.path)
        records = storage.load_tickets(self.path)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["license_plate"], "TN09AB1234")

    def test_next_ticket_id(self):
        self.assertEqual(storage.get_next_ticket_id(self.path), 1)
        storage.save_ticket(self.make_ticket(1, "TN09AB1234", "2", 2, 120), self.path)
        self.assertEqual(storage.get_next_ticket_id(self.path), 2)

    def test_search_by_plate(self):
        storage.save_ticket(self.make_ticket(1, "TN09AB1234", "2", 2, 120), self.path)
        storage.save_ticket(self.make_ticket(2, "KA01CD5678", "4", 1, 80), self.path)
        found = report.search_by_plate(storage.load_tickets(self.path), "ka01-cd 5678")
        self.assertEqual(len(found), 1)

    def test_summary(self):
        storage.save_ticket(self.make_ticket(1, "TN09AB1234", "2", 2, 120), self.path)
        storage.save_ticket(self.make_ticket(2, "KA01CD5678", "4", 1, 80), self.path)
        s = report.summary(storage.load_tickets(self.path))
        self.assertEqual(s["total_tickets"], 2)
        self.assertEqual(s["total_earnings"], 200)
        self.assertEqual(s["two_wheeler_earnings"], 120)
        self.assertEqual(s["highest_fare"], 120)


if __name__ == "__main__":
    unittest.main()
