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
        if inp[i]=="B":
            print(s.size())
        if inp[i]=="S":
            tmp = []
            while not s.isEmpty():
                top = int(s.pop())
                if top % 2 == 0:
                    top -= 1
                else:
                    top += 2
                tmp.append(top)
            tmp.reverse()
            for i in range(len(tmp)):
                n = tmp[i]
                while not s.isEmpty() and int(n) >= int(s.top()):
                    s.pop()
                s.push(n)
    else:
        s.push(n)