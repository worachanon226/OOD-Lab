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

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
        
    def rank(self,ch):
        def order(node,ans):
            if node.data <= ch:
                ans += 1
            if node.left:
                ans = order(node.left,ans)
            if node.right:
                ans = order(node.right,ans)
            return ans
        return order(self.root,0)
        

T = BST()
st = input("Enter Input : ").split("/")
inp, ch = [int(i) for i in st[0].split()], st[1]
root = ""

for i in inp:
    root = T.insert(i)
T.printTree(root)
print(f'--------------------------------------------------\nRank of {ch} : {T.rank(int(ch))}',end="")