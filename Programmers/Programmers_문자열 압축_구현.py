def solution(s):
    l1 = []
    ls = len(s)
    answer = []

    for i in range(1,ls+1):
        sl = []

        for j in range(0,ls,i):
            spl = s[j:j+i]
            sl.append(spl)
        
        l1.append(sl)
    
    for l in l1:
        count = 1
        result = ''
        for i in range( len(l) - 1 ):

            if l[i] == l[i+1]:
                count = count + 1
            else:
                if count == 1:
                    result = result + l[i]
                    count = 1
                else:
                    result = result + l[i] + str(count) 
                    count = 1
        
        if count == 1:
            result = result + l[-1]
            answer.append(len(result))
        else:
            result = result + l[-1] + str(count)
            answer.append(len(result))

    return min(answer)

s = 'aaaaaaaaaabbbbbbbbbb'
print(solution(s))