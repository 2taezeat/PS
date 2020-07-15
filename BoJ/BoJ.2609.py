from math import gcd

a, b = map(int,input().split())
g = gcd(a,b)
n = a*b // g

print(g)
print(n)