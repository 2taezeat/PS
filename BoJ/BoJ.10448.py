t = int(input())

gl = []
for j in range(1,45):
    gl.append( (j*(j+1))//2 )

el = [0] * 1001

for a in gl:
    for b in gl:
        for c in gl:

            if a+b+c < 1001:
                el[a+b+c] = 1

for i in range(t):

    k = int(input())
    print(el[k])