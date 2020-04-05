N = int(input())
c = 0
for i in range(1,N+1):
    p = 0
    if 0 < i < 10:
        c += 1
        continue
    else:
        i = list(str(i))
        d = int(i[1]) - int(i[0])

        for n in range(1,len(i)):
            if d != int(i[n]) - int(i[n-1]):
                p = 1
                break

    if p == 0:
        c += 1

print(c)