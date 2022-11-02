class hash:
    def __init__(self,size,maxcol,threshold):
        self.size = size
        self.maxcol = maxcol
        self.threshold = threshold
        self.table = [None] * size

    def insert(self,value):
        idx = 0
        if not self.isFull():
            idx = value % self.size

            if self.table[idx] is None:
                self.table[idx] = value

            elif self.table[idx] is not None:
                r, newidx = 0, idx
                print(f'collision number {r+1} at {newidx}')

                while self.table[newidx] is not None:
                    r += 1
                    newidx = (idx + r * r) % self.size

                    if self.maxcol <= r:
                        print("****** Max collision - Rehash !!! ******")
                        return False
                    
                    if self.table[newidx] is None:
                        self.table[newidx] = value
                        break

                    print(f'collision number {r+1} at {newidx}')
            return True
        else:
            print("****** Data over threshold - Rehash !!! ******")
            return False
        
    def isFull(self):
        s, ch = int(self.size * self.threshold / 100), 0
        for i in self.table:
            if i is not None:
                ch += 1
        if ch >= s:
            return True
        return False

    def __str__(self):
        s = ""
        for i in range(len(self.table)):
            s += f'#{i+1}'+ " " * (7-len(str(i+1))) + f'{self.table[i]}\n'
        return s

def nextprime(value):
    while value:
        value += 1
        for i in range(2,value):
            if value % i == 0:
                break
            if i == value-1:
                return value

print(" ***** Rehashing *****")
inp = input("Enter Input : ").split("/")

size, maxcol, threshold = map(int, inp[0].split())
data = list(map(int, inp[1].split()))
Hash = hash(size, maxcol, threshold)

print("Initial Table :")
print(Hash,end="----------------------------------------\n")

lastadd, notall = -1, True
while notall:
    for i in range(len(data)):
        if i >= lastadd + 1:
            print(f'Add : {data[i]}')
        if not Hash.insert(data[i]):
            Hash = hash(nextprime(Hash.size * 2),maxcol,threshold)
            lastadd = i
            break
        else:
            if i >= lastadd:
                print(Hash,end="----------------------------------------\n")
        if i == len(data)-1:
            notall = False