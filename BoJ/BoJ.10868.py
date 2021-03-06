import sys
from math import ceil, log
input = sys.stdin.readline

N , M  = map(int,input().split())
k = ceil(log(N,2))
treesize = (2**(k+1)) -1
t = [ 100001 for i in range(treesize)]
x = (2**k)

for i in range(x-1, N+x-1):
    t[i] = int(input())

for i in range( treesize - 2, 0 , -2 ):
    t[i//2] = min(t[i],t[i+1])

def func(a,b):
    global t
    if a == b:
        return t[a]
    else:
        if a % 2 == 0 and b % 2 == 1:
            if b - a == 1:
                return min( t[a] , t[b] )
            else:
                return min ( t[a], t[b], func(a+1,b-1) ) 

        if a % 2 == 0 and b % 2 == 0:
            return min ( t[a] , func(a+1,b) )

        if a % 2 == 1 and b % 2 == 0:
            return func(a//2, b//2-1)
        
        if a % 2 == 1 and b % 2 == 1:
            return min( t[b] ,func(a,b-1) )

for i in range(M):
    a , b = map(int,input().split())
    ra , rb = x - 2 + a, x + b - 2
    print(func(ra,rb))
