# 27 min 40 sec
def triangle(num):
    rows = yanghui(num)
    max_digits = len(str(max(rows[-1])))
    for row_index in range(len(rows)):
        for num_index in range(len(rows[row_index])):
            if num_index==0:
                print(' '*max_digits*(num-row_index),end='')
                print(rows[row_index][num_index],end='')
                continue
            print(' '*(2*max_digits-len(str(rows[row_index][num_index]))),end='')
            print(rows[row_index][num_index],end='')
        print()

def get_inside(L):
    ret = []
    for i in range(len(L)-1):
        ret.append(L[i]+L[i+1])
    return ret

def yanghui(num):
    L = []
    for i in range(num+1):
        if i == 0:
            L.append([1])
        elif i == 1:
            L.append([1,1])
        else:
            current_row = []
            current_row.append(1)
            last_row = L[-1]
            current_row.extend(get_inside(last_row))
            current_row.append(1)
            L.append(current_row)
    return L





if __name__ == '__main__':
    number = int(input('Enter a nonnegative number:'))
    triangle(number)