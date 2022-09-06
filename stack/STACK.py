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
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return " ".join(self.items)


inp = input("Enter Input : ").split(",")

s = Stack()

for i in range(len(inp)):
    if len(inp[i]) == 1: # P
        if not s.isEmpty(): # not Empty
            top = s.pop()
            print(f'Pop = {top} and Index = {s.size()}')
        else:
            print("-1")
    else: #A value
        n = inp[i].split(" ")[1]
        s.push(n)
        print(f'Add = {n} and Size = {s.size()}')

print("Value in Stack = ",end = "")
if s.isEmpty():
    print("Empty")
else:
    print(s)