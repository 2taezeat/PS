# list1 = input()
# array1 = []
# I,a,c,d = 0,0,0,0
# #list1 = [sum(int(x) for x in y.split('+')) for y in input().split('-')]

# for i in range(len(list1)-1):
#     if (list1[i+1] == '-'):
#         array1.append(eval(list1[:i+1]))
#         e = 1
#         break

# while (I < len(list1)) : 

#     if (I == len(list1)-1):
#         if d == 1:
#             break
        
#         else:
#             a = eval( list1[c:I+1] )
#             array1.append(a)
#             break

#     if (list1[I+1] == '-'):
        
#         for j in range(I+2,len(list1)):

#             if j == len(list1)-1:
#                 d = 1
#                 a = - eval( list1[I+2:j+1] )
#                 array1.append(a)
#                 break

#             if list1[j+1] == '-':
#                 a = - eval( list1[I+2:j+1] )
#                 array1.append(a)
#                 d = d + 1
#                 c = j + 2
#                 break
#         I = j
#     else:
#         I = I + 1

# print(array1)
# print(sum(array1))
#######################################################3

array1 = input().split('-')
result = 0
for i in array1[0].split('+'):

    result = result + int(i)

for i in array1[1:]:

    for j in i.split('+'):

        result = result - int(j)
print(result)
