# BFS
# FIFO (first in first out)
T = {1:[2,3],2:[4,5],3:[6,7],4:[8,9],5:[10,11],6:[12]}

class QueueError(Exception):
    def __init__(self,msg):
        print('QueueError:',msg)

class Queue:
    def __init__(self):
        self._data = []

    def append(self,datum):
        self._data.append(datum)

    def print_all(self):
        if not self._data or self._data==[]:
            raise QueueError('Queue is empty already.')
        for i in range(len(self._data)):
            print(self._data[i])

    def pop(self):
        if not self._data or self._data==[]:
            raise QueueError('Queue is empty already.')
        return self._data.pop()

    def is_empty(self):
        return self._data == []

def bfs(tree):
    queue = Queue()
    # add head node of the tree
    queue.append([1])
    while not queue.is_empty():
        queue.print_all()
        path = queue.pop()
        if path[-1] in tree:
            # left to right
            for i in tree[path[-1]]:
                queue.append(path+[i])

bfs(T)