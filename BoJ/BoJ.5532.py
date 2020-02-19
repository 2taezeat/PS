import math
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

rnrdj = A / C
tngkr = B / D

m = max(rnrdj,tngkr)
m1 = math.ceil(m)

print(L-m1)