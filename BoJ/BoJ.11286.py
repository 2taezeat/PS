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
        r = heapq.heappop(h)
        print( r[1] ) 
    else:
        heapq.heappush(h, (abs(x),x) )

# * heap을 tuple로 구성했을때 맨 앞 숫자만 가지고 정렬함.
# 그 후 [0] 요소가 같을시, [1] 요소로 힙을 정렬,결정함.