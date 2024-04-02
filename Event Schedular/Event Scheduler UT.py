import datetime
import unittest

from main import validate_date, validate_time


class TestEventManager(unittest.TestCase):
    def test_validate_date(self):
        self.assertEqual(validate_date("2022-01-30"), datetime.date(2022, 1, 30))
        self.assertIsNone(validate_date("invalid_date"))

    def test_validate_time(self):
        self.assertEqual(validate_time("12:34"), datetime.time(12, 34))
        self.assertIsNone(validate_time("invalid_time"))

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()
