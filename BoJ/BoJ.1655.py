import heapq # 최소 힙 모듈
import sys
input = sys.stdin.readline
n = int(input())
maxh = []
minh = []

for i in range(n):
    k = int(input())

    if len(minh) == len(maxh):
        heapq.heappush(maxh, [-k,k] )
    else:
        heapq.heappush(minh, [k,k] )


    if (minh != []) and (maxh[0][1] > minh[0][1]):
        t_max = heapq.heappop(maxh)[1]
        t_min = heapq.heappop(minh)[1]

        heapq.heappush(maxh, [-t_min, t_min])
        heapq.heappush(minh, [t_max, t_max])
    
    print(maxh[0][1])
