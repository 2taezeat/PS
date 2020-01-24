n = int(input())
list1 = input().split()

for j in range(0,n):
    list1[j] = int(list1[j])

answer = []

for a in range(0,n):
    d = 0
    if a == 0:
        answer.append(list1[a])
        continue

    for i in answer:
        d = d + i

    answer.append(list1[a]*(a+1) - d)

for b in answer:
    print(b, end= ' ')