import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def BS(seq,target): # 반복문
    high, low = len(seq)-1, 0
    while high >= low:   
        mid = (high + low) // 2
        if seq[mid] == target:
            return 1

        elif seq[mid] > target:
            high = mid

        elif seq[mid] < target:
            low = mid + 1
    
    return 0
 
def BSR(seq,target,low,high): # 여기서는 재귀버젼 더 빠른듯
    if low > high:
        return 0
    
    mid = (high + low) // 2
    if seq[mid] == target:
        return 1

    elif seq[mid] > target:
        return BSR(seq,target,low,mid-1)

    elif seq[mid] < target:
        return BSR(seq,target,mid+1,high)

N = int(input())
A = list(map(int,input().split()))
A.sort()

M = int(input())
targetlist = list(map(int, input().split()))

for i in range(M):
    print( BSR(A,targetlist[i], 0 ,N-1 ) )

