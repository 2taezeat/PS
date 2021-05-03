a = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
a.sort(key = lambda x : x[1] ,reverse=True)

print(a)


tree = [a[0], [], []]

