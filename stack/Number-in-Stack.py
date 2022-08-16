class ManageStack():
    def __init__(self):
        self.items = []

    def add(self,i):
        self.items.append(i)

    def pop(self):
        if self.isEmpty():
            print("-1")
        else:
            return self.items.pop()
    
    def delete(self,i):
        self.pop(self.items.find(i))

    def lessThanDelete(self,i):
        for k in range(len(self.items)):
            if int(self.items[k]) < int(i):
                self.items.pop()
    
    def isEmpty(self):
        return self.items == self.size()
    
    def size(self):
        return len(self.items)