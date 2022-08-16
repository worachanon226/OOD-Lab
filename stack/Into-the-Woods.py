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
        print(s.size())
    else:
        n = inp[i].split(" ")[1]
        while not s.isEmpty() and int(n) >= int(s.top()):
            s.pop()
        s.push(n)