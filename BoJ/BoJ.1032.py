n = int(input())
sl = []
for i in range(n):
    s1 = input()
    sl.append(s1)

l = len(sl[0])
answer = ''
c = 0

while( c<l ):
    l2 = []
    for j in range(n):
        l2.append(sl[j][c])
    
    set1 = set(l2)
    s_l = list(set1)

    if len(s_l) == 1:
        answer = answer + s_l[0]
    else:
        answer = answer + '?'

    c = c + 1

print(answer)