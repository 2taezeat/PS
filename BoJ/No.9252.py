str1 = input()
str2 = input()
if len(str1) > len(str2) :
    str1, str2 = str2, str1

l_list1 =list(str1)
l_list2 =list(str2)
l_list1.insert(0,0)
l_list2.insert(0,0)

l_str1 = len(l_list1)
l_str2 = len(l_list2)

matrix1 = []
for j in range(l_str2):
    array1 = []

    for i in range(l_str1):

        if (i == 0) or (j==0):
            array1.append(0)
            
        else:
            if (l_list2[j] == l_list1[i]) :
                array1.append( matrix1[j-1][i-1] + 1 )
            
            else:
                max1 = -1 
                if (matrix1[j-1][i] > array1[i-1] ):
                    max1 = matrix1[j-1][i]
                else:
                    max1 = array1[i-1]

                array1.append( max1 )
        
    matrix1.append(array1)
print(max(matrix1[l_str2-1]))

array2 = []
j = l_str2 - 1
i = l_str1 - 1

while(1):

    while(1):
        if ( matrix1[j][i] > matrix1[j-1][i] ) and ( matrix1[j][i] > matrix1[j][i-1] ) and ( matrix1[j][i] > matrix1[j-1][i-1] ):
            array2.append(l_list2[j])
            i = i - 1
            break
        
        else:
            if ( matrix1[j][i] == matrix1[j][i-1] ):
                i = i - 1
                if (i-1 < 0) | (j-1 < 0):
                    break  

            if ( matrix1[j][i] == matrix1[j-1][i] ):
                j = j - 1
                if (i-1 < 0) | (j-1 < 0):
                    break  

    j = j - 1
    if (i-1 < 0) | (j-1 < 0):
        break 

la2 = len(array2) -1
for k in range(la2,-1,-1):
    print(array2[k],end='')
