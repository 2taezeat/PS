from collections import deque
def solution(priorities, location):
    list1 = deque()
    i = 0
    for p in priorities:
        list1.append((p,i))
        i += 1
    answer = 0
    j = 0
    while list1:
        maxv = max(list1)[0]
        (a,b) = list1.popleft()
        if a < maxv:
            list1.append((a,b))
        else:
            j += 1
            if b == location:
                answer = j
                break
    
    return answer


print(solution([2,1,3,2],2))
print(solution([1, 1, 9, 1, 1, 1],0))