a = int(input())
b = int(input())
c = int(input())

r = a*b*c
r = list(str(r))
nl = [0,0,0,0,0,0,0,0,0,0]

for i in r:
    nl[int(i)] = nl[int(i)] + 1

for j in nl:
    print(j)