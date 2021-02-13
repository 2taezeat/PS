N = int(input())
d = [[],[],[],[],[],[],[],[],[],[]]
alp = [0] * 26
for i in range(N):
    l1 = input()
    length = len(l1)

    for j in range(length-1,-1,-1):
        d[j].insert(j,l1[length - j- 1])

i = 1
for a in d:
    for ch in a:
        alp[ord(ch)-65] = alp[ord(ch)-65] + (1*i)
    i = i * 10
alp.sort(reverse=True)
r = 9
sum1 = 0
for i in alp:
    sum1 = sum1 + i*r
    r = r - 1

print(sum1)