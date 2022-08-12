class Calculator :

    def __init__(self,x):
        self.x = x

    def __add__(self,ob):
        return self.x + ob.x
        

    def __sub__(self,ob):
        return self.x - ob.x
        

    def __mul__(self,ob):
        return self.x * ob.x
        

    def __truediv__(self,ob):
        return self.x / ob.x
        

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")