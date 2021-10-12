
def get_dow(prompt):
    user_input = input(f'{prompt} ')
    return user_input

def get_dow_rate():
    print('This one returns the day of the week rate')

def get_str():
    print('Check if the user has typed in a string or not')

def base_rate_based_on_day(prompt, data_type='str'):

    base_rate = 80
    user_input = get_dow(prompt)

    SUN = (base_rate * 0.2) + base_rate
    MON = (base_rate * 0.2) + base_rate
    TUE = (base_rate * 0.2) + base_rate
    WED = (base_rate * 0.1) + base_rate
    THU = (base_rate * 0.1) + base_rate
    FRI = base_rate
    SAT = base_rate

    if user_input == 'SUN':
        base_rate = SUN
        return base_rate
    elif user_input == 'MON':
        base_rate =  MON
        return base_rate
    elif user_input == 'TUE':
        base_rate =  TUE
        return base_rate
    elif user_input == 'WED':
        base_rate =  WED
        return base_rate
    elif user_input == 'THU':
        base_rate =  THU
        return base_rate
    elif user_input == 'FRI':
        base_rate =  FRI
        return base_rate
    elif user_input == 'SAT':
        base_rate =  SAT
        return base_rate

if __name__ == "__main__": # Basically if the name of the module is equal to main


