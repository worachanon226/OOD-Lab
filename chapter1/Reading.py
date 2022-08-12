print("*** Reading E-Book ***")
s = (input("Text , Highlight : "))
txt = s.split(",")[0]
hl = s.split(",")[1]
for i in range(0,len(txt)) :
    if txt[i] == hl:
        print("[",txt[i],"]",sep="",end="")
    else :
        print(txt[i],end="")