n = int(input())
l1 = []

for i in range(0,10000000):
    i = list(str(i))
    p = 0

    for m in range(1,len(i)):

        if i[m-1] <= i[m]:
            p = 1
            break

    if p == 0:
        # i = ''.join(i)
        # l1.append(int(i))
        l1.append(i)

    if len(l1) >= n:
        break

#print(l1)
a = ''.join(l1[-1])

print(int(a))