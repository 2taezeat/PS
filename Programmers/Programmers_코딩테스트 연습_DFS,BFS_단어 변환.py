def solution(begin, target, words):
    answer_list = []

    def dfs(w,count,visit):
        if w == begin:
            answer_list.append(count)
            return
        j = 0
        for b in words:
            same_count = 0
            for i in range(len(b)):
                if b[i] == w[i]:
                    same_count += 1

            if same_count == len(begin) - 1 and visit[j] == False:
                visit[j] = True
                dfs(b,count+1,visit)
                visit[j] = False
            
            j += 1

    words.append(begin)
    v = [ False for _ in range(len(words))]
    if target not in words:
        return 0
    
    dfs(target,0,v)
    return min(answer_list)


print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","cog",	["hot", "dot", "dog", "lot", "log"]))