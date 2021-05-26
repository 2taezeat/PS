def solution(brown, yellow):
    t = 0
    for x in range(1,2000000):
        y = ((brown-(2*x)+4) // 2)
        eq = x * y + 4 -2*(x+y)    
        #print(x,eq)
        if eq == yellow:
            t = x
            break

    y = ((brown-(2*t)+4) // 2)


    answer = [t,y]
    answer.sort(reverse=True)
    return answer



print(solution(24,24))