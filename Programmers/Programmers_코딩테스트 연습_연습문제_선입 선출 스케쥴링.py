def solution(n, cores):
    l1 = [ [] for _ in range(len(cores))]
    a = 0
    while True:
        for j in range(len(cores)):
            if l1[j] == [] and a <= n:
                a += 1
                if a == n:
                    return j + 1

                for k in range(cores[j]):
                    l1[j].append(a)

        for j in range(len(cores)):
            if l1[j] != []:
                l1[j].pop()


# 정확성 o, 효율성 x
print(solution(6,[1,2,3]))