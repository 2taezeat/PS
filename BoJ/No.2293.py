N, K = map(int,input().split())
array1 =[]
for i in range(N):
    a = int(input())
    array1.append(a)

array2 = [0 for i in range(K+1)] # [0,0,0,0,0,0,0,0,0,0,0] index : 0 ~ 10
array2.insert(0,1)
array3 = []

for i in range(1):
    for k in range(K+1):
        if array1[i] > k:
            v = array2[k]
        else:
            v = array2[k] + array3[k-array1[i]]

        array3.append(v)
dp = []
dp.append(array3)

for i in range(1,N):
    dplist1 = []
    for k in range(K+1):
        if array1[i] > k:
            v = dp[0][k]
        else:
            v = dp[0][k] + dplist1[k-array1[i]]

        dplist1.append(v)
 
    dp[0] = dplist1

print(dp[0][k])