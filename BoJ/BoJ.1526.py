N = int(input())
list1 = ['4','7']
for i in range(2,7):
    ml = []
    nl = []
    for a in list1:
        if len(a) == i-1:
            m = '4'+a
            ml.append(m)
    
    for b in list1:
        if len(b) == i-1:
            n = '7'+b
            nl.append(n)

    list1 = list1 + ml + nl

for i in range(len(list1)):
    list1[i] = int(list1[i])

    if N < list1[i]:
        result = list1[i-1]
        break

if N >= 777777:
    result = 777777

print(result)