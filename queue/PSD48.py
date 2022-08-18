class Queue:
    def __init__(self):
        self.items = []

    def push_back(self,i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0
    
    def __str__(self):
        return str(self.items)

inp = input("Enter Input : ").split(",")
q1 = Queue()
q2 = Queue()
for data in inp:
    if len(data) == 1:
        if not q2.isEmpty():
            print(f'{q2.pop()}')
        elif not q1.isEmpty():
            print(f'{q1.pop()}')
        else:
            print("Empty")
    else:
        ln = data.split(" ")
        if ln[0] == "EN":
            q1.push_back(ln[1])
        if ln[0] == "ES":
            q2.push_back(ln[1])