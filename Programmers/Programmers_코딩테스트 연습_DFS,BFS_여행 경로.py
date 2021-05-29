def solution(tickets):
    answer_list = []
    v = [ False for _ in range(len(tickets))]

    def dfs(s,count,visit,result):
        if count == len(tickets)  : 
            answer_list.append(result)
            return
        j = 0
        for (a,b) in tickets:
            if s == a and visit[j] == False:
                visit[j] = True
                # *** result.append(b) => result + [b]
                dfs(b,count+1,visit,result+[b])
                #result = []
                visit[j] = False
            
            j += 1

    dfs("ICN",0,v,[])
    answer = min(answer_list)
    answer.insert(0,"ICN")
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
#print(solution([['ICN','A'],['A','B'],['A','C'],['C','A'],['B','D']]))
