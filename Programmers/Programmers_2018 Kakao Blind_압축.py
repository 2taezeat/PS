from collections import defaultdict
def solution(msg):
    dic = defaultdict(int)
    answer = []
    j = 1
    for i in range(65,91):
        dic[chr(i)] = j
        j = j + 1

    z = 27
    i = 0
    while( i < len(msg) ):
        c = 1
        q = 0

        while(1):
            word = msg[i:i+c]
            if dic[word] == 0:
                dic[word] = z
                z = z + 1
                i = i+c-2
                break
            else:
                a = dic[word]

            if i + c == len(msg):
                q = 1
                break
            c = c + 1
            
        answer.append(a)
        if q == 1:
            break

        i = i + 1

    return answer


#print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
#print(solution("ABABABABABABABAB"))
