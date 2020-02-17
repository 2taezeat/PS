N = int(input())

list1 = input()
slist = []
hlist = []
array1 = []

for i in range(N):
    array1.append( [list1[i] , i] )

newarray = sorted(array1)
print(newarray)

# for i in range(N//2):
#     slist.append()



#     hlist.append(newarray1[0][0])

# print(array1)
    