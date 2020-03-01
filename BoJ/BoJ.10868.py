import sys
input = sys.stdin.readline

N , M  = map(int,input().split())
nl = []

for i in range(N):
    num = int(input())
    nl.append(num)

nl.sort()

for j in range(M):
    a , b  = map(int,input().split())
    print(nl[a-1])
    #print(min(nl[a-1:b]))