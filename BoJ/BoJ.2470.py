# 이진탐색_3_이태경.py

# 초기화 및 input 받기
n = int(input())
l1 = list(map(int,input().split()))
a = []
result = []

# l1을 절댓값을 기준으로 오름차순 정렬
for i in range(n):
    x = l1[i]
    a.append([abs(x),x])
a.sort()

# 양 옆의 수들의 합중 0에 가장 가까운 값으로 정렬
for i in range(0,n-1):
    y = a[i][1]+a[i+1][1]
    result.append( [abs(0-y), a[i][1], a[i+1][1] ] )
result.sort()

# 정답 산출을 위한 과정
answer = [0,0]
answer[0] = result[0][2]
answer[1] = result[0][1]
answer.sort()
print(answer[0],answer[1])