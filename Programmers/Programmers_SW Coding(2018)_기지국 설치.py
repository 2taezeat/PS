import math
def solution(n, stations, w):
    answer = 0
    visit = []

    # 좌표1 ~ 첫번째 안테나 사이의 전파가 안통하는 구간
    if stations[0]- 1 - w - 1 >= 0:
        visit.append([0, stations[0]-w-2])

    # 첫번째 안테나 ~ 마지막 안테나 사이의 전파가 안통하는 구간
    for i in range(len(stations) - 1):
        start = stations[i]-1 + w + 1
        end = stations[i+1]-1 - w - 1

        if start <= end:
            visit.append([start, end])

    # 마지막 안테나 ~ 좌표n 까지 전파가 안통하는 구간
    if stations[-1] + w + 1 - 1<= n - 1:
        visit.append([stations[-1] + w, n-1])
    
    for (a,b) in visit:
        t = b - a + 1
        r = math.ceil(t / (2*w+1))
        answer += r
        
    return answer

print(solution(11,[4,11],1))
#print(solution(11,[1],1))
#print(solution(11,[11],1))
#print(solution(11,[1,4,11],1))