def solution(answers):
    answer = []
    l1 = [1,2,3,4,5]
    l2 = [2, 1, 2, 3, 2, 4, 2, 5]
    l3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1,c2,c3 = 0,0,0
    i1,i2,i3 = 0,0,0
    for a in answers:
        if a == l1[i1]:
            c1 += 1
        if a == l2[i2]:
            c2 += 1
        if a == l3[i3]:
            c3 += 1
        i1 += 1
        i2 += 1
        i3 += 1
        if i1 == 5:
            i1 = 0
        if i2 == 8:
            i2 = 0
        if i3 == 10:
            i3 = 0

    tmp = [c1,c2,c3]
    max1 = max(c1,c2,c3)

    for i in range(3):
        if tmp[i] == max1:
            answer.append(i+1)

    answer.sort()
    return answer


print(solution([1,2,3,4,5]))