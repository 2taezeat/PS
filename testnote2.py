import itertools
n = int(input())
lineup = []
l1 = [1,2,3,4,5,6,7,8]
aa = list ( itertools.permutations(l1) )
pp = []
for a in aa:
    b = list(a)
    b.insert(3,0)
    pp.append(b)
for i in range(n):
    lineup.append( list(map(int,input().split())) )

result = []

p = [0,1,2,3,4,5,6,7,8]
i = 0
score = 0
for l in lineup:
    
    out_count = 0
    base1 = 0
    base2 = 0
    base3 = 0
    while(1):
        player_number = p[i]
        state = l[player_number]


        if state == 0:
            out_count += 1
            i = i + 1
        elif state == 1:
            print('#',score+base3,'#',end= '-')
            score = score + base3
            base3 = base2 | 0
            base2 = base1 | 0
            base1 = 1
            i = i + 1
        elif state == 2:
            score = score + base2 + base3
            base2 = 1
            base3 = base1 | 0
            base1 = 0
            i = i + 1
        
        elif state == 3:
            score = score + base1 + base2 + base3
            base1 = 0
            base2 = 0
            base3 = 1
            i = i + 1

        elif state == 4:
            score = score + base1 + base2 + base3 + 1
            base1 = 0
            base2 = 0
            base3 = 0
            i = i + 1

        print(player_number,state,i,base1,base2,base3,score)

        if i == 9:
            i = 0

        if out_count > 2:
            break

result.append(score)

#print(result)
print(max(result))