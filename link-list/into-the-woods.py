class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

    def __str__(self):
        return f'{self.value} {self.next}'

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

    def manageTree(self):
        if self.size() >= 2:
            head = self.head
            tmp = head.next
            while int(head.value) >= int(tmp.value):
                if tmp.next is not None:
                    tmp = tmp.next
                else:
                    self.head.next = None
                    return 
            self.head.next = tmp


l = LinkedList()
inp = input("Enter Input : ").split(",")
for data in inp:
    opr = data.split(" ")
    if opr[0] == 'A':
        l.addHead(opr[1])
        l.manageTree()
    if opr[0] == 'B':
        print(l.size())