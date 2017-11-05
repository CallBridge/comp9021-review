import math

# 7 min

def get_divisors(num):
    L = [1]
    for i in range(2,round(math.sqrt(num))+1):
        if num%i==0:
            L.append(i)
            L.append(num//i)
    return L

def is_perfect(num):
    L = get_divisors(num)
    if sum(L)==num:
        return True
    return False

try:
    num_range = int(input('Input an integer: '))
except:
    print('Error.')
else:
    for n in range(6,num_range+1):
        if is_perfect(n):
            print(n,'is a perfect number.')
