s1 = list(map(int,input().split()))
result = 1

while(1):
    count = 0
    for i in range(5):
        if result % s1[i] == 0:
            count += 1

    if count > 2:
        print(result)
        break

    result += 1