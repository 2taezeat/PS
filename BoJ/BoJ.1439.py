# 그리디_1_이태경.py
l1 = list(input())
r = []
for i in range(len(l1)-1):

    if l1[i] != l1[i+1]: # 현재와 그 뒤의 l1값이 다르면, 현재 l1[i]값 r에 추가
        r.append(l1[i])

r.append(l1[-1]) # 마지막 원소 추가
c0 = 0 # r리스트에서 '0'의 갯수 count
c1 = 0 # r리스트에서 '1'의 갯수 count
for i in r:
    if i == '0':
        c0 = c0 + 1
    elif i == '1':
        c1 = c1 + 1

# 0의 갯수와 1의 갯수중 작은값 print
print(min(c0,c1))