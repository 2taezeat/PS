t = 9
nl = []
for i in range(t):
    nl.append(int(input()))

m = max(nl)
print(m)
print(nl.index(m)+1)