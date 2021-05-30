import math
def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        progresses[i] = int(math.ceil((100 - progresses[i]) / speeds[i]))

    i = 0
    while 1:
        stand = progresses[i]
        j = i
        count = 0
        while 1:
            if j == len(progresses):
                break

            if stand >= progresses[j]:
                j += 1
                count += 1
            else:
                break
        
        answer.append(count)
        i = j
        if i == len(progresses):
            break

    return answer


print(solution([93,30,55],[1,30,5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))