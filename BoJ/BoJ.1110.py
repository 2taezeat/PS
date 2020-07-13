n = int(input())
N = n
k = 1
while(k < 1000000):
    sn = str(n)
    ln = list(sn)
    sum1 = 0

    for i in ln:
        sum1 = sum1 + int(i)

    sum1 = list(str(sum1))
    m = ln[-1] + sum1[-1]
    m = int(m)

    if m == N:
        break
    else:
        n = m
    
    k = k + 1

print(k)

