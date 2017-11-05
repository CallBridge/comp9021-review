import math

# 14 min 47 sec

def is_prime(n):
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def get_intervals(n,L=[]):
    if len(L)==n:
        return L
    if L ==[]:
        L.append(0)
    else:
        L.append(L[-1]+len(L)*2)
    return get_intervals(n,L)

def is_consecutive_prime(n):
    intervals = get_intervals(6)
    for i in range(intervals[-1]):
        if i in intervals and not is_prime(n+i):
            return False
        if i not in intervals and is_prime(n+i):
            return False
    return True

intervals = get_intervals(6)
for i in range(10_001,100_000,2):
    if is_consecutive_prime(i):
        for j in range(5):
            print(i+intervals[j],end='  ')
        print(i+intervals[j+1])
