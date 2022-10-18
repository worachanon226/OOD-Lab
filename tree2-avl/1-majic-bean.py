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
    
    def insert(self,data):
        if not self.root:
            self.root = Node(data)
            print("*",end="")
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left:
                        print("L",end="")
                        cur = cur.left
                    else:
                        print("L*",end="")
                        cur.left = Node(data)
                        break
                elif data > cur.data:
                    if cur.right:
                        print("R",end="")
                        cur = cur.right
                    else:
                        print("R*",end="")
                        cur.right = Node(data)
                        break
                else:
                    break

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)
    print("")