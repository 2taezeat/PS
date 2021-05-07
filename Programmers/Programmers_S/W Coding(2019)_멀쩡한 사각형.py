import math
def solution(w,h):
    answer = 0
    for i in range(w):
        answer += math.floor((h/w) * i)

    return answer * 2



print(solution(8,12))
