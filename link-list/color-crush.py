class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

    def __str__(self):
        return f'{self.value} {self.next}'

class LinkedList:
    def __init__(self):
        self.combo = 0
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + ""
        while cur.next != None:
            s += str(cur.next.value) + ""
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def addHead(self, item):
        NewNode = Node(item)
        if self.head == None:
            self.head = NewNode
            return  
        NewNode.next = self.head
        self.head = NewNode

    def size(self):
        cnt = 0
        tmp = self.head
        while tmp is not None :
            cnt += 1
            tmp = tmp.next
        return cnt

    def crush(self):
        cur = self.head
        prev = None
        while cur.next.next != None:
            if cur.value == cur.next.value == cur.next.next.value:
                if prev is None and cur.next.next.next is None:
                    self.head.next = None
                    self.head = None
                elif prev is None and cur.next.next.next is not None:
                    self.head = cur.next.next.next
                    if cur.next.next.next.next is not None:
                        self.head.next = cur.next.next.next.next
                    else:
                        self.head.next = None
                elif prev is not None and cur.next.next.next is None:
                    self.head = prev
                    self.head.next = None
                elif prev is not None and cur.next.next.next is not None:
                    self.head = prev
                    self.head.next = cur.next.next.next
                self.combo += 1
                break
            prev = cur
            cur = cur.next

    def getCombo(self):
        return self.combo

l = LinkedList()
inp = input("Enter Input : ").split(" ")
for data in inp:
    l.addHead(data)
    if l.size() > 2:
        l.crush()
print(l.size())
print(l)
if l.getCombo() > 1:
    print(f'Combo : {l.getCombo()} ! ! !')