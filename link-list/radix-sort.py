class Node:
    def __init__(self,v = 0):
        self.value = v
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        if self.isEmpty():
            return ""
        cur, s = self.head, str(self.head.value)
        while cur.next != None:
            s +=  " " +str(cur.next.value)
            cur = cur.next
        return s

    def toStirng(self):
        if self.isEmpty():
            return ""
        cur, s = self.head, str(self.head.value)
        while cur.next != None:
            s +=  " -> " +str(cur.next.value)
            cur = cur.next
        return s
        
    def isEmpty(self):
        return self.head == None

    def size(self):
        cur, cnt = self.head, 0
        while cur is not None:
            cnt += 1
        return cnt

    def dequeue(self):
        if self.isEmpty():
            return 
        head = self.head
        v = head.value
        if head.next is None:
            self.head = None
        else:
            self.head = head.next
        return v
    
    def enqueue(self,value):
        newNode = Node(value)
        if self.isEmpty():
            self.head = newNode
            return 
        cur = self.head 
        while cur.next is not None:
            cur = cur.next
        cur.next = newNode

class Radixsort:
    ch = 0
    def setCh(self):
        self.ch = 1

    def sort(self,l):
        lq = LinkedQueue()
        for i in l:
            lq.enqueue(i)
        lqs = [LinkedQueue() for _ in range(10)]
        i = 0
        while 1:
            i += 1
            print(f'Round : {i}')
            pos, neg = [], []
            while not lq.isEmpty():
                num = int(lq.dequeue())
                pos.append(num) if num >= 0 else neg.append(num)
            neg.reverse()
            for item in neg:
                num = item
                idx = self.get_idx(-1*int(num), i)
                lqs[idx].enqueue(num)
            for item in pos:
                num = item
                idx = self.get_idx(int(num), i)
                lqs[idx].enqueue(num)
            for k in range(10):
                if not lqs[k].isEmpty():
                    temp_l = []
                    while not lqs[k].isEmpty():
                        temp_l.append(lqs[k].dequeue())
                    temp_l.sort()
                    for kk in temp_l:
                        lqs[k].enqueue(kk)
                print(f'{k} : {lqs[k]}')
            print("------------------------------------------------------------")
            ch = 0
            for j in range(1,10):
                if not lqs[j].isEmpty():
                    ch = 1
            for j in range(10):
                while not lqs[j].isEmpty():
                    lq.enqueue(lqs[j].dequeue())
            if not ch:
                self.rnd = i-1
                return lq
        return lq

    def get_idx(self,n,d):
        for _ in range(d-1):
            n //= 10
        return n % 10
    
    def get_round(self):
        return self.rnd
        
rs = Radixsort()
l = LinkedQueue()
inp = input("Enter Input : ").split(" ")
for data in inp:
    if int(data) >= 0:
        rs.setCh()
    l.enqueue(data)
print("------------------------------------------------------------")
lq = rs.sort(inp)
print(f'{rs.get_round()} Time(s)')
print(f'Before Radix Sort : {l.toStirng()}')
print(f'After  Radix Sort : {lq.toStirng()}')




        
            
        