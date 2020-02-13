N = int(input())
array1 = [0,1]
for i in range(2,N+1):
    array1.append(  array1[i-1] + array1[i-2] )

print(array1[N])