A, B = list(input().split())
dlist = []
Al = len(A)
Bl = len(B)

for i in range(Bl-Al+1):
    d = 0
    for j in range(i,Al+i):
        k = j-i
        if A[k] != B[j]:
            d = d + 1

    dlist.append(d)

print(min(dlist))