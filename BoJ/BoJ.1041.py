import sys
N = int(sys.stdin.readline())
l1 = input().split()

a = []
for i in l1:
    a.append(int(i))

a3 = a[0] + a[1] + a[2]
for i in range(6):
    for j in range(i+1,6):
        for k in range(j + 1, 6):
            if (i + j == 5) or (i + k == 5) or ( j + k == 5):
                continue
            else:
                sa3 = a[i] + a[j] + a[k]
                a3 = min(a3, sa3)

a2 = a[0] + a[1]
for i in range(6):
    for j in range(i+1,6):
        if (i ==0 and j ==5) or (i ==1 and j==4) or (i==2 and j==3):
            continue
        else:
            sa2 = a[i] + a[j]
            a2 = min(a2,sa2)

a1 = min(a)
result = 0

if N == 1:
    result = sum(a) - max(a)
if N > 1:
    r3 = a3*4
    r2 = ((N-2)*4 + (N-1)*4) * a2
    r1 = ((N-1)*(N-2)*4 + (N-2)*(N-2) ) * a1

    result = r3 + r2 + r1


print(result)
