# 시간초과, 테스트케이스 6번 실패
import math
def solution(w,h):
    answer = 0
    for i in range(w):
        answer += math.floor((h/w) * i)

    return answer * 2

print(solution(8,12))
