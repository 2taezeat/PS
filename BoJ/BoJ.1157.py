s = input()
s = s.upper()
s_set = list(set(s))
s_list = list(s)
cl = []
for c in s_set:

    count = 0
    for j in s_list:
        if c == j:
            count += 1

    cl.append([count,c])

ml = []

m = max(cl)[0]
for i in range(len(cl)):
    if cl[i][0] == m:
        ml.append(cl[i])

if len(ml) > 1:
    print('?')
else:
    print(ml[0][1])