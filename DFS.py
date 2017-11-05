# DFS
# DFS use stack 'LIFO' property, which is last in first out
# So the last one stored in stack would be handle first
# define a Tree
T = {1:[2,3],2:[4,5],3:[6,7],4:[8,9],5:[10,11],6:[12]}

class StackError(Exception):
    def __init__(self,message):
        self.message = message
        print('StackError:',message)

class Stack:
    def __init__(self):
        self._data = []

    def peek_at_top(self):
        if not self._data:
            raise StackError('Stack is empty.')
        print(self._data[-1])

    def pop(self):
        if not self._data:
            raise StackError('Cannot pop from empty stack.')
        return self._data.pop()

    def push(self,datum):
        self._data.append(datum)

    def is_empty(self):
        return self._data==[]

def deepest_first_search(tree):
    stack = Stack()
    stack.push([1])
    while not stack.is_empty():
        path = stack.pop()
        print(path)
        # path like 1->2
        if path[-1] in tree:
            for child in reversed(tree[path[-1]]):
                stack.push(list(path)+[child])

deepest_first_search(T)
