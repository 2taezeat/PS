# 투 포인터 알고리즘
N, M = map(int,input().split())
A = list(map(int,input().split()))
start, end = 0, 0
answer = 0
while(True):
    s = sum(A[start:end])

    if start == N:
        break

    if s >= M or end == N:
        start += 1
    else:
        end += 1

    if s == M:
        answer += 1
    
print(answer)