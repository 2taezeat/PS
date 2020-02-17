N = int(input())
answer = 0

if N >= 0 and N <= 10:
    answer = 1

if N >= 11 and N <= 110:
    answer = 2

if N >= 111 and N <= 1110:
    answer = 3

if N >= 1111 and N <= 11110:
    answer = 4

if N >= 11111 and N <= 111110:
    answer = 5

if N >= 111111 and N <= 1111110:
    answer = 6

if N >= 1111111 and N <= 11111110:
    answer = 7

if N >= 11111111 and N <= 111111110:
    answer = 8

if N >= 111111111 and N <= 1111111110:
    answer = 9

print(answer)