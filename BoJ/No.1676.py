N = int(input())

def f(n):
    if n==0:
        return 1
    return n*f(n-1)


#print(f(N))


count = 0
for i in range(1,N+1):
    if i % 5 ==0:
        count = count + 1
    if i % 25 ==0:
        count = count + 1
    if i % 125 ==0:
        count = count + 1

print(count)