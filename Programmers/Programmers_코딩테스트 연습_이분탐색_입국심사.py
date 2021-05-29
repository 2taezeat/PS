def solution(n, times):
    left = 1
    right = max(times) * (n // len(times))
    while left <= right:
        mid = (left + right) // 2
        time = 0
        for t in times:
            time = time + (mid // t)

        if time < n:
            left = mid + 1
        else:
            right = mid - 1

    return left

print(solution(6,[7,10]))