x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())
x3, y3 = map(int,input().split())
x4 , y4 = 0, 0
xl = []
yl = []
xl.append(x1)
xl.append(x2)
xl.append(x3)
xl.sort()
yl.append(y1)
yl.append(y2)
yl.append(y3)
yl.sort()

for i in range(1,3):
    if i == 1:
        if xl[i-1] != xl[i]:
            x4 = xl[i-1]
            break
    else:
        if xl[i-1] != xl[i]:
            x4 = xl[i]
            break

for i in range(1,3):
    if i == 1:
        if yl[i-1] != yl[i]:
            y4 = yl[i-1]
            break
    else:
        if yl[i-1] != yl[i]:
            y4 = yl[i]
            break

print(x4, y4)