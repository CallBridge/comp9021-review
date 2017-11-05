import sys
#12 min 59 sec
def get_solutions(depth,available_digits,desired_number,current_number=0):

    if current_number>desired_number:
        return 0
    elif current_number==desired_number:
        return 1
    if depth==len(available_digits):
        return 0
    return get_solutions(depth+1,available_digits,desired_number,current_number+available_digits[depth])+get_solutions(depth+1,available_digits,desired_number,current_number)

def get_digits(num):
    L = []
    while num!=0:
        L.append(num%10)
        num//=10
    return L

try:
    available_digits_number = int(input('Input a number that we will use as available digits: '))
    desired_number = int(input('Input a number that represents the desired sum: '))
except:
    print('Error, Exit.')
    sys.exit()
else:
    available_digits = get_digits(available_digits_number)
    solution = get_solutions(0,available_digits,desired_number)
    if solution == 0:
        print('There is no solution.')
    elif solution == 1:
        print('There is 1 solution.')
    else:
        print('There are',solution,'solutions.')

