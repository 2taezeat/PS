import sys
N = int(sys.stdin.readline())
array1 = [ [-1, -1] ]

for i in range(N):
    s,f = map(int,sys.stdin.readline().split())
    array1.append([f,s])

list.sort(array1)

result = 1
k = 1
for m in range(2,N+1):
    if array1[m][1] >= array1[k][0]:
        result = result + 1
        k = m

print(result)
