import heapq
n = int(input())
l1 = []
for i in range(n):
    heapq.heappush(l1,int(input()))

r = 0
if n == 1:
    print(0)
elif n == 2:
    print(l1[0]+l1[1])
    
else:
    for i in range(n-1):
        a = heapq.heappop(l1)
        b = heapq.heappop(l1)
        r = a + b +r

        heapq.heappush(l1,a+b)

    print(r)