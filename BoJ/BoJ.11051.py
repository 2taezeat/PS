import math
N, K = map(int, input().split())

r = math.factorial(N) // ( math.factorial(K) * math.factorial(N-K) )
print( r % 10007 )