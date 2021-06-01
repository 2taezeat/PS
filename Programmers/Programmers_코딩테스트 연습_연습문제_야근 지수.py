import heapq
def solution(n, works):
    answer = 0
    h = []
    for w in works:
        heapq.heappush(h,[-w,w])

    for i in range(n):
        v1,v2 = heapq.heappop(h)
        if v2 != 0 :
            v2 -= 1
            heapq.heappush(h,[-v2,v2])
        else:
            heapq.heappush(h,[-v2,v2])

    for (a,b) in h:
        answer += b**2

    return answer

print(solution( 4, [4,3,3] ))