# last in frist out , LIFO
#  책상 위에 쌓여 있는 책
import sys
input = sys.stdin.readline
class Stack(object):
    def __init__(self):
        self.items = []

    def empty(self):
        if self.items == []:
            return 1
        else:
            return 0
        
    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.items == []:
            return -1
        else:
            value = self.items.pop()
            return value

    def size(self):
        return len(self.items)

    def top(self):
        if self.items != []:
            return self.items[-1]
        else:
            return -1 
            
    def __repr__(self):
        return repr(self.items)

N = int(input())
stack1 = Stack()

for i in range(N):
    a = list(input().split())
    
    if a[0] == 'push':
        stack1.push(a[1])

    if a[0] == 'pop':
        print(stack1.pop())

    if a[0] == 'size':
        print(stack1.size())

    if a[0] == 'empty':
        print(stack1.empty())

    if a[0] == 'top':   
        print(stack1.top())