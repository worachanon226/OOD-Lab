def hbd(yr):
    if yr % 2 == 0:
        base = yr/2
        base = int(base)
        return  f'saimai is just 20, in base {base}!'
    else:
        base = (yr-1) / 2
        base = int(base)
        return  f'saimai is just 21, in base {base}!'

yr = input("Enter year : ")

print(hbd(int(yr)))