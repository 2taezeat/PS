def solution(n):

    def dfs(l,c,d):
        answer = 0
        if c == n:
            return 1

        for i in range(n):
            l[c] = i
            for j in range(c):
                if l[j] == l[c]:
                    break

                if abs(l[j] - l[c]) == c - j:
                    break
            else:
                answer += dfs(l, c+1,d+1)

        return answer

    a = dfs( [0]*n, 0,0 )
    return a

print(solution(4))