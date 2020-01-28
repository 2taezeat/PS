N = int(input())

dp = [[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,1] ]
array1 = [1,2,2,2,2,2,2,2,2,1]
dp.append(array1)

for i in range(3,101):
    array2 = []
    for j in range(10):  
        if j == 0 :
            array2.append( dp[i-1][j+1])

        if j == 9 :
            array2.append( dp[i-1][j-1] )

        if 0 < j < 9:
            array2.append( dp[i-1][j-1] + dp[i-1][j+1] )

    dp.append(array2)

result = []
for i in range(101):
    sum = 0
    for j in range(1,10):
        sum = sum + dp[i][j]
    sum = sum % 1000000000
    result.append(sum)

print(result[N])