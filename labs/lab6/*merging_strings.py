import sys

def merging(first,second,third):
    if len(first)==len(second)+len(third):
        return 0 if execute_merge(second,third,first) else -1
    elif len(second)==len(first)+len(third):
        return 1 if execute_merge(first,third,second) else -1
    elif len(third)==len(second)+len(first):
        return 2 if execute_merge(first,second,third) else -1
    else:
        return -1

def execute_merge(first,second,third,last_index=0):
    # check if third can come from [first and second merged]
    # return boolean
    ret = False
    if len(third)==len(first):
        if third==first:
            return True
        else:
            return False
    if second[-1] in third:
        for s in range(len(third)):
            if third[s] == second[-1]:
                ret = ret or execute_merge(first,second[:-1],third[:s]+third[s+1:],s)
    else:
        return False

    return ret



try:
    first_string = input('Please input the first string: ')
    second_string = input('Please input the second string: ')
    third_string = input('Please input the third string: ')
except:
    print('Error.')
    sys.exit()
else:
    status = merging(first_string,second_string,third_string)
    if status == 0:
        print('The first string can be obtained by merging the other two.')
    elif status == 1:
        print('The second string can be obtained by merging the other two.')
    elif status == 2:
        print('The third string can be obtained by merging the other two.')
    else:
        print('No solution.')