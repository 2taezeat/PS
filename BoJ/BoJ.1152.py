s = input()
s1 = s.split(' ')
c = 0

for i in range(len(s1)):
    if s1[i] != '':
        c = c + 1

print(c)
