n, k = map(int,input().split())

visited = [False] * 26
visited[ord('a')-ord('a')] = True
visited[ord('n')-ord('a')] = True
visited[ord('t')-ord('a')] = True
visited[ord('i')-ord('a')] = True
visited[ord('c')-ord('a')] = True
words = []
selectedCount = 5

# 단어들을 순회하면서 읽을 수 있는가를 체크하는 함수.
def countWords(visited):
    count = 0
    if k < 5:
        return count 
        
    for i in range(n):
        isPossible = True
        word = words[i]

        for c in word:
            j = ord(c) - 97
            if visited[j] == False: # 해당 알파벳을 배운적이 없으면. 
                isPossible = False
                break

        if isPossible == True:
            count = count + 1

    return count

def dfs(index,visited):
    global selectedCount
    global max1
    # 1. 체크인               visted[0-25] = true;
    visited[index] = True
    selectedCount += 1
    # 2. 목적지 인가?(조건)    selectedCount  == k => 최대개수 계산
    if (selectedCount == k):
        max1 = max(countWords(visited), max1)
    else:
        # 3. 갈 수 있는 곳을 순회  for (0~25)
        for i in range(index+1,26):
            # 4. 갈 수 있는가?           if (visted[] == false)
            if visited[i] == False:
                # 5. 간다 dfs(next)          dfs(next)
                dfs(i,visited)
    
    # 6. 체크아웃
    visited[index] = False
    selectedCount -= 1


for i in range(n):
    s = input()
    s = s[4:-4]
    words.append(s)

max1 = countWords(visited)
#print(max1)

for i in range(0,26):
    visited = [False] * 26
    visited[ord('a')-ord('a')] = True
    visited[ord('n')-ord('a')] = True
    visited[ord('t')-ord('a')] = True
    visited[ord('i')-ord('a')] = True
    visited[ord('c')-ord('a')] = True

    if visited[i] == False:
        dfs(i,visited)

print(max1)

