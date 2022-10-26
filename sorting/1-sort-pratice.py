l = input("Enter Input : ").split(" ")
for i in range(1,len(l)):
    if int(l[i]) > int(l[i-1]):
        continue
    else:
        print("No")
        exit(0)
print("Yes")