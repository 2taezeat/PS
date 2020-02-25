# Introduction to Algorithms (3rd) 를 참고
import math
Infinity = math.inf
import sys
input = sys.stdin.readline
def Merge(l, p, q, r):
    n1 = q - p + 1
    n2 = r - q
 
    Left = list()
    Right = list()
    for i in range(0, n1):
        Left.append(l[p + i])
 
    for j in range(0, n2):
        Right.append(l[q + 1 + j])
 
    Left.append(Infinity)
    Right.append(Infinity)
 
    i = 0
    j = 0
 
    for k in range(p, r+1):
        if Left[i] <= Right[j]:
            l[k] = Left[i]
            i = i + 1
        else:
            l[k] = Right[j]
            j = j + 1
 
def MergeSort(l, p, r):
    if p < r:
        q = (p + r) // 2
        MergeSort(l, p, q)
        MergeSort(l, q+1, r)
        Merge(l, p, q, r)
 
# list 하나 입력 받기
N = int(input())
list1 = []
for i in range(N):
    a = int(input())
    list1.append(a)
 
# 정렬후 결과 값 출력
MergeSort(list1,0,len(list1)-1)
for i in range(N):
    print(list1[i])