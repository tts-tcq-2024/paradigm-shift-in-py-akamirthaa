from warning import reaching_lower_limit, reaching_upper_limit

soc_lower_limit = 20
soc_upper_limit = 80

def soc_warning(soc):
    if reaching_lower_limit(soc,soc_upper_limit,soc_lower_limit):
        return f'State of charge is {soc} and reaching lower limit'
    if reaching_upper_limit(soc,soc_upper_limit):
        return f'State of charge is {soc} and reaching upper limit'
    return "State of charge is within safe limits"

def check_soc_limit(soc):
    print(soc_warning(soc))
    if soc < soc_lower_limit or soc > soc_upper_limit:
      print('State of Charge is out of range!')
      return False
    else:
      return True
    
# check_soc_limit(19)
    
