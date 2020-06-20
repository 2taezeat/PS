nl = [0]*31
for i in range(28):
    n= int(input())
    nl[n] = 1

cl = []
for i in range(1,31):
    if nl[i] == 0:
        cl.append(i)

print(min(cl))
print(max(cl))