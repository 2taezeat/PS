def solution(s):
    zero_count = 0
    ghlttn = 0
    while(1):
        l = []
        ghlttn += 1
        for i in s:
            if i == '1':
                l.append(i)
            else:
                zero_count += 1

        c = len(l) 
        cc = bin(c)
        cc = cc[2:]

        if cc == '1':
            break
        s = cc
        
    return [ghlttn,zero_count]


print(solution("110010101001"))