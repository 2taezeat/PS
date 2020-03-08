N = int(input())

a =[]
for i in range(N):
    age, name = input().split()
    age = int(age)
    a.append([age,name,i])

a.sort(key=lambda x:(x[0],x[2]) )

for i in range(N):
    print(a[i][0],a[i][1])