class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1
    
class AVL:
    def insert(self,data,root):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(data, root.left)
        else:
            root.right = self.insert(data, root.right)
        
        root.height = 1 + max(self.getheight(root.left),self.getheight(root.right))

        balance = self.getbalance(root)

        if balance > 1 and data < root.left.data:
            return self.right(root)
        if balance > 1 and data > root.left.data:
            root.left = self.left(root)
            return self.right(root)
        if balance < -1 and data < root.right.data:
            root.right = self.right(root)
            return self.left(root)
        if balance < -1 and data > root.right.data:
            return self.right(root)
        return root
    
    def right(self,z):
        y = z.left
        x = y.right
        y.right = z
        z.left = x
        z.height = 1 + max(self.getheight(z.left),self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left),self.getheight(y.right))
        return y
    
    def left(self,z):
        y = z.right
        x = y.left
        y.left = z
        z.right = x
        z.height = 1 + max(self.getheight(z.left),self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left),self.getheight(y.right))
        return y

    def getbalance(self,root):
        return self.getheight(root.left) - self.getheight(root.right)
        
    def getheight(self,root):
        if not root:
            return 0
        return root.height
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

T = AVL()
root = None
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    print(f'Insert : ( {i} )')
    root = T.insert(i,root)
    T.printTree(root)
    print("--------------------------------------------------")