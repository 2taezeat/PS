N = input().split()
l1 = N[0]

OL = []
for i in l1:
    OL.append(int(i))

def check(n):
    if n == -1:
        return n
    if n == 0:
        result2 = ''
        for i in OL:
            i = str(i)
            result2 = i + result2
        return result2

result = -1
sum = 0
for i in OL:
    sum = sum + i
    if i == 0:
        result = 0

OL.sort()

if sum % 3 !=0:
    result = -1

a = check(result)
print(int(a))
