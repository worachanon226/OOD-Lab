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

    def clear(self):
        self.items.clear()
    
    def __str__(self):
        return str(self.items)


inp = input("Enter Input : ").split(",")

s1 = Stack()
s2 = Stack()

for i in range(len(inp)):
    if len(inp[i]) == 1:
        if inp[i]=="B":
            print(s2.size())
        if inp[i]=="S":
            tmp = []
            s2.clear()
            while not s1.isEmpty():
                top = int(s1.pop())
                if top % 2 == 0:
                    tmp.append(top-1)
                else:
                    tmp.append(top+2)
            tmp.reverse()
            for n in tmp:
                s1.push(n)
                while not s2.isEmpty() and int(n) >= int(s2.top()):
                    s2.pop()
                s2.push(n)
    else:
        n = inp[i].split(" ")[1]
        s1.push(n)
        while not s2.isEmpty() and int(n) >= int(s2.top()):
            s2.pop()
        s2.push(n)