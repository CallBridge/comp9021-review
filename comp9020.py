import math
def expection(n,top):
    if n == 0:
        return 0
    return 5*probability(n,top)+8*probability(n,top)+expection(n-1,top)

def probability(n,top):
    ret = 1
    duration = top-n+1
    for i in range(duration):
        ret /= (top-i)
    return ret

def get_factorial(mul):
    for i in range(1,100):
        for j in range(i,10000):
            if abs(mul*i-j)<0.0000001:
                return (j,r'/',i)

print(get_factorial(expection(4,4)))



