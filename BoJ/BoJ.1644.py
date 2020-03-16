N = int(input())
prime = []
nl = [True] * (N+1)
nl[0] = nl[1] = False # 소수 아님

for i in range(2,N+1):
    if nl[i] == True:
        j = 2
        k = j*i
        while( k <= N ):
            nl[k] = False 
            j = j + 1
            if k > N:
                break
            k = j*i

for i in range(2,N+1):
    if nl[i] == True:
        prime.append(i)

start, end = -1, -1
answer, s = 0 ,0
le = len(prime)
while(True):
    if start == le or (end == le):
        break
    else:
        if s >= N :
            if s == N:
                answer += 1
            start += 1
            s = s - prime[start]
        
        elif s < N:
            end += 1
            if end != le:
                s = s + prime[end]

print(answer)