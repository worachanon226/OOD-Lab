class van:
    def __init__(self,num,time):
        self.num = int(num)
        self.time = int(time)
    
    def __lt__(self,o):
        if self.time == o.time:
            return self.num < o.num
        return self.time < o.time
    
    def __repr__(self):
        return str((self.num, self.time))

inp = input("Enter Input : ").split("/")
n, booking, q = int(inp[0]),[int(i) for i in inp[1].split()], []

for i in range(n):
    q.append(van(i+1,0))

for i in range(len(booking)):
    ready = q.pop(0)
    print(f'Customer {i+1} Booking Van {ready.num} | {booking[i]} day(s)')
    q.append(van(ready.num,int(booking[i])+ready.time))
    q.sort()