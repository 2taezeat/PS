N = int(input())
list1 = []
psum = 0 
for i in range(N):
    x, a = map(int,input().split())
    list1.append( [x,a])
    psum = psum + a

list1.sort()
pssum = 0

for i in range(N):
    pssum = list1[i][1] + pssum
    if (psum + 1 ) // 2 <= pssum:
        break

print(list1[i][0])
