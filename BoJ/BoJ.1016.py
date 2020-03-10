n,m = map(int,input().split())
list1 = [True] * (m-n+1)
count = 0
N = n
k = 2

while (k*k) <= m:    
    square = (k*k)
    i = N // square

    while i * square <= m :

        index = i * square - n

        if index >= 0 and list1[index] == True:
            count = count + 1
            list1[index] = False

        i = i + 1

    k = k + 1

print(m-n+1-count)