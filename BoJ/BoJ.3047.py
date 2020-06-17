a1 = list(map(int,input().split()))
a1.sort()

s = input()
s = list(s)
d = []
d.append(['A',a1[0]])
d.append(['B',a1[1]])
d.append(['C',a1[2]])

for i in range(3):
    for j in range(3):
        if s[i] == d[j][0]:
            print(d[j][1], end= ' ')
