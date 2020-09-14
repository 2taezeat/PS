def solution(array, com):
    answer = []

    for s in com:
        c = s
        i = c[0] 
        j = c[1] 
        k = c[2]

        nl = array[i-1:j]
        nl.sort()
    
        answer.append(nl[k-1])
      
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))