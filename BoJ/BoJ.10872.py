a = [1]
for i in range(1,12):
    a.append(i*a[i-1])

n = int(input())
print(a[n])