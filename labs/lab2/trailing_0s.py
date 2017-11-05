import sys
import math

# spend 19 min

def trail_1(num):
    trail = 0
    num = math.factorial(num)
    while num%10 == 0:
        num//=10
        trail+=1
    return trail

def trail_2(num):
    trail = 0
    num = math.factorial(num)
    num = str(num)
    while num[-(trail+1)]=='0':
        trail+=1
    return trail

def trail_3(num):
    trail = 0
    power = 0
    while num > 5**power:
        power+=1
    for i in range(1,power):
        trail+=num//(5**i)
    return trail

try:
    n = int(input('Input a nonnegative integetr:'))
    if n <0:
        raise Exception
except:
    print('Incorrect input, giving up.')
    sys.exit()
else:
    print('Computing the number of trailing 0s in',str(n)+'! by dividing by 10 for long enough:',trail_1(n))
    print('Computing the number of trailing 0s in',str(n)+'! by converting it into a string:',trail_2(n))
    print('Computing the number of trailing 0s in',str(n)+'! the smart way:',trail_3(n))
          
