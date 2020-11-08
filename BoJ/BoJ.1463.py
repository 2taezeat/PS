N = int(input())

dplist = [0,0,1,1]

# 주어진 수 N을 1로 만드는 최소 횟수는
# 1. N-1을 1로 만드는 최소 횟수 + 1
# 2. N/2을 1로 만드는 최소 횟수 + 1
# 3. N/3을 1로 만드는 최소 횟수 + 1

for i in range(4,N+1):
    dplist.append( dplist[i-1] + 1 )
    
    if (i % 3 ==0):
        dplist[i] = min(dplist[i], dplist[i//3]+1 )

    if (i % 2 ==0):
        dplist[i] = min(dplist[i], dplist[i//2]+1 ) 

print(dplist[N])

