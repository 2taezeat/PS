import heapq # 최소 힙 모듈
import sys
input = sys.stdin.readline
N = int(input())
h = []

for i in range(N):
    x = int(input())

    if h == [] and x == 0 :
        print(0)

    elif x == 0:
        print( - (heapq.heappop(h)) )  
    else:
        heapq.heappush(h,-x)
