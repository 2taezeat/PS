import bisect
def solution(d, budget):
    d.sort() # 신청한 금액 리스트를 정렬
    c = 0 # count = 0
    sum1 = 0
    for i in d:
        sum1 = sum1 + i # 계속 신청한 금액을 더함.
        c = c + 1
        if sum1 > budget: #  신청한 금액의 합이 예산을 넘을 경우
            c = c - 1 # count에서 -1 를 함.
            break

    return c

