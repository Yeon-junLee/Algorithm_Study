import sys

class BTree():
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pre(root : Node):
    print(root.val,end="")
    if root.left:
        pre(root.left)
    if root.right:
        pre(root.right)

def post(root : Node):
    if root.left:
        post(root.left)
    if root.right:
        post(root.right)
    print(root.val, end="")

def inorder(root : Node):
    if root.left:
        inorder(root.left)
    print(root.val, end="")
    if root.right:
        inorder(root.right)
    

N = int(sys.stdin.readline())

# tree = []
# for i in range(N):
#     parent, child1, child2 = map(chr,sys.stdin.readline().split())
#     tree.append(parent)
    

PC = [list(sys.stdin.readline().split()) for _ in range(N)]
node = []
made = []

for li in PC:
    if li[0] not in made:
        temp = Node(li[0])
        node.append(temp)
        made.append(li[0])
    else:
        for n in node:
            if n.val == li[0]:
                temp = n
                break
    if li[1] != '.' and li[1] not in made:
        temp2 = Node(li[1])
        node.append(temp2)
        made.append(li[1])
        temp.left = temp2
    if li[2] != '.' and li[2] not in made:
        temp3 = Node(li[2])
        node.append(temp3)
        made.append(li[2])
        temp.right = temp3
btree = BTree()
btree.root = node[0]

pre(btree.root)
print()
inorder(btree.root)
print()
post(btree.root)