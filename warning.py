def calculate_tolerance(upper_limit):
    tolerance = (5/100) * upper_limit
    print(round(tolerance,2))
    return round(tolerance,2)

def reaching_lower_limit(value,upper_limit,lower_limit):
    lower_tolerance_level = calculate_tolerance(upper_limit) + lower_limit
    print(lower_tolerance_level)
    if lower_limit <= value <= lower_tolerance_level:
        return True
    return False

def reaching_upper_limit(value,upper_limit):
    upper_tolerance_level = upper_limit - calculate_tolerance(upper_limit)
    print(upper_tolerance_level)
    if upper_tolerance_level <= value <= upper_limit:
        return True
    return False

# print(show_warning(22,80,20))
# print("---------------------------")
# print(show_warning(80,80,20))
    
    