s = input()
l1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in s:
    l1[ord(i)-97] = l1[ord(i)-97] + 1 

for j in l1:
    print(j,end=' ')