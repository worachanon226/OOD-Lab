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

    def setValue(self,v):
        self.diff = 9999999
        self.ans = 0
        self.value = v

    def closestValue(self):
        return self.ans

    def insert(self, data):
        if abs(self.value-data) < self.diff:
            self.diff = abs(self.value-data)
            self.ans = data
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

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ').split("/")
fir = [int(i) for i in inp[0].split()]
T.setValue(int(inp[1]))
for i in fir:
    root = T.insert(i)
    T.printTree(root)
    print("--------------------------------------------------")
print(f'Closest value of {inp[1]} : {T.closestValue()}')