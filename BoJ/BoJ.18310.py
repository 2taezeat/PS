import sys
n = int(input())
l1 = list(map(int,sys.stdin.readline().strip().split()))
l1.sort()

print(l1[(n-1)//2])