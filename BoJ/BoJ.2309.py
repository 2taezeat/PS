list1=[]
for i in range(0,9):
    i = int(input())
    list1.append(i)

list1.sort()

list2=[]
a =0
b =0

for i in range(0,9):
    for j in range(0,9):
        if ( sum(list1) - (list1[i] + list1[j]) ) == 100:
            a = i
            b = j

A = list1[a]
B = list1[b]
list1.remove(A)
list1.remove(B)
for i in list1:
    print(i)
    