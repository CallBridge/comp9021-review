import sys
# 132426 48
def get_solutions(available_digits_number,target_product):
    if available_digits_number==0:
        if target_product == 1:
            return 1
        else:
            return 0
    elif target_product<0:
        return 0
    if target_product%(available_digits_number%10)==0:
        return get_solutions(available_digits_number//10,target_product//(available_digits_number%10))+get_solutions(available_digits_number//10,target_product)
    return get_solutions(available_digits_number//10,target_product)

# 漏掉了1的所有情况
def get_solutions111(available_digits_number,target_product):
    if target_product == 1:
        return 1
    if available_digits_number==0:
        return 0
    elif target_product<0:
        return 0
    if target_product%(available_digits_number%10)==0:
        return get_solutions(available_digits_number//10,target_product//(available_digits_number%10))+get_solutions(available_digits_number//10,target_product)
    return get_solutions(available_digits_number//10,target_product)



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

