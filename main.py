import unittest
from check_limits import is_battery_ok
from test_battery import TestBattery
from test_warnings import TestWarnings

def main():
    is_battery_ok(20, 40, 0.7)
    
if __name__ == '__main__':
    main()
    unittest.main(exit=False)
