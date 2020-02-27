import sys
sys.setrecursionlimit(100000000)
a, b, c = map ( int, input().split())

def fun(x,n):
    global c
    if n == 0:
        return 1

    else:
        result = fun(x,n//2)
        
        if n % 2 == 0:
            return (result * result) % c
        else:
            return (result * result * x) % c
            
# (X*Y) % C = ( (X % C) * (Y % C) ) % C
print(fun(a,b))