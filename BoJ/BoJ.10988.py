s = input()
p = 1

for n in range(len(s)//2):

    if s[n] != s[-n-1]:
        p = 0
        break

print(p)
