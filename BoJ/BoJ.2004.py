n, m = map(int,input().split())
def count2(x):
    c = 0
    while x != 0:
        x = x // 2
        c = c + x

    return c

def count5(x):
    c = 0
    while x != 0:
        x = x // 5
        c = c + x
        
    return c

c2 = count2(n) - (count2(m)+count2(n-m))
c5 = count5(n) - (count5(m)+count5(n-m))
print(min(c2,c5))


