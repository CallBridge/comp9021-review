# 17 min 48 sec
import math
def get_squares(max_num):
    ret = []
    top = math.ceil(math.sqrt(max_num))
    for i in range(top+1):
        ret.append(i*i)
    return ret

def varify(n):
    for i in range(math.ceil(math.sqrt(n//2))+1):
        if (n-squares[i]) in squares:
            current_solution.append((i,squares.index(n-squares[i])))
            return True
    return False

def is_valid(num):
    for i in range(3):
        if varify(num+i):
            pass
        else:
            return False
    return True

squares = get_squares(1000)
current_solution = []
for num in range(100,998):
    if is_valid(num):
        print((num, num+1, num+2),'(equal to', '('+str(current_solution[0][0])+'^2+'+str(current_solution[0][1])+'^2, '+str(current_solution[1][0])+'^2+'+str(current_solution[1][1])+'^2, '+str(current_solution[2][0])+'^2+'+str(current_solution[2][1])+'^2))','is a solution.')
        current_solution.clear()

