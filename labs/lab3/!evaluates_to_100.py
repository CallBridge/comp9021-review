L = [1,2,3,4,5,6,7,8,9]

def evaluate(depth,total,target,symbols=[]):
    if depth>=8:
        return
    if total == target:
        print('- - -'*10)
        print(total)
        print(depth)
        print(symbols)
        for i in range(len(symbols)):
            if symbols[i] != '':
                print(symbols[i],L[i],end='')
            else:
                print(L[i],end='')
        print('= 100')
        return

    # positive
    t1 = total+L[depth]
    s1 = symbols[:]
    s1.append('+')

    # negative
    t2 = total-L[depth]
    s2 = symbols[:]
    s2.append('-')
    # no symbol
    t3 = 0
    s3 = None
    if len(symbols)==0:
        t3 = total + L[depth - 1] * 9 + L[depth]
    elif symbols[-1]=='-':
        t3 = total-L[depth-1]*9-L[depth]
    elif symbols[-1]=='+':
        t3 = total + L[depth - 1]*9 + L[depth]
    else:
        t3 = total
        digit_counter = 0
        # forget the first none symbol
        for i in range(len(symbols) - 1, 0, -1):
            if symbols[i] == '':
                digit_counter += 1
        if symbols[depth-digit_counter-1]=='-':
            for i in range(digit_counter, 0, -1):
                t3 = total - L[depth-i]*(10**i-1)
            t3 = total - L[depth]
        else:
            for i in range(digit_counter, 0, -1):
                t3 = total + L[depth-i]*(10**i-1)
            t3 = total + L[depth]
    s3 = symbols[:]
    s3.append('')
    evaluate(depth + 1, t1, target, s1)
    evaluate(depth + 1, t2, target, s2)
    evaluate(depth + 1, t3, target, s3)

evaluate(0,0,100)


