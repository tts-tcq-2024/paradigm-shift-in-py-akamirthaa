import unittest
from check_limits import is_battery_ok

class TestBattery(unittest.TestCase):

    def test_is_battery_ok(self):
        self.assertEqual(is_battery_ok(20, 40, 0.7),True)
        self.assertEqual(is_battery_ok(47, 40, 0.7), False)
        self.assertEqual(is_battery_ok(20, 18, 0.7), False)
        self.assertEqual(is_battery_ok(20, 40, 0.9), False)
        self.assertEqual(is_battery_ok(44, 40, 0.7),True)

if __name__ == '__main__':
    unittest.main()
