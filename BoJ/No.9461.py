N = int(input())
array2 = []

for i in range(N):
    a = int(input())
    array2.append(a)

array1 = [1,1,1,2,2]

for i in range(5,101):
    array1.append(array1[i-5] + array1[i-1])

for i in range(N):
    print(array1[array2[i]-1])