TCN = int(input())
for i in range(TCN):
    N, M = map(int, input().split() )
    queue1 = list(map(int, input().split()))
    f1 = queue1[M] 
    count = 0

    while queue1 != []:
        maxq = max(queue1)
        q0 = queue1[0]
        if maxq > queue1[0]:
            del queue1[0]
            queue1.append(q0)

            if M == 0 :
                M = len(queue1) - 1
            else:
                M = M - 1

        else:
            del queue1[0]
            count = count + 1
            M = M - 1

            if M == -1:
                break
            
    print(count)

