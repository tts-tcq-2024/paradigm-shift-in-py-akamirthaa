from temperature import check_temperature_limit
from charge_rate import check_charge_rate_limit
from state_of_charge import check_soc_limit

def is_battery_ok(temperature, soc, charge_rate):
    return (check_temperature_limit(temperature) and check_soc_limit(soc) and check_charge_rate_limit(charge_rate))
