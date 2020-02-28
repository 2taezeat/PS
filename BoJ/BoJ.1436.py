N = int(input())
a = []
c = 0
for i in range(666,2667000):
    if '666' in str(i):
        a.append(i)
        c = c + 1

    if c == N:
        break    

print(a[N-1])