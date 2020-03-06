n, ans = int(input()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def solve(i):
    global ans

    if i == n:
        ans += 1
        return
        
    for j in range(n):

        if a[j] == False and b[i+j] == False and c[i-j+n-1] == False :

            a[j] = b[i+j] = c[i-j+n-1] = True

            solve(i+1)

            a[j] = b[i+j] = c[i-j+n-1] = False # 해제

solve(0)
print(ans)


# 백트래킹, 가지치기, 경우를 검사할때, 불가하다 판단되면 그쪽 가지는 폐쇄(가지치기) 시키고 다음 가지로 넘어가서 검사함.
# https://idea-sketch.tistory.com/29
# https://rebas.kr/761

# N = 4일때,
# i, j / row ,column

# i = 0 , j = 0 일때부터 시작
# i = 1, j = 0~3 중 조건에 맞는 것만 검사

# 조건에 맞는 i = 1, j=2 은 그 이후

# i = 2, j = 0~ 3 로 도약,
# 하지만 , i = 2, j = 0~ 3 인 경우 모두 불가
# a[j] = b[i+j] = c[i-j+n-1] = False 로 True를 False로 해제시킴(F-> 될것이라고 예상하고 T로 바꿈, T-> 불가하다고 판정나면 -> F (해제 시킴))
# 따라서 i = 0 , j = 0 / i = 1, j = 2 이 가지는 불가

# i = 1, j = 0~3 중 다음 조건 i = 1, j = 3 검사,

# i = 4가 되어 모든 행(row)의 검사가 통과 그러면, result += 1, 하나의 조건을 만족하는 경우(case,instance, 이 가지는 행을 하나씩 덤어가서, 끝까지 같을때까지도 조건 만족) 가 생김,

# 이게 i =0, j =0 의 '한 사이클' 이 끝난 경우//

# 다음은 i = 0, j = 1 => '한 사이클'
# 그 다음은 i = 0, j = 2 => '한 사이클'
# 그 다음은 i = 0, j = 3 => '한 사이클'

# 총 4개의 '큰 사이클'

# 다 끝나면, global result(모든조건을 만족하고 살아남은 가지의 갯수, 정답) 를 출력


