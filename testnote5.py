dic = {}
a = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
b = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
for i in range(len(a)):
    A = a[i]
    B = b[i]
    if B =='-':
        B = 'center'
    #print(A,B)

    dic[A] = dic.get(A, []) + [B]
    #dic[B] = dic.get(B, []) + [A]


print(dic) 