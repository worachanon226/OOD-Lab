class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    def str_reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, ""
        while cur.next is not None:
            cur = cur.next
        while cur.previous is not None:
            s += str(cur.data) + " "
            cur = cur.previous
        return s
    
    def isEmpty(self):
        return self.head is None

    def append(self,data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            return 
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = newNode
        newNode.previous = cur

    def size(self):
        cur, cnt = self.head, 0
        while cur is not None:
            cnt += 1
            cur = cur.next
        return cnt

    def insert(self,index,data):
        index = int(index)
        cur = self.head
        newNode = Node(data)
        if index < 0 or index > self.size():
            return
        if index == 0 and self.size() == 0:
            self.head = newNode
            return 
        elif index == 0:
            cur.previous = newNode
            newNode.next = cur
            self.head = newNode
            return 
        for i in range(index-1):
            cur = cur.next
        newNode.previous = cur.previous
        cur.previous.next = newNode
        newNode.previous = cur.previous
        newNode.next = cur
        return 

    def remove(self,data):
        if self.isEmpty():
            return 
        cur = self.head
        while cur is not None:
            if cur.data == data:
                print(cur.data)
                if cur.previous is None and cur.next is None:
                    self.head = None
                    self.head.previous = None
                    self.head.next = None
                elif cur.previous is None and cur.next is not None:
                    self.head = cur.next
                    self.head.previous = None
                elif cur.previous is not None and cur.next is None:
                    print(cur.previous.data)
                elif cur.previous is not None and cur.next is not None:
                    cur.previous.next = cur.next
                    cur.next.previous = cur.previous
                return 
            cur = cur.next
        return 

l = DoublyLinkedList()
inp = input("Enter Input : ").split(",")
for data in inp:
    task = data.strip().split(" ")
    if task[0] == "A":
        l.append(task[1])
    if task[0] == "Ab":
        l.insert(0, task[1])
    if task[0] == "I":
        opr = task[1].split(":")
        l.insert(opr[0], opr[1])
    if task[0] == "R":
        l.remove(task[1])
    print(l)

        

        