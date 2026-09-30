import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import fare_calculator


class TestFare(unittest.TestCase):
    def test_two_wheeler_one_hour(self):
        self.assertEqual(fare_calculator.calculate_fare("2", 1), 60)

    def test_four_wheeler_three_hours(self):
        self.assertEqual(fare_calculator.calculate_fare("4", 3), 240)

    def test_three_wheeler_same_as_four(self):
        self.assertEqual(fare_calculator.calculate_fare("3", 2), 160)

    def test_partial_hour_rounds_up(self):
        self.assertEqual(fare_calculator.calculate_fare("2", 2.1), 180)

    def test_exactly_12_hours_not_flat(self):
        self.assertEqual(fare_calculator.calculate_fare("2", 12), 720)

    def test_more_than_12_hours_flat(self):
        self.assertEqual(fare_calculator.calculate_fare("4", 12.5), 1800)

    def test_exactly_24_hours_allowed(self):
        self.assertEqual(fare_calculator.calculate_fare("2", 24), 1800)

    def test_more_than_24_hours(self):
        with self.assertRaises(ValueError):
            fare_calculator.calculate_fare("2", 25)

    def test_zero_hours(self):
        with self.assertRaises(ValueError):
            fare_calculator.calculate_fare("2", 0)

    def test_wrong_vehicle_type(self):
        with self.assertRaises(ValueError):
            fare_calculator.calculate_fare("5", 2)


if __name__ == "__main__":
    unittest.main()
