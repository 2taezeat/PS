from collections import deque
import copy
def check(inputString):
    rhkfgh = []

    if ( inputString[0] == ')' or inputString[0] == '}' or inputString[0] == ']' ):
        return False

    for i in range(len(inputString)):
        if inputString[i] == '(':
            rhkfgh.append(')')
        elif inputString[i] == '{':
            rhkfgh.append('}')
        elif inputString[i] == '[':
            rhkfgh.append(']')

        if ( inputString[i] == ')' or inputString[i] == '}' or inputString[i] == ']')  and rhkfgh ==[]:
            return False

        if ( inputString[i] == ')' or inputString[i] == '}' or inputString[i] == ']'  ):
            if rhkfgh != []:

                if rhkfgh[-1] == inputString[i]:
                    rhkfgh.pop()
                
                elif rhkfgh[-1] != inputString[i]:
                    return False

    if rhkfgh != []:
        return False

    return True

def solution(s):

    q = deque()
    for ss in s:
        q.append(ss)

    answer = 0
    for i in range(len(s)):
        semi_q = copy.deepcopy(q)
        for _ in range(i):
            a = semi_q.popleft()
            semi_q.append(a)
        
        if check(semi_q):
            answer += 1

    return answer


print(solution("[](){}"))