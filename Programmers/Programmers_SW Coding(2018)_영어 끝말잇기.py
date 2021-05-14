import math
def solution(n, words):
    stack = []
    i = 1
    for w in words:
        if w in stack: break
        elif i != 1 and stack[-1][-1] != w[0]: break
        else: stack.append(w)
        i = i + 1

    if len(words) + 1 == i:
        return [0,0]

    per = (i) % (n)
    rou = math.ceil(i / n)
    if per == 0:
        per = n

    return [per,rou]


#print(solution(3,	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
#print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))