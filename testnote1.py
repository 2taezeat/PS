result = []
def solution(tickets):
    answer_list = []
    

    def dfs(s,count,visit):
        global result
        if count == len(tickets) and len(result) == len(tickets)+1:
            answer_list.append(result)
            # result = []
            print(count,result)
            #print(1111)
            return
        #result.append(s)
        j = 0
        print(result,count)
        for (a,b) in tickets:
            
            if s == a and visit[j] == False:
                visit[j] = True
                result.append(b)
                dfs(b,count+1,visit)
                result = []
                visit[j] = False
            
            j += 1
        
    v = [ False for _ in range(len(tickets))]
    dfs("ICN",0,v)
    for a in answer_list:
        print(a)
    
    answer = min(answer_list)
    answer.insert(0,"ICN")

    return answer


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
