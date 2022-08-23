class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        NewNode = Node(item)
        if self.head == None:
            self.head = NewNode
            return 
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode

    def addHead(self, item):
        NewNode = Node(item)
        if self.head == None:
            self.head = NewNode
            return 
        NewNode.next = self.head
        self.head = NewNode

    def search(self, item):
        tmp = self.head
        for i in range(self.size()):
            if tmp.value == item:
                return "Found"
            tmp = tmp.next
        return "Not Found"

    def index(self, item):
        tmp = self.head
        for i in range(self.size()):
            if tmp.value == item:
                return i
            tmp = tmp.next
        return -1

    def size(self):
        cnt = 0
        tmp = self.head
        while(tmp != None):
            cnt += 1
            tmp = tmp.next
        return cnt
        
    def pop(self, pos):
        if pos < 0 or pos >=self.size():
            return "Out of Range"
        else:
            tmp = self.head
            for i in range(pos-1):
                tmp = tmp.next
            tmp.next = tmp.next.next
            return "Success"                
        
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1}".format(L.search(i[3:]), i[3:]),end="")
        print(f' in {L}')
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)