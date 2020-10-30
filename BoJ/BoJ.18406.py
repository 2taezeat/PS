s = list(input())
l = s[:len(s)//2]
r = s[len(s)//2:]
ls = 0
rs = 0

for i in range(len(s)//2):
    ls = ls + int(l[i])

for i in range(len(s)//2):
    rs = rs + int(r[i])

if rs == ls:
    print("LUCKY")
else:
    print("READY")