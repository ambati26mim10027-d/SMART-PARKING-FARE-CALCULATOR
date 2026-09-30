import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import validators


class TestValidators(unittest.TestCase):
    def test_good_name(self):
        self.assertEqual(validators.validate_name("  Rahul Sharma "), "Rahul Sharma")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            validators.validate_name("   ")

    def test_name_with_numbers(self):
        with self.assertRaises(ValueError):
            validators.validate_name("Rahul123")

    def test_plate_is_cleaned(self):
        self.assertEqual(validators.validate_license_plate("tn 09-ab 1234"), "TN09AB1234")

    def test_plate_too_short(self):
        with self.assertRaises(ValueError):
            validators.validate_license_plate("AB1")

    def test_plate_special_characters(self):
        with self.assertRaises(ValueError):
            validators.validate_license_plate("TN09@#1234")

    def test_vehicle_type_valid(self):
        self.assertEqual(validators.validate_vehicle_type(" 3 "), "3")

    def test_vehicle_type_invalid(self):
        with self.assertRaises(ValueError):
            validators.validate_vehicle_type("7")

    def test_hours_text(self):
        with self.assertRaises(ValueError):
            validators.validate_hours("abc")

    def test_hours_negative(self):
        with self.assertRaises(ValueError):
            validators.validate_hours("-2")

    def test_hours_valid(self):
        self.assertEqual(validators.validate_hours("2.5"), 2.5)


if __name__ == "__main__":
    unittest.main()
