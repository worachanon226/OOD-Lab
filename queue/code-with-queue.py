class Queue:
    def __init__(self):
        self.items = []

    def push_back(self,i):
        self.items.append(i)
    
    def pop(self):
        front = self.items[0]
        self.items = self.items[1:]
        return front

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0
    
    def __str__(self):
        return str(self.items)

q = Queue()
inp = input("Enter code,hint : ").split(",")
code, hint = inp[0], inp[1]
dif = ord(hint) - ord(code[0])
for data in code:
    q.push_back(chr(ord(data) + int(dif)))
    print(q)
