L = [1,2,3,4,5,6,7,8,9]

# find all possible configurations using 1,2,3,4,5,6,7,8,9 to 100
# operator would use from '' '+' '-'

# The expected output is (the ordering could be di erent):
#  1 + 23 - 4 + 5 + 6 + 78 - 9 = 100
#  123 - 4 - 5 - 6 - 7 + 8 - 9 = 100
#  123 + 45 - 67 + 8 - 9 = 100
#  123 + 4 - 5 + 67 - 89 = 100
#  12 + 3 + 4 + 5 - 6 - 7 + 89 = 100
#  123 - 45 - 67 + 89 = 100
#  12 - 3 - 4 + 5 - 6 + 7 + 89 = 100
#  1 + 2 + 34 - 5 + 67 - 8 + 9 = 100
#  1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 = 100
# -1 + 2 - 3 + 4 + 5 + 6 + 78 + 9 = 100
#  12 + 3 - 4 + 5 + 67 + 8 + 9 = 100
#  1 + 23 - 4 + 56 + 7 + 8 + 9 = 100

results = []
queue=[]
#BFS solution
queue.append(['+'])
queue.append(['-'])
queue.append([None])
while len(queue[0]) != 9:

    cp = queue.copy()
    queue.clear()
    for path in cp:
        #merge
        queue.append(path+[None])
        #plus
        queue.append(path+['+'])
        #minus
        queue.append(path+['-'])

for operator_set in queue:
    string_of_formula=''
    for i,op in enumerate(operator_set):
        if op:
            string_of_formula+=op
        string_of_formula+=str(L[i])
    else:
        if eval(string_of_formula) == 100:
            results.append(string_of_formula)

for i in results:
    print(i)





