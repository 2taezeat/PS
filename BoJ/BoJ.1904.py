N = int(input())

def f1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return f1(n-1) + f1(n-2)

a = [1,2]

for i in range(2,N):
    a.append(a[i-2]%15746+ a[i-1]%15746)

print(a[N-1]%15746)
