import sys
from math import ceil, log
input = sys.stdin.readline
N, M, K  = map(int,input().split())
t = []
k = ceil(log(N,2))
treesize = (2**(k+1)) -1
t = [ 0 for i in range(treesize)]
x = (2**k)
for i in range(x-1, N+x-1):
    t[i] = int(input())
for i in range( treesize - 2, 0 , -2 ):
    t[i//2] = t[i] + t[i+1]

def func(a,b):
    global t
    if a == b:
        return t[a]
    else:
        if a % 2 == 0 and b % 2 == 1:
            if b - a == 1:
                return t[a] + t[b] 
            else:
                return t[a] + t[b] + func(a+1,b-1) 

        if a % 2 == 0 and b % 2 == 0:
            return ( t[a] + func(a+1,b) )

        if a % 2 == 1 and b % 2 == 0:
            return func(a//2, b//2-1)
        
        if a % 2 == 1 and b % 2 == 1:
            return ( t[b] + func(a,b-1) )

for i in range(M+K):
    a, b, c = map(int,input().split())
    if a == 1: # 변화
        b = x + b - 2
        r = c - t[b]
        t[b] = c
        if b % 2 == 0:
            b = b//2 -1
        else:
            b = b//2 

        j = b
        while (j>=0):
            t[j] = t[j] + r
            if j % 2 == 0:
                j = j//2 -1
            else:
                j = j//2 

    elif a == 2:
        ra , rb = x - 2 + b, x + c - 2
        print( func(ra,rb) )