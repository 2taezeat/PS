M = int(input())
N = int(input())
result = []
if M == 1:
    M = 2
    
for num in range(M,N+1):
    y = 0
    for i in range(2,num):
        if num % i == 0:
            y = 1
            break

    if y == 0:
        result.append(num)

if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)