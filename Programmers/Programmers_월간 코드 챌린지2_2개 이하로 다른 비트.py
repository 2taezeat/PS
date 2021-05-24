def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n+1)
            continue
        else:
            b = bin(n)
            b = '0' + b[2:]
            b = list(b)
            for i in range(len(b)-1,-1,-1):
                if b[i] == '0':
                    b[i] = '1'
                    break
            b[i+1] = '0'
            answer.append( int(''.join(b),2) )

    return answer

print(solution([3,7]))