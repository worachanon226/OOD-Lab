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
        return s.items

leftparen = "({["
rightparen = ")}]"

inp = input("String : ")

for data in inp:
    if data in leftparen:
        s.push(data)
    if data in rightparen:
        while not s.isEmpty():
            top = s.top()
            if rightparen.find(data) == leftparen.find(top):
                s.pop()
                break
            else:
                print("Not match.")
                exit(0)
print("Match")

    