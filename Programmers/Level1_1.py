def solution(strings, n):
    al = []
    for i in range(len(strings)):
        al.append([strings[i][n],strings[i]])

    answer = []
    al.sort()
    for j in range(len(strings)):
        answer.append(al[j][1])
        
    
    return answer