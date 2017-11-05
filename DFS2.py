
class StackError(Exception):
    def __init__(self,message):
        print('StackError:',message,end='.')

class Stack:
    def __init__(self):
        self._data = []

    def pop(self):
        if not self._data or self._data==[]:
            raise StackError('Cannot pop from an empty stack.')
        return self._data.pop()

    def print_peek(self):
        if not self._data or self._data==[]:
            raise StackError('Stack is empty already.')
        print(self._data[-1])

    def push(self,datum):
        self._data.append(datum)

    def is_empty(self):
        return self._data==[]

def dfs(tree):
    stack = Stack()
    # push head node of tree
    stack.push([1])
    while not stack.is_empty():
        stack.print_peek()
        path = stack.pop()
        if path[-1] in tree:
            # from left to right
            for i in reversed(tree[path[-1]]):
                stack.push(path+[i])

T = {1:[2,3],2:[4,5],3:[6,7],4:[8,9],5:[10,11],6:[12]}
dfs(T)