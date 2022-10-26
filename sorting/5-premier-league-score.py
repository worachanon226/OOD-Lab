class Team:
    def __init__(self,name,points,gd):
        self.name = name
        self.points = points
        self.gd = gd
    
    def __lt__(self,o):
        if self.points == o.points:
            return self.gd > o.gd
        return self.points > o.points
    
    def __repr__(self):
        s = str("['" + str(self.name) + "', {'points': " + str(self.points) + "}, {'gd': " + str(self.gd) + "}]")
        return s
l, team = [], input("Enter Input : ").split("/")
for i in team:
    stat = i.split(",")
    name, wins, loss, draws = stat[0], stat[1],stat[2],stat[3]
    scored, conceded = stat[4], stat[5]
    points = 3 * int(wins) + int(draws)
    gd = int(scored) - int(conceded)
    l.append(Team(name,points,gd))
l.sort()
print("== results ==")
for i in l:
    print(i)