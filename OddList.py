def odd_list(al):
    list = []
    for i in range(0,len(al)):
        if al[i] % 2 !=0:
            list.append(al[i])
    return list


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)