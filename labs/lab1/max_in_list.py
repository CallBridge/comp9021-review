from random import seed,randint
import sys
# 10min40sec too slow
try:
    s = int(input('Input a seed for the random number generator:'))
    num_of_elements = int(input('How many elements do you want to generate?'))
except:
    print('Error')

seed(s)
L = [randint(0, 99) for _ in range(num_of_elements)]
print('The list is:',L)

min_num, max_num = L[0], L[0]
for i in L:
    if min_num > i:
        min_num = i
    elif max_num < i:
        max_num = i

print('The maximum difference between largest and smallest values in this list is:',max_num-min_num)
print('Confirming with builtin operations:', max(L) - min(L))
# Eric Martin's Code
from random import seed, randint

# Prompts the user for a seed for the random number generator,
# and for a strictly positive number, nb_of_elements.
arg_for_seed = input('Input a seed for the random number generator: ')
try:
    arg_for_seed = int(arg_for_seed)
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
nb_of_elements = input('How many elements do you want to generate? ')
try:
    nb_of_elements = int(nb_of_elements)
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
# Generates a list of nb_of_elements random integers between 0 and 99.
seed(arg_for_seed)
L = [randint(0, 99) for _ in range(nb_of_elements)]
# Prints out the list, computes the maximum element of the list, and prints it out.
print('\nThe list is:', L)
max_element = 0
for e in L:
    if e > max_element:
        max_element = e
print('\nThe maximum number in this list is:', max_element)
# Of course there is an easier way; as so often, Python just makes it too easy!
print('Confirming with builtin operation:', max(L))
max = 0
min = 0
for i in L:
    if (i < min):
        min = i
    elif (i > max):
        max = i
print("The maximum difference between largest and smallest values in this list is", max - min, rep=': ')
print("Confirming with builtin operations: ", max(L) - min(L))
