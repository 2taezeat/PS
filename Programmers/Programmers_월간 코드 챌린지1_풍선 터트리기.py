def solution(a):
    minleft = a[0]
    minright = a[-1]
    result = [0 for _ in range(len(a))]
    result[0] = 1
    result[-1] = 1

    for i in range(1,len(a)-1):
        if a[i] < minleft:
            minleft = a[i]
            result[i] = 1

    for i in range(len(a)-2,0,-1):
        if a[i] < minright:
            minright = a[i]
            result[i] = 1
        
    return sum(result)


#print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))