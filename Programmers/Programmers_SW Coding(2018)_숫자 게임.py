def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)

    for i in range(len(A)):
        flag = False
        sta = A[i]
        for j in range(len(B)):
            if sta < B[j]:
                sta = B[j]
                flag = True
            else:
                break

        if flag == True:
            answer += 1
            B.remove(sta)

    return answer