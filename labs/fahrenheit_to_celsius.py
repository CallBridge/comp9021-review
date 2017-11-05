'''
Prints out a conversion table of temperatures from Fahrenheit to Celsius degrees,
with the former ranging from 0 to 300 in steps of 20.
'''
# celsius = (fahreneit-32)*(5/9)
min_temperature = 0
max_temperature = 300
step = 20
# \t: A tab
print('Fahrenheit\Celsius')

for fahrenheit in range(min_temperature,max_temperature+step,step):
    print(f'fahrenheit:{fahrenheit:10d}\t celsius:,{5*(fahrenheit-32)/9:7.2f}')

# martin 's code
# Written by Eric Martin for COMP9021


'''
Prints out a conversion table of temperatures from Fahrenheit to Celsius degrees,
with the former ranging from 0 to 300 in steps of 20.
'''

min_temperature = 0
max_temperature = 300
step = 20
# \t: A tab
print('Fahrenheit\tCelsius')
# We let fahrenheit take the values
# - min_temperature
# - min_temperature + step
# - min_temperature + 2 * step
# - min_temperature + 3 * step
# ...
# up to the largest value smaller than max_temperature + step
for fahrenheit in range(min_temperature, max_temperature + step, step):
    celsius = 5 * (fahrenheit - 32) / 9
    # {:10d}:  fahrenheit as a decimal number in a field of width 10
    # {:7.1f}: celsius as a floating point number in a field of width 7
    #          with 1 digit after the decimal point
    print(f'{fahrenheit:10d}\t{celsius:7.1f}')

# notes:
'''
1. the using of f'{xxx:10d}'
formate string, in 3.6
思考： 期中考试的环境是3.5，怎么样实现 format化？
'''