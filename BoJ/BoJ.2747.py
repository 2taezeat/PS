l = [0,1]
for i in range(2,45):
    l.append(l[i-1]+l[i-2])
N = int(input())
print(l[N])