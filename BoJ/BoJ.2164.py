from collections import deque
n = int(input())

l1 = deque()

for i in range(n,0,-1):
    l1.append(i)

while(1):
    
    if len(l1) == 1:
        break

    l1.pop()
    nxt = l1.pop()
    l1.appendleft(nxt)
    
print(l1[0])

