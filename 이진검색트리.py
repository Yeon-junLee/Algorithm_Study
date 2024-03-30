import sys
sys.setrecursionlimit(10**6)
class BST():
    def __init__(self, root):
        self.root = root
    
    def insert(self, data):
        self.cur = self.root
        while True:
            if data < self.cur.val:
                if self.cur.left != None:
                    self.cur = self.cur.left
                else:
                    self.cur.left = Node(data)
                    break
            else:
                if self.cur.right != None:
                    self.cur = self.cur.right
                else:
                    self.cur.right = Node(data)
                    break


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def post(root : Node):
    if root.left:
        post(root.left)
    if root.right:
        post(root.right)
    print(root.val)

val = int(sys.stdin.readline())
root = Node(val)
bst = BST(root)
while  True:
    val = sys.stdin.readline()
    if val == "":
        break
    else:
        bst.insert(int(val))

post(bst.root)