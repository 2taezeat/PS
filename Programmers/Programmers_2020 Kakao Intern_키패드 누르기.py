def diff_cal(d):
    real_d = 0

    if d == -10:
        real_d = 4
    elif d == -8:
        real_d = 4
    elif d == -7:
        real_d = 3
    elif d == -5:
        real_d = 3
    elif d == -4:
        real_d = 2
    elif d == -2:
        real_d = 2
    elif d == -1:
        real_d = 1

    elif d == 10:
        real_d = 4
    elif d == 8:
        real_d = 4
    elif d == 7:
        real_d = 3
    elif d == 5:
        real_d = 3
    elif d == 4:
        real_d = 2
    elif d == 2:
        real_d = 2
    elif d == 1:
        real_d = 1

    elif d == 3:
        real_d = 1
    elif d == 6:
        real_d = 2
    elif d == 9:
        real_d = 3

    elif d == -3:
        real_d = 1
    elif d == -6:
        real_d = 2
    elif d == -9:
        real_d = 3

    return real_d


def solution(numbers, hand):
    answer = ''
    left_h = 10
    right_h = 12

    for n in numbers:
        if n == 0:
            n = 11

        if n == 1 or n == 4 or n == 7:
            answer = answer + 'L'
            left_h = n

        elif n == 3 or n == 6 or n == 9:
            answer = answer + 'R'
            right_h = n

        elif n == 2 or n == 5 or n == 8 or n == 11:
            diff_l = left_h - n
            diff_r = right_h - n

            diff_l = diff_cal(diff_l)
            diff_r = diff_cal(diff_r)

            if diff_l > diff_r:
                answer = answer + 'R'
                right_h = n

            elif diff_l < diff_r:
                answer = answer + 'L'
                left_h = n

            elif diff_l == diff_r:
                if hand == 'right':
                    answer = answer + 'R'
                    right_h = n

                elif hand == 'left':
                    answer = answer + 'L'
                    left_h = n

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))