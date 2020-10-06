def balanced_index(p):
    count = 0 # '(' 의 갯수
    for i in range(len(p)):
        if p[i] == "(":
            count = count + 1
        else:
            count = count - 1
        
        if count == 0:
            return i

def check_proper(p):
    count = 0 # '(' 의 갯수
    for i in p:
        if i == "(":
            count = count + 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False

            count = count - 1

    return True

def solution(p):
    answer = ''
    if p == '':
        return answer

    if check_proper(p):
        return p

    idx = balanced_index(p)
    u = p[:idx+1] 
    v = p[idx+1:]

    if check_proper(u): # u가 올바른 문자열이라면
        a = solution(v)
        answer = u + a

    else: # u가 올바른 문자열이 아니라면
        answer = '('
        a = solution(v)
        answer = answer + a
        answer = answer + ')'
        u = list(u[1:-1])
 
        for i in range(len(u)):

            if u[i] == '(':
                u[i] = ')'

            else:
                u[i] = '('

        answer = answer + "".join(u)

    return answer

print('-------------')
print(solution("(()())()"))
print('-------------')
print(solution(")("))
print('-------------')
print(solution("()))((()"))
