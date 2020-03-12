import sys
import bisect
input = sys.stdin.readline
T = int(input())
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
AS, BS = [], []
for i in range(N):
    sum1 = 0
    for j in range(i,N):
        sum1 = sum1 + A[j]
        AS.append(sum1)
AS.sort()
for i in range(M):
    sum1 = 0
    for j in range(i,M):
        sum1 = sum1 + B[j]
        BS.append(sum1)

answer = 0

for i in BS:

    upper = bisect.bisect_right(AS, T - i)
    lower = bisect.bisect_left(AS, T - i)

    if lower < len(AS) and AS[upper-1] == T - i:
        answer = answer + (upper - lower)

print(answer)
