from warning import reaching_lower_limit, reaching_upper_limit

temperature_lower_limit = 0
temperature_upper_limit = 45

def temperature_warning(temperature):
    if reaching_lower_limit(temperature,temperature_upper_limit,temperature_lower_limit):
        return f'Temperature is {temperature} and reaching lower limit'
    if reaching_upper_limit(temperature,temperature_upper_limit):
        return f'Temperature is {temperature} and reaching upper limit'
    return "Temperature is within safe limits"


def check_temperature_limit(temperature):
    print(temperature_warning(temperature))
    if temperature < temperature_lower_limit or temperature > temperature_upper_limit:
        print('Temperature is out of range!')
        return False
    else:
        return True

# check_temperature_limit(2)
# check_temperature_limit(43)