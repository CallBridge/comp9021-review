from random import shuffle
# shuffle : rerder all elements randomly

# bubble sort o(n^2)
def bubble_sort(L):
    if len(L)==0:
        return

    length = len(L)
    for i in range(length):
        for j in range(length-i-1):
            if L[j]>L[j+1]:
                # swap
                L[j],L[j+1]=L[j+1],L[j]
    return L

# select sort o(n^2)
def select_sort(L):
    if len(L)==0:
        return

    for i in range(1,len(L)):
        while L[i]<L[i-1] and i>0:
            # swap til beginning while necessary
            L[i],L[i-1]=L[i-1],L[i]
            i-=1
    return L

# insert sort o(n^2)
def insert_sort(L):
    if len(L)==0:
        return

    for i in range(1,len(L)):
        # compare with elements supposed sorted list L'
        j = i
        while L[j-1]>L[j]:
            L[j-1],L[j]=L[j],L[j-1]
    return L

# merge sort
def merge_sort(L):
    L1 = [None]*len(L)
    return _mergesort(L,L1,0,len(L))

def _mergesort(output_list, input_list, start, end):
    # recursively
    if end - start<=1:
        return
    _mergesort(input_list, output_list, start, (start + end) // 2)
    _mergesort(input_list, output_list, (start + end) // 2, end)
    # sort
    i0 = start
    i1 = (start + end) //2
    i = start
    while i0< (start + end) //2 and i1< end:
        print(input_list,i0,start,end)
        if input_list[i0] < input_list[i1]:
            output_list[i] = input_list[i0]
            i += 1
            i0 += 1
            print('+1')
        else:
            output_list[i] = input_list[i1]
            i += 1
            i1 += 1
    if i0 < (start + end) // 2:
        output_list[i:] = input_list[i0: (start+end)//2]
    else:
        output_list[i:]= input_list[i1:end]
    return output_list

L=[1,3,5,4,2]
print('bubble sort:',bubble_sort(L))
print('select sort:',select_sort(L))
print('insert sort:',insert_sort(L))
print('merge sort:',merge_sort(L))

def batcher_sort(L):
    pass