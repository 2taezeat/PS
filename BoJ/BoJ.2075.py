N = int(input())
arr1 = list(map(int,input().split()))

for i in range(N-1):
    a = list(map(int,input().split()))
    n = a + arr1

    n.sort(reverse=True)
    arr1 = n[:N]

print(arr1[-1])

