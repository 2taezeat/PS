import heapq
def solution(n, works):
    answer = 0
    h = []
    for w in works:
        heapq.heappush(h,[-w,w])

    for i in range(n):
        heapq.heapify(h)
        if h[0][1] != 0 :
            h[0][1] -= 1
            h[0][0] += 1

    for (a,b) in h:
        answer += b**2

    return answer

print(solution( 4, [4,3,3] ))