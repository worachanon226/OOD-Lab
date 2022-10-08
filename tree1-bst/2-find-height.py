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
        
    def getHeight(self,node,h,mx):
        if node:
            mx = self.getHeight(node.right, h+1,mx)
            mx = self.getHeight(node.left, h+1,mx)
            mx = max(h,mx)
        return mx

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = ""
for i in inp:
    root = T.insert(i)
print(f'Height of this tree is : {T.getHeight(root, 0, -999)}')
