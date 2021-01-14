n = int(input())
s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))

s1.sort(reverse=True)
s2.sort()
sum1 = 0 
for i in range(n):
    sum1 = sum1 + s1[i]*s2[i]

print(sum1)