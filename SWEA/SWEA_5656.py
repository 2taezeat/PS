import sys
from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,w,h = map(int,input().split())
    space = []
    for i in range(h):
        space.append(list(map(int,input().split())))


    print(space)