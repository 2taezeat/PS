import sys
input = sys.stdin.readline
N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

#숫자 별로 count 해준다
N_count = {}
for n in N_list:
    try:
        N_count[n] = N_count[n] + 1
    except:
        N_count[n] = 1
    
for m in M_list:
    try:
        print(N_count[m],end=' ')
    except:
        print(0,end=' ')
