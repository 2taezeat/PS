sl = []
for i in range(5):
    sc = int(input())

    if sc < 40 :
        sc = 40
    
    sl.append(sc)

print(sum(sl)//5)