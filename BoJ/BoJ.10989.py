# 계수 정렬 / Counting Sort
import sys
s = sys.stdin.readline
N = int(s())
c = [0 for _ in range(10001)]

for i in range(N):
    a = int(s())
    c[a] = c[a] + 1

for i in range(10001):
    for k in range(c[i]):
        print(i)


