s = input()
l = [s]

for i in range(1,len(s)):
    l.append(s[i:])

a = sorted(l)
for c in a:
    print(c)