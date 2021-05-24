def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)] # 삼각형 구조 만들기
    x, y = 0, -1 # 좌표값
    num = 1 # 대입 숫자
    for i in range(n): 
        for j in range(i,n): 
            if i % 3 == 0:
                x = x
                y = y + 1

            elif i % 3 == 1:
                x = x + 1
                y = y
            
            elif i % 3 == 2:
                x = x - 1
                y = y - 1

            answer[y][x] = num
            num += 1

    result = []
    for a in answer:
        for b in a:
            result.append(b)

    return result
    print(result)


print(solution(4))