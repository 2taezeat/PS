S = list(input())
Slen = len(S)
result = 0
for i in range(Slen+1):
    ss = []
    ss.extend(S)
    c = 0
    for j in range(i-1,-1,-1):
        ss.append(S[j])

    sslen = len(ss)  
    for k in range(sslen // 2): # 팰린드롬 확인
        if ss[k] != ss[-k-1]:
            c = -1
            break

    if c == 0:
        result = sslen
        break
    
print(result)