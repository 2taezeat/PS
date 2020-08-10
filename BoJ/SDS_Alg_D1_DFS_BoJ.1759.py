l, c = map(int,input().split())
data = input().split()
data.sort()

def dfs(length, con, vow, current, pwd): # 주어진 모든 알파벳을 순회할수있는 dfs
    global data
    # 1. 체크인 - 생략가능        
    # 2. 목적지 인가?(조건)
    if (length == l):
        if (con >= 2) and (vow >= 1):
            print(pwd)
    else:
        # 3. 갈 수 있는 곳을 순회  
        for i in range(current + 1, c):
            # 4. 갈 수 있는가? - 생략 가능

            # 5. 간다
            if (data[i] == 'a') or (data[i] == 'e') or (data[i] == 'i') or (data[i] == 'o') or (data[i] == 'u'):
                dfs(length + 1, con, vow + 1, i, pwd + data[i])
            else:
                dfs(length + 1, con + 1, vow, i, pwd + data[i])

    # 6. 체크아웃 - 생략가능



dfs(0,0,0,-1,"")