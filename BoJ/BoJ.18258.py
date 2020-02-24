# FIFO
# 롤러코스터의 줄
# 스택 2개로 구현, 시간 단축
import sys
class Queue():
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def empty(self):
        if self.in_stack == [] and self.out_stack == []:
            return 1
        else:
            return 0

    def push(self, value):
        self.in_stack.append(value)

    def pop(self):
        if self.in_stack == [] and self.out_stack == []:
            return -1

        if not self.out_stack:
            self._transfer()

        if self.out_stack:
            return self.out_stack.pop()

    def size(self):
        return ( len(self.in_stack) + len(self.out_stack) )

    def front(self):
        if self.in_stack == [] and self.out_stack == []:
            return -1

        if not self.out_stack:
            self._transfer()

        if self.out_stack:
            return self.out_stack[-1]

    def back(self):
        if self.in_stack == [] and self.out_stack == []:
            return -1

        if self.in_stack != []:
            return self.in_stack[-1]
        else:
            if not self.out_stack:
                self._transfer()

            if self.out_stack:
                return self.out_stack[0]

N = int( sys.stdin.readline().strip() )
queue1 = Queue()
for i in range(N):
    a = sys.stdin.readline().strip()
    
    if a == 'pop':
        print(queue1.pop())

    elif a == 'size':
        print(queue1.size())

    elif a == 'empty':
        print(queue1.empty())

    elif a == 'front':   
        print(queue1.front())

    elif a == 'back':   
        print(queue1.back())

    else:
        c,d = a.split()
        if c == 'push':
            queue1.push(int(d))