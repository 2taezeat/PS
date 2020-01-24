N,K = map(int,input().split())
a = []
for i in range(N):
    m = int(input())
    a.append(m)

a.sort(reverse=True)

sum = 0
for j in range(N):
    result = K // a[j]
    sum = result + sum
    K = K % a[j]
    if K == 0:
        break

        
print(sum)