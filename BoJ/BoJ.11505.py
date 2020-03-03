import sys
from math import ceil, log
input = sys.stdin.readline
N, M, K  = map(int,input().split())
t = []
k = ceil(log(N,2))
treesize = (2**(k+1)) -1
t = [ 1 ] * treesize
x = (2**k)
for i in range(x-1, N+x-1):
    t[i] = int(input())
for i in range( treesize - 2, 0 , -2 ):
    t[i//2] = t[i] * t[i+1]

# def func(a,b):
#     global t
#     if t[a] == 0 or t[b] == 0:
#         return 0
#     else:
#         if a == b:
#             return t[a] % 1000000007
        
#         if a % 2 == 0 and b % 2 == 1:
#             if b - a == 1:
#                 return (t[a] * t[b]) % 1000000007 
#             else:5
#                 return (t[a] * t[b] * func(a+1,b-1) ) % 1000000007

#         if a % 2 == 0 and b % 2 == 0:
#             return ( t[a] * func(a+1,b) ) % 1000000007

#         if a % 2 == 1 and b % 2 == 0:
#             return func(a//2, b//2-1) % 1000000007
        
#         if a % 2 == 1 and b % 2 == 1:
#             return ( t[b] * func(a,b-1) ) % 1000000007

for i in range(M+K):
    a, b, c = map(int,input().split())
    if a == 1: # 변화
        b = x + b - 2
        t[b] = c
        p = b
        while ( p > 0):

            if p % 2 == 0:
                t[p//2-1] = t[p] * t[p-1]
                p = p//2 -1
            else:
                t[p//2] = t[p] * t[p+1]
                p = p//2 

    elif a == 2:
        ra , rb = x - 2 + b, x + c - 2

        # if t[ra] == 0 or t[rb] == 0:
        #     print(0)
        # else:
        #     print( (func(ra,rb) % 1000000007) )

        result = 1 
        while (True):
            if ra == rb:
                result = t[ra] * result % 1000000007
                break
            
            else:
                if ra % 2 == 0 and rb % 2 == 1:
                    if rb - ra == 1:
                        result = result * t[ra//2] % 1000000007 
                        break
                    else:
                        result = result * (t[ra] * t[rb] ) % 1000000007
                        ra = ra + 1
                        rb = rb - 1
                        

                elif ra % 2 == 0 and rb % 2 == 0:
                    result = result *  t[ra] % 1000000007
                    ra = ra + 1
                    rb = rb

                elif ra % 2 == 1 and rb % 2 == 0:
                    ra = ra//2
                    rb = rb//2-1
                
                elif ra % 2 == 1 and rb % 2 == 1:
                    result = result * t[rb] % 1000000007        
                    ra = ra
                    rb = rb - 1

        print(result)