def battery_is_ok(temperature):
  if temperature < 0 or temperature > 45:
    print('Temperature is out of range!')
    return False
  else:
    return True
def check_soc(soc):
  if soc < 20 or soc > 80:
    print('State of Charge is out of range!')
    return False
  else:
    return True
def check_charge_rate(charge_rate):
  if charge_rate > 0.8:
    print('Charge rate is out of range!')
    return False
  else:
    return True




if __name__ == '__main__':
  assert(battery_is_ok(25) is True)
  assert(battery_is_ok(50) is False)
  assert(check_soc(70) is True)
  assert(check_soc(85) is False)
  assert(check_charge_rate(0.7) is True)
  assert(check_charge_rate(0) is False)
