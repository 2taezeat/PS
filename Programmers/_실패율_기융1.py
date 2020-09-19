def solution(N, stages):
    count = [0] * (N+2) # N스테이지인 경우 N+1 스테이지까지 존재하므로
    for i in stages:
        count[i] += 1 # 계수 정렬
    
    total = len(stages)
    result = []
    for index, i in enumerate(count):
        if i != 0:
            fail_rate = i / total

            if index != N+1:
                result.append([fail_rate, index])
                total -= i
        else:
            if index != 0 and index != N+1:
                result.append([0,index])
                
    result.sort(key=lambda x: x[0], reverse=True)
    return list(map(lambda x: x[1], result)) # 배열의 두번째 요소를 표시하기 위함.


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N,stages))