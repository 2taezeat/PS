n = int(input())
sl = []
for i in range(n):
    name = list(input())
    sl.append(name[0])

setsl = list(set(sl))
answer = []
for i in range(len(setsl)):
    c = 0
    for j in range(len(sl)):

        if setsl[i] == sl[j]:
            c = c + 1
    answer.append((setsl[i],c))
answer.sort()

result = []
for i in range(len(answer)):
    if answer[i][1] >= 5:
        result.append(answer[i][0])

if result == []:
    print('PREDAJA')
else:
    for r in result:
        print(r,end='')
    