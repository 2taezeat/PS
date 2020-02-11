import sys
N = int(sys.stdin.readline())
list1 = []
for i in range(N):
    a = list(input())
    list1.append(a)

for l in list1:
    left = [] # 커서 기준 왼쪽
    right = [] # 커서 기준 오른쪽
    length1 = len(l)

    for j in range(length1):
        if l[j] == '<':
            if (left != []):
                right.append(left.pop())

        elif l[j] == '>':
            if (right != []):
                left.append(right.pop())

        elif l[j] == '-':
            if (left != []):
                left.pop()

        else:
            left.append(l[j])

    left = left
    right.reverse()
    print(''.join(left+right))