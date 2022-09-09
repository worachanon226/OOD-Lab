class node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

def createList(l=[]):
    head = cur = node(l[0])
    for i in range(1,len(l)):
        cur.next = node(l[i])
        if i < len(l):
            cur = cur.next
    return head

def printList(H):
    s = ""
    while H:
        s += str(H) + " "
        H = H.next
    print(s)

def mergeOrderesList(p,q):
    if p.data < q.data:
        head = cur = p
        p = p.next
    else:
        head = cur = q
        q = q.next
    
    while p or q:
        if p is not None and q is not None and int(p.data) <= int(q.data):
            cur.next = p
            p = p.next
        
        elif p is not None and q is not None and int(p.data) > int(q.data):
            cur.next = q
            q = q.next

        elif p is None and q is not None:
            cur.next = q
            q = q.next
        elif p is not None and q is None:
            cur.next = p
            p = p.next

        cur = cur.next
    return head

inp,L1, L2 = input("Enter 2 Lists : ").split(" "), [], []

for i in inp[0].split(","):
    L1.append(i)

for i in inp[1].split(","):
    L2.append(i)
        
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)