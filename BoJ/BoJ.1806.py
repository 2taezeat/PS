N, S = map(int,input().split())
A = list(map(int,input().split()))
start, end = -1, -1
answer = []
i = 1
s = 0
while(True):
    if start == N or (end == N):
        break
    else:
        if s >= S :
            answer.append(end-start)
            start += 1
            s = s - A[start]
        
        elif s < S:
            end += 1
            if end != N:
                s = s + A[end]

if answer == []:
    print(0)
else:
    #print(answer)
    print(min(answer))