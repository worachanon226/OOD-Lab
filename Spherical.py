import math

class Spherical:

    def __init__(self,radius):
        self.radius = radius

    def changeR(self,Radius):
        self.radius = Radius

    def findVolume(self):
        return round(4/3,16) * round(math.pi,15) * self.radius * self.radius * self.radius

    def findArea(self):
        return 4 * math.pi * self.radius * self.radius

    def __str__(self):
        str = f'Radius ={self.radius} Volumn = {self.findVolume()} Area = {self.findArea()}'
        return str


r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)