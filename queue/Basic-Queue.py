class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self,i):
        self.items.append(i)
    
    def deQueue(self):
        return self.items.pop(0)

    def front(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0
    
    def __str__(self):
        return str(self.items)

# inp = input("Enter Input : ").split(",")
q = Queue()
print(q)
q.enQueue(2)
print(q)
q.enQueue(3)
print(q)
print(q.front())
q.deQueue()
print(q)

# for data in inp:
#     if len(data) == 1:
#         if q.isEmpty():
#             print("-1")
#         else:
#             print(f'Pop {q.pop()} size in queue is {q.size()}')
#     else:
#         n = data.split(" ")[1]
#         print(f'Add {n} index is {q.size()}')
#         q.push_back(n)

# if q.isEmpty():
#     print("Empty")
# else:
#     print(f'Number in Queue is :  {str(q)}')