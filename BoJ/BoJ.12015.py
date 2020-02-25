from bisect import *
import sys

n = int(input())
a = [int(x) for x in sys.stdin.readline().split()]

answer = [a[0]]
for i in range(1,len(a)):
    num = a[i]
    if answer[-1] < num:
        answer.append(num)
    else:
        idx = bisect_left(answer,num)
        answer[idx] = num

print(len(answer))