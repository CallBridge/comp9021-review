# 7 min correct
def alpha(n):
    if n%26 == 0 and n>0:
        return 'Z'
    return chr(64+n%26)

def print_row(L,max_number):
    for i in L:
        print(alpha(i),end='')
    for i in range(len(L)-1,-1,-1):
        if L[i]!=max_number:
            print(alpha(L[i]),end='')
    print()

def triangle(scale):
    last_max = 0
    for i in range(scale):
        L = [n+last_max for n in range(1,i+2)]
        last_max = max(L)
        print(' '*(scale-i-1),end='')
        print_row(L,last_max)
        L.clear()



if __name__ == '__main__':
    try:
        scale = int(input('Enter a positive number: '))
    except:
        print('Error, try again.')
    else:
        triangle(scale)