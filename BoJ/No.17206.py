N = int(input())
list1 = list(map(int,input().split()))

for i in range(N):
    sum = 0
    
    d3 = list1[i] // 3
    r3 = 3 * ( 1+d3 ) * (d3/2)

    d7 = list1[i] // 7
    r7 = 7 * ( 1+d7 ) * (d7/2)
    
    d21 = list1[i] // 21
    r21 = 21 * ( 1+d21) * (d21/2)

    sum = int( sum + r3 + r7 - r21 ) 
    print(sum)