l = input()
i = 0
l3 = []
while( i < len(l) ):
    if l[i] == '<':
        pp = 1
        j = i

        for k in range(i,len(l)):
            if l[k] == '>':
                pp = 0
                s_s = ''.join(l[j:k+1])
                l3.append(s_s)

            if pp == 0:
                i = k
                break
    else:
        if l[i] != ' ':
            l3.append(i)
        else:
            l3.append(' ')

    i = i + 1

l5 = []
i = 0

while(i < len(l3)):
    l5 =[]

    if type(l3[i]) == type('asd'):
        print(l3[i],end='')

    else:
        j = i 
        while(l3[j] != ' '):
            if type(l3[j]) == type('asd'):
                break

            l5.append( l[ l3[j] ] )
            j = j + 1
            if j == len(l3):
                break

        l5.reverse()
        print(''.join(l5),end='')
        i = j - 1

    i = i + 1