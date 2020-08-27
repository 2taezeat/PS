n = int(input())
l1 = [500,100,50,10,5,1]
n = 1000 - n
c = 0
for i in l1:
    c = c + (n // i)
    n = n % i

print(c)