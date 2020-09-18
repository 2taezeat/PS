n = int(input())
l1 = list((input().split()))

m = int(input())
l2 = list((input().split()))
# input 받기

l1_dict = {} # dictionary 초기화
for i in range(n):
    l1_dict[l1[i]] = 999


for i in l2:
    if i in l1_dict:
        print(1,end=' ')
    else:
        print(0,end=' ')

# dictionary자료구조는 내부적으롤 hash를 
# 통해서 자료들을 저장하기 때문에 시간복잡도가 O(1)가 가능합니다.
# 따라서 이경우에 l1,l2를 list in으로 반복문을 도는 것 보다
# dict을 이용하여 in 연산자(search)하는 것이 훨씬 효율적 입니다.