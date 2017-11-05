# Written by KEQIAO QIAN

# time escaping: 6 min 38 sec


'''
    Decodes all multiplications of the form
    
    *  *  *
    x       *  *
    ----------
    *  *  *  *
    *  *  *
    ----------
    *  *  *  *
    
    such that the sum of all digits in all 4 columns is constant.
    '''


for x in range(100, 1_000):
    for y in range(10, 100):
        product0 = x*(y%10)
        product1 = x*(y//10)
        total = x*y
        the_sum = x%10+y%10+product0%10+total%10
        if the_sum !=x//10%10+y//10+product0//10%10+product1%10+total//10%10:
            continue
        if the_sum !=x//100+product0//100%10+product1//10%10+total//100%10:
            continue
        if the_sum !=product0//1_000+product1//100+total//1_000:
            continue
        print(f'{x} * {y} = {total}, all columns adding up to {the_sum}.')
