from check_limits import is_battery_ok
from test_battery import test_battery_limits
from test_warnings import test_warning_limits

def main(temperature, soc, charge_rate):
    is_battery_ok(temperature, soc, charge_rate)

if __name__ == '__main__':
  main(20, 40, 0.7)
  test_battery_limits()
  test_warning_limits()