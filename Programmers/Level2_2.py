
def solution(brown, yellow):
    x1 = ((brown + 4) + (((brown+4)**2) - 16*(brown+yellow))**0.5 ) / 4
    y1 = (brown + yellow) // x1

    return [int(x1), int(y1)]

