class ManageStack():
    def __init__(self):
        self.items = []

    def add(self,i):
        self.items.append(i)
        print(f'Add = {i}')

    def pop(self):
        if self.isEmpty():
            print("-1")
        else:
            print(f'Pop = {self.items.pop()}')
    
    def delete(self,i):
        if self.isEmpty():
            print("-1")
        else:
            while i in self.items:
                self.items.pop(self.items.index(i))
                print(f'Delete = {i}')

    def lessThanDelete(self,i):
        if self.isEmpty():
            print("-1")
        else:
            ls = []
            for x in self.items:
                if int(x) < int(i) and x not in ls:
                    ls.append(x)
            ls.reverse()
            for x in ls:
                self.items.pop(self.items.index(x))
                print(f'Delete = {x} Because {x} is less than {i}')

    def moreThanDelete(self,i):
        if self.isEmpty():
            print("-1")
        else:
            ls = []
            for x in self.items:
                if int(x) > int(i) and x not in ls:
                    ls.append(x)
            ls.reverse()
            for x in ls:
                self.items.pop(self.items.index(x))
                print(f'Delete = {x} Because {x} is more than {i}')
        
    
    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.items)

    def __str__(self):
        return ", ".join(self.items)

inp = input("Enter Input : ").split(",")

s = ManageStack()

for data in inp:
    if len(data) == 1:
        s.pop()
    else:
        t = data.split(" ")
        if t[0] == "A":
            s.add(t[1])
        if t[0] == "D":
            s.delete(t[1])
        if t[0] == "MD":
            s.moreThanDelete(t[1])
        if t[0] == "LD":
            s.lessThanDelete(t[1])
    
print(f'Value in Stack = [{s}]')