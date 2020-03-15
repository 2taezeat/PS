import itertools
L, C = map(int,input().split())
arr = input().split()
arr.sort()
c = list(map(list, itertools.combinations(arr,L)))
l1 = []

for i in c:
    s = ''
    ahdmacount = 0
    wkdmacount = 0
    for char in i:
        if char == 'a' or char == 'o' or char =='u' or char =='e' or char == 'i':
            ahdmacount = ahdmacount + 1
            
        else:
            wkdmacount = wkdmacount + 1

        s = s + char

    if ahdmacount >= 1 and wkdmacount >=2:
        l1.append(s)    

for i in l1:
    print(i)