# 15 min
# Martin's solution
# https://echo360.org.au/lesson/G_c86c6425-7f42-405b-b649-360a005b8452_3d58217d-e191-412e-982b-30c0eed13205_2017-10-09T15:05:00.000_2017-10-09T15:55:00.000/classroom#sortDirection=desc
# 37 min start
def longest_path(candidates):
    L = [0]*len(candidates)
    length = [0]*len(L)
    #transfer to asc ii
    for i in range(len(candidates)):
        L[i] = ord(candidates[i])
    # record the value
    for i in range(len(L)):
        num = L[i]
        while num in L:
            num+=1
            length[i]+=1
    # find max path
    max_length = max(length)
    start_letter = 'z'
    for i in range(len(L)):
        current_length = 0
        num=L[i]
        while num in L:
            num+=1
            current_length+=1
        if current_length == max_length\
                and ord(start_letter)>L[i]:
            start_letter = chr(L[i])
    ret = [chr(ord(start_letter)+i) for i in range(max_length)]
    return ''.join(ret)



try:
    letters = input('Please input a string of lowercase letters: ')
    print('The solution is:',longest_path(letters))
except:
    print('Error.')