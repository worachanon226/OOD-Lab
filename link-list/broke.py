class Node():
    def __init__(self, w, f):
        self.weight = w
        self.frequency = f
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.weight) + " "
        while cur.next != None:
            s += str(cur.next.weight) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def addHead(self, item):
        NewNode = item
        if self.head == None:
            self.head = NewNode
            return 
        NewNode.next = self.head
        self.head = NewNode

    def size(self):
        cnt = 0
        tmp = self.head
        while(tmp != None):
            cnt += 1
            tmp = tmp.next
        return cnt
        
    def pop(self, pos):
        if pos < 0 or pos >=self.size():
            return 
        else:
            tmp = self.head
            for i in range(pos-1):
                tmp = tmp.next
            tmp.next = tmp.next.next

    def brokeDisk(self):
        if self.size() >= 2:
            head = self.head
            tmp = head.next
            while int(head.weight) > int(tmp.weight):
                print(f'{tmp.frequency}')
                if tmp.next:
                    tmp = tmp.next
                else:
                    self.head.next = None
                    return 
            self.head.next = tmp
            

inp = input("Enter Input : ").split(",")
l = LinkedList()
for data in inp:
    disk = data.split(" ")
    l.addHead(Node(disk[0],disk[1]))
    l.brokeDisk()