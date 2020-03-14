import math
A, B = map(int,input().split())
r = math.gcd(A,B)

for i in range(r):
    print(1,end='')
