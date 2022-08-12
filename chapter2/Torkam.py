print("*** TorKham HanSaa ***")
inp = input("Enter Input : ").split(",")
ls = []

for i in range(0,len(inp)):
    if ' ' in inp[i]:
        opr = inp[i].split(" ")[0]
        txt = inp[i].split(" ")[1]
    else:
        opr = inp[i]

    if opr == 'P':
        if len(ls)==0:
            ls.append(txt)
            print(f'\'{txt}\' -> {ls}')
        elif ls[-1][-2].lower() == txt[0].lower() and ls[-1][-1].lower() == txt[1].lower():
            ls.append(txt)
            print(f'\'{txt}\' -> {ls}')
        else:
            print(f'\'{txt}\' -> game over')
    elif opr == 'R':
        ls.clear()
        print("game restarted")
        
    elif opr == 'X':
        exit(0)
    else:
        print(f'\'{inp[i]}\' is Invalid Input !!!')
        exit(0)
        