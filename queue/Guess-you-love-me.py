class Queue:
    def __init__(self):
        self.items = []

    def push_back(self,i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0
    
    def __str__(self):
        return ", ".join(self.items)
   
activity = ["Eat","Game","Learn","Movie"]
place = ["Res.","ClassR.","SuperM.","Home"]

me, you,point = Queue(),Queue(),0
ls_me, ls_you = [],[]

inp = input("Enter Input : ").split(",")
for data in inp:
    ac = data.split(" ")
    me.push_back(ac[0])
    you.push_back(ac[1])

print(f'My   Queue = {me}')
print(f'Your Queue = {you}')

while not me.isEmpty():
    top_me, top_you = me.pop(), you.pop()

    ls_me.append(f'{activity[int(top_me[0])]}:{place[int(top_me[2])]}')
    ls_you.append(f'{activity[int(top_you[0])]}:{place[int(top_you[2])]}')

    if top_me[0] == top_you[0] and top_me[2] != top_you[2]:
        point += 1
    elif top_me[0] != top_you[0] and top_me[2] == top_you[2]:
        point += 2
    elif top_me[0] == top_you[0] and top_me[2] == top_you[2]:
        point += 4
    else:
        point -= 5

print("My   Activity:Location = ",end="")
print(", ".join(ls_me))
print("Your Activity:Location = ",end="")
print(", ".join(ls_you))

if point >= 7:
    print(f'Yes! You\'re my love! : Score is {point}.')
elif point > 0:
    print(f'Umm.. It\'s complicated relationship! : Score is 4.')
else:
    print(f'No! We\'re just friends. : Score is {point}.')

        