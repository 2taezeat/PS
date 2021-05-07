from collections import Counter
def solution(a):
    cou = Counter(a)
    ans = 0

    for (k,v) in cou.items():
        length = 0
        i = 0
        if ans > (v*2):
            continue

        while(i < len(a) - 1):
            if a[i] == a[i+1]:
                i = i + 1

            elif a[i] == k or a[i+1] == k:
                i = i + 2
                length += 2

            else:
                i = i + 1

        ans = max(length,ans)

    return ans


#print(solution([0]))
#print(solution([5,2,3,3,5,3]))
print(solution([0,3,3,0,7,2,0,2,2,0]))

#print(solution([0,1,1,3,7,2,4,3,3,3]))
