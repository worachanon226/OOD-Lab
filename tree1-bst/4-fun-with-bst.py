class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return self.root
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        break
                elif data > cur.data:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Node(data)
                        break
                else:
                    break
            return self.root
        
    def preorder(self,r):
        if r:
            print(f'{r.data} ',end="")
            self.preorder(r.left)
            self.preorder(r.right)

    def inorder(self,r):
        if r:
            self.inorder(r.left)
            print(f'{r.data} ',end="")
            self.inorder(r.right)

    def postorder(self,r):
        if r:
            self.postorder(r.left)
            self.postorder(r.right)
            print(f'{r.data} ',end="")

    def breadth(self,r):
        queue = []
        queue.append(r)
        while queue:
            node = queue.pop(0)
            print(f'{node.data} ',end="")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = ""
for i in inp:
    root = T.insert(i)
print("Preorder : ",end=""), T.preorder(root)
print(f'\nInorder : ',end=""), T.inorder(root)
print(f'\nPostorder : ',end=""), T.postorder(root)
print(f'\nBreadth : ',end=""),T.breadth(root)