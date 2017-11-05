import sys

def merging(first,second,third):
    # solution 1
    # generalise it into len(third string) = len(first+second)
    if len(first)==len(second)+len(third):
        return 0 if execute_merge(second,third,first) else -1
    elif len(second)==len(first)+len(third):
        return 1 if execute_merge(first,third,second) else -1
    elif len(third)==len(second)+len(first):
        return 2 if execute_merge(first,second,third) else -1
    else:
        return -1



def try_execute(first,second,third):
    last_index=0
    while first!='':
        try:
            char = first[0]
            first=first[1:]
            index = third.index(char)
            third=third[:index]+third[index+1:]
        except:
            return False
    else:
        if third==second:
            return True
        else:
            return False

def execute_merge(first,second,third):
    # solution 1
    return try_execute(first,second,third) or try_execute(second,first,third)




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