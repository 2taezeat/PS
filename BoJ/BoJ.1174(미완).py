n = int(input())
l1 = []
c = 0 
for i in range(0,9876543210):
    i = list(str(i))
    p = 0
    
    for m in range(1,len(i)):

        if i[m-1] <= i[m]:
            p = 1
            break

    if p == 0:
        i = ''.join(i)
        a = int(i)
        c = c + 1
        l1.append(a)
        print(a, c)
        #l1.append(i)

    # if len(l1) >= n:
    #     break

print(l1)
print(len(l1))
#a = ''.join(l1[-1])

#print(int(a))