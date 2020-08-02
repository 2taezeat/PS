import itertools

def pal(word):
    return (word == word[::-1])

st = input()
s = list(st)

a = (list(map(''.join, itertools.permutations(s))))

answer = st
p = 0
for i in a:
    result = pal(i)

    if result == True:
        answer = min(answer,i)
        p = 1
    else:
        continue

if p == 0:
    print("I'm Sorry Hansoo")
else:
    print(answer)