import sys
# 7min 14 sec
def get_solutions(available_digits_number,desired_number):
    if desired_number == 0:
        return 1
    elif desired_number<0:
        return 0
    if available_digits_number==0:
        return 0
    current_digit = available_digits_number%10
    available_digits_number//=10
    return get_solutions(available_digits_number,desired_number-current_digit)+get_solutions(available_digits_number,desired_number)




try:
    available_digits_number = int(input('Input a number that we will use as available digits: '))
    desired_number = int(input('Input a number that represents the desired sum: '))
except:
    print('Error, Exit.')
    sys.exit()
else:
    solution = get_solutions(available_digits_number,desired_number)
    if solution == 0:
        print('There is no solution.')
    elif solution == 1:
        print('There is 1 solution.')
    else:
        print('There are',solution,'solutions.')

