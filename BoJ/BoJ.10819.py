from itertools import permutations
N = int(input())
arr1 = list(map(int,input().split()))
a = list(permutations(arr1))
dl = []
for arr in a:
    sum1 = 0

    for i in range(0,len(arr1)-1):
        sum1 = abs(arr[i+1]-arr[i]) + sum1
    dl.append(sum1)

print(max(dl))