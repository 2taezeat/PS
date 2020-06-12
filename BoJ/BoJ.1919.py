s1 = input()
s2 = input()
s1_l = list(s1)
s2_l = list(s2)

a = [0]*26
b = [0]*26


for i in range(len(s1_l)):
    a[ord(s1_l[i]) -97] += 1

for i in range(len(s2_l)):
    b[ord(s2_l[i]) -97] += 1

sum1 = 0
for i in range(26):
    sum1 = sum1 + abs(a[i]-b[i])

print(sum1)