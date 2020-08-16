from math import gcd
a, b = map(int,input().split())
c, d = map(int,input().split())

r = gcd(b,d)
l = b * d // r
x = l // b
y = l // d
a2 = x * a
c2 = y * c
n = a2 + c2

if l % n != 0:
    r = gcd(n,l)
    print(n//r,l//r)

else:
    p = l // n
    a = n
    b = l
    x = n // a
    y = l // a
    print(x,y)
