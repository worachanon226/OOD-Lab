print(" *** Wind classification ***")
spd = float(input("Enter wind speed (km/h) : "))
print("Wind classification is ",end="")
if spd >= 209 :
    print("Super Typhoon.")
elif spd >= 102 :
    print("Typhoon.")
elif spd >= 56 :
    print("Tropical Storm.")
elif spd >= 52 :
    print("Depression.")
else :
    print("Breeze.")