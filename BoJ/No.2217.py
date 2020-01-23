N = int(input())
a = []
for i in range(N):
    m = int(input())
    a.append(m)

a.sort(reverse=True)

M = a[0]

for i in range(1,N):
    newM = a[i]*(i+1)
    if M < newM:
        M = newM

print(M)