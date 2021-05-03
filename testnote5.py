def insertLeft(root, newBranch):
    t = root.pop(1) #root list를 말함
    if len(t) > 0: #값이 존재하면,
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch,[],[]])
def insertRight(root, newBranch):
    t = root.pop(2) #root list를 말함
    if len(t) > 0: #값이 존재하면,
        root.insert(2, [newBranch, t, []])
    else:
        root.insert(2, [newBranch,[],[]])
def BinaryTree(r):
    return [r, [], []]
def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]
def getRootVal(root):
    return root[0]


a = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
a.sort(key = lambda x : x[1] ,reverse=True)

tree = BinaryTree(a[0])
insertLeft(tree,a[1])
insertLeft(tree,a[2])
print(tree)
for i in range(1,len(a)):
    root = getRootVal(tree[i-1])
    root = tree[i-1]
    print(root)
    if root[0] > a[i][0]:
        insertLeft(tree,a[i])

    else:
        insertRight(tree,a[i])


print(tree)
