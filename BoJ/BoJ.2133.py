N = int(input())
dplist = [0,3,0,11,0]


for i in range(5,31):
    update = 0

    if ( i % 2 == 0):
        dplist.append(0)

    else:
        update = dplist[i-2] * 3
        for j in range(i-4,0,-2):
            update = dplist[j]*2 + update

            

        update = update + 2
        dplist.append(update)

print(dplist[N-1])