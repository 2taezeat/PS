k = int(input())
l1 = []
for i in range(k):
    n = int(input())

    if n == 0:
        l1.pop()
    else:
        l1.append(n)

print(sum(l1))