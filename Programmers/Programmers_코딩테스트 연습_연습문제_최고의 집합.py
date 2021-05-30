def solution(n, s):
    answer = []
    v = s // n
    S = (v+1) * n
    k = S - s
    if v == 0: return [-1]
    for i in range(n): answer.append(v+1)
    for i in range(k): answer[i] -= 1
    return answer