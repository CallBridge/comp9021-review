from random import seed,randint
import sys
from math import sqrt
'''
12min14sec too slow!
'''
try:
    random_seed = int(input('Input a seed for the random number generator:'))
    nb_of_elements = int(input('How many elements do you want to generate?'))
except:
    sys.exit()

seed(random_seed)
L = [randint(-50,50) for _ in range(nb_of_elements)]
mean = 0.0
median = 0.0
standard_deviation = 0.0
# sort L
L = sorted(L)
mean = sum(L)/nb_of_elements
median = L[nb_of_elements//2]
for i in L:
    standard_deviation+=(i-mean)**2
standard_deviation/=nb_of_elements
print('The mean is',round(mean,2))
print('The median is',round(median,2))
print('The standard deviation is',round(sqrt(standard_deviation),2))

