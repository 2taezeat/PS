n = int(input())
l1 = list((input().split()))

m = int(input())
l2 = list((input().split()))


l1_dict = {}
for i in range(n):
    l1_dict[l1[i]] = 999


for i in l2:
    if i in l1_dict:
        print(1,end=' ')
    else:
        print(0,end=' ')

# 딕셔너리 !