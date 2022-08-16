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

inp = input("Enter Input : ").split(",")
q = Queue()

for data in inp:
    if len(data) == 1:
        if q.isEmpty():
            print("-1")
        else:
            print(f'Pop {q.pop()} size in queue is {q.size()}')
    else:
        n = data.split(" ")[1]
        print(f'Add {n} index is {q.size()}')
        q.push_back(n)

if q.isEmpty():
    print("Empty")
else:
    print(f'Number in Queue is :  {str(q)}')