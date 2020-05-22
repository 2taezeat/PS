sl = []
for i in range(5):
    l = input()
    sl.append(l)
answer = ''
j = 0

while(j<15):

    for s in sl:
        answer = answer + s[j]
    
    for s2 in sl:
        if len(s2) <= j+1:
            sl.remove(s2)

    for s2 in sl:
        if len(s2) <= j+1:
            sl.remove(s2)

    for s2 in sl:
        if len(s2) <= j+1:
            sl.remove(s2)

    for s2 in sl:
        if len(s2) <= j+1:
            sl.remove(s2)
    
    j = j + 1

print(answer)
