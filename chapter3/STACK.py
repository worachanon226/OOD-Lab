class Stack:
    
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()
        
    def top(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)


inp = input("Enter Input : ").split(",")

s = Stack()

for i in range(len(inp)):
    if len(inp[i]) == 1:
        if not s.isEmpty():
            top = s.pop()
            print(f'Pop = {top} and Index = {s.size()}')
        else:
            print("-1")
    else:
        n = inp[i].split(" ")[1]
        s.push(n)
        print(f'Add = {n} and Size = {s.size()}')

print("Value in Stack = ",end = "")
if s.isEmpty():
    print("Empty")
else:
    ls = []
    while not s.isEmpty():
        ls.append(s.pop())
    ls.reverse()
    print(" ".join(ls))