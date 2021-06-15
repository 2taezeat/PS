def check(word):
    for i in range(len(word) // 2):      # 0부터 문자열 길이의 절반만큼 반복
        if word[i] != word[-1 - i]:      # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
            return False

    return True

def solution(s):
    for l in range(len(s),0,-1):
        i = 0
        while True:
            if i + l > len(s):
                break

            word = s[i:i+l]
            # print(word)
            if check(word):
                return l

            i += 1

    return 0