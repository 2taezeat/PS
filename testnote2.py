from collections import deque
import heapq
def solution(n, k, cmd):
    delete_list = []
    q = [] ##
    K = k
    for i in range(n):
        q.append(i)

    for i in range(len(cmd)):
        if cmd[i][0] == 'D':
            #a = cmd[i][2:]
            K = K + int(cmd[i][2:])

        elif cmd[i][0] == 'U':
            K = K - int(cmd[i][2:])

        elif cmd[i][0] == 'C': #선택된행 삭제
            if K == len(q) - 1 :
                delete_list.append(q[K])
                q.pop(K)
                K = K - 1 

            else:
                delete_list.append(q[K])
                q.pop(K)
                
        elif cmd[i][0] == 'Z': #복구
            back = delete_list.pop()
            q.append(back)
            q.sort()
            idx = q.index(back)
            if K >= idx:
                K = K + 1

        #print(q,delete_list,k,cmd[i])

    answer = ''

    for i in range(n):
        if i in q:
            answer += 'O'
        else:
            answer += 'X'

    return answer

#print(solution(8,2,["D 2","C","C","C","C","Z",'Z',"D 2","Z"]))

print(solution(8,3,["D 2","C","U 3","C","D 3","C","U 2","Z","Z","U 1","C","U 1","C","Z"]))
#print(solution(8,2,["D 2","C","C","C","C","Z",'Z',"D 2"]))