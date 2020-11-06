def solution(s):
    l1 = []
    ls = len(s)
    answer = []
    # 문자열을 1,2,3 ... ls 까지로 쪼개서 l1리스트에 추가.
    for i in range(1,ls+1):
        sl = []

        for j in range(0,ls,i):
            spl = s[j:j+i]
            sl.append(spl)
        
        l1.append(sl)

    for l in l1:
        count = 1
        result = '' # 빈문자열 선언
        for i in range( len(l) - 1 ):

            if l[i] == l[i+1]: # 다음 문자열과 현재 문자열이 같으면,
                count = count + 1 # count + 1
            else: # 다음 문자열과 현재 문자열이 같지 않다면,
                if count == 1: # 그리고 count가 1이면
                    result = result + l[i] #기존 문자열에 현재 문자열 (기존 문자열과 다른) 추가, count값이 1이면 추가하지 않음.
                    count = 1 # count를 1로 초기화
                else: # 그리고 count가 1이 아니면
                    result = result + l[i] + str(count) #기존 문자열에 현재 문자열 (기존 문자열과 다른) 추가, 그리고 count값도 추가.
                    count = 1 # count를 1로 초기화
        
        # result에 l의 마지막 원소 추가를 추가한다. 이때 위에와 마찬가지로 count가 1일때와 아닐때를 나눈다.
        if count == 1:
            result = result + l[-1]
        else:
            result = result + l[-1] + str(count)

        answer.append(len(result)) # answer리스트에 result의 길이 추가
        #print(result)
    return min(answer) # answer리스트에서 가장 작은 값을 return 



s = 'aaaaaaaaaabbbbbbbbbb'
print(solution(s))