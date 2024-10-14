import unittest
from temperature import temperature_warning
from state_of_charge import soc_warning
from charge_rate import charge_rate_warning

class TestWarnings(unittest.TestCase):

    def test_temperature_warning(self):
        self.assertEqual(temperature_warning(20),"Temperature is within safe limits")
        self.assertEqual(temperature_warning(1),f'Temperature is 1 and reaching lower limit')
        self.assertEqual(temperature_warning(44),f'Temperature is 44 and reaching upper limit')

    def test_soc_warning(self):
        self.assertEqual(soc_warning(30),f'State of charge is within safe limits')
        self.assertEqual(soc_warning(22),f'State of charge is 22 and reaching lower limit')
        self.assertEqual(soc_warning(77),f'State of charge is 77 and reaching upper limit')

    def test_charge_rate_warning(self):
        self.assertEqual(charge_rate_warning(0.7), "Rate of charge is within safe limits" )
        self.assertEqual(charge_rate_warning(0.78), f'Rate of charge is 0.78 and reaching upper limit' )

if __name__ == '__main__':
    unittest.main()
