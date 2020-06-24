s = input()
s1 = list(s)
l1 = [-1]*26

for i in range(len(s1)):
    a = ord(s1[i])-97
    if l1[a] == -1:
        l1[a] = i

for j in l1:
    print(j, end=' ')