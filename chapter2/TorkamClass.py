class Torkam:
    def __init__(self,inp):
        self.ls = []
        opr = ""
        txt = ""
        inp = inp.split(",")
        for i in range(0,len(inp)):
            if ' ' in inp[i]:
                opr = inp[i].split(" ")[0]
                txt = inp[i].split(" ")[1]
            else:
                opr = inp[i]
            if opr == 'P':
                self.play(txt)
            elif opr == 'R':
                self.restart()
            elif opr == 'X':
                self.ext()
            else:
                print(f'\'{inp[i]}\' is Invalid Input !!!')
                exit(0)

    def play(self,txt):
        if len(self.ls) == 0:
            self.ls.append(txt)
            print(f'\'{txt}\' -> { self.ls}')

        elif self.ls[-1][-2].lower() == txt[0].lower() and self.ls[-1][-1].lower() == txt[1].lower():
            self.ls.append(txt)
            print(f'\'{txt}\' -> { self.ls}')
            
        else:
            print(f'\'{txt}\' -> game over')

    def restart(self):
        self.ls.clear()
        print("game restarted")
    
    def ext(self):
        exit(0)

print("*** TorKham HanSaa ***")
game = Torkam(input("Enter Input : "))
        