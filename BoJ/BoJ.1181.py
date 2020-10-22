import sys
N = int(input())
list1 = []
for i in range(N):
    list1.append(input())

list1 = list(set(list1))
list1.sort()
arr1 = []

for w in list1:
    arr1.append([len(w),w])

arr1.sort()
for i in arr1:
    print(i[1])