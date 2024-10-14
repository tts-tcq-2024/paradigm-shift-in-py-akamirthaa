from warning import reaching_upper_limit

charge_rate_max_limit = 0.8

def charge_rate_warning(charge_rate):
    if reaching_upper_limit(charge_rate,charge_rate_max_limit):
        return f'Rate of charge is {charge_rate} and reaching upper limit'
    return "Rate of charge is within safe limits"

def check_charge_rate_limit(charge_rate):
    print(charge_rate_warning(charge_rate))
    if charge_rate > charge_rate_max_limit:
        print('Charge rate is out of range!')
        return False
    else:
        return True

# check_charge_rate_limit(0.77)