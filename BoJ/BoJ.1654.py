list1 = []
K, N = map(int,input().split())
for i in range(K):
    list1.append(int(input()))

left = 1
right = max(list1)
result = 0

while left <= right:
    mid = (left + right) // 2
    result = 0
    
    for l in list1:
        result = result + (l // mid)

    if result >= N:
        left = mid + 1

    else:
        right = mid - 1

print(right)