import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
nl = list(map(int,input().split()))
p, s, m, d = map(int,input().split())
oplist = []
t = p+s+m+d

for i in range(p):
    oplist.append('+')
for i in range(s):
    oplist.append('-')
for i in range(m):
    oplist.append('*')
for i in range(d):
    oplist.append('//')

alist = set(permutations(oplist, t)) # 중복 제거
answer = []
for a in alist:

    if a[0] == '+':
        r = nl[0] + nl[1]
    if a[0] == '-':
        r = nl[0] - nl[1]
    if a[0] == '*':
        r = nl[0] * nl[1]
    if a[0] == '//':
        if nl[0] < 0:
            r = - ( -nl[0] // nl[1] )
        else:
            r = nl[0] // nl[1]

    for i in range(1, t ):
        if a[i] == '+':
            r = r + nl[i+1]
        if a[i] == '-':
            r = r - nl[i+1]
        if a[i] == '*':
            r = r * nl[i+1]
        if a[i] == '//':
            if r < 0:
                r= -( (-r) // nl[i+1] )
            else:
                r = r // nl[i+1]

    answer.append(r)

print(max(answer))
print(min(answer))