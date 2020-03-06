import sys
N = int(input())
tree = {}
for i in range(N):
    p, lc, rc = input().split()
    tree[p] = [lc, rc]

def preorder(node):
    print(node, end='')

    if tree[node][0] != '.':
        preorder(tree[node][0])

    if tree[node][1] != '.' :
        preorder(tree[node][1])

def inorder(node):
    if tree[node][0] != '.':
        inorder(tree[node][0])

    print(node, end='')

    if tree[node][1] != '.' :
        inorder(tree[node][1])

def postorder(node):
    if tree[node][0] != '.':
        postorder(tree[node][0])

    if tree[node][1] != '.' :
        postorder(tree[node][1])

    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')