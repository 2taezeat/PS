N = input()
a = []
for i in N:
    a.append(int(i))

answer = 200
c0,c1,c2,c8 = 0,0,0,0


for i in a:
    if (i != 2) and (i != 0) and (i != 1) and (i != 8):
        answer = 0
        break
    if i == 0:
        c0 = c0 + 1
    if i == 1:
        c1 = c1 + 1
    if i == 2:
        c2 = c2 + 1
    if i == 8:
        c8 = c8 + 1

    if c0 and c1 and c2 and c8 > 0:
        answer = 2
        if c0 == c1 == c2 == c8:
            answer = 8
    else:
        answer = 1




print(answer)