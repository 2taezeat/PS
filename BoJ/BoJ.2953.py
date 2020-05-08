l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l3 = list(map(int,input().split()))
l4 = list(map(int,input().split()))
l5 = list(map(int,input().split()))

sl = [sum(l1),sum(l2),sum(l3),sum(l4),sum(l5)]
winner = max(sl)

print(sl.index(winner)+1,winner)