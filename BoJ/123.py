import heapq # 최소 힙 모듈
import sys
import math
input = sys.stdin.readline
n = int(input())
h = []

for i in range(n):
    k = int(input())
    heapq.heappush(h,k)

        

    k = math.log2(i+2)
    k = math.floor(k)

    j = 2**k-2

    print('#',h[j])
