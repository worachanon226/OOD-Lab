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



inp = input('Enter Input : ').split()

s = Stack()

boom = 0

for i in range(len(inp)):
    if s.size() < 2:
        s.push(inp[i])
    else:
        s.push(inp[i])
        th, sc, fr = s.pop(), s.pop(), s.pop()
        if not fr==sc==th:
            s.push(fr)
            s.push(sc)
            s.push(th)
        else:
            boom += 1

print(s.size())
if s.isEmpty():
    print("Empty")
else:
    while not s.isEmpty():
        print(s.pop(),end="")
    print()
if boom > 1:
    print(f'Combo : {boom} ! ! !')

