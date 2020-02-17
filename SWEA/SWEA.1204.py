T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    l1 = list(map(int, input().split()))
    l1.sort()
    countlist = []
    der_l1 = list(set(l1))

    for el in der_l1:
        count = 0 
        for j in range(len(l1)):
            if el == l1[j]:
                count = count + 1

        countlist.append([count,el])
    r = countlist.index(max(countlist))
    print('#',N,' ',der_l1[r], sep="")
