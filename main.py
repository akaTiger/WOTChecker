import os
from wotChecker import *


if __name__ == "__main__":
    os.system("clear")
    obj = wot()
    print("\n\n\n_____________BASIC______________")
    print("WOT ID:", obj.id)
    print("Profile Name:", obj.name)
    print("Location:", obj.location)
    print(f"{obj.stats[1]}: {obj.stats[0]}")
    print(f"{obj.stats[4]}: {obj.stats[2]}{obj.stats[3]}")
    print(f"{obj.stats[7]}: {obj.stats[5]}{obj.stats[6]}")
    print("\n\n\n______________ETS2______________")
    print(f"Truck: {obj.truck[0]}")
    print(f"{obj.truck[1]}: {obj.truck[2]}")
    print(f"{obj.truck[3]}: {obj.truck[4]}")
    print(f"{obj.truck[5]}: {obj.truck[6]}")
    print(f"{obj.truck[7]}: {obj.truck[8]}")
    print(f"{obj.truck[9]}: {obj.truck[10]}")
    print(f"{obj.truck[11]}: {obj.truck[12]}")
    print(f"{obj.truck[13]}: {obj.truck[14]}")
    print("\n\n\n______________ATS______________")
    print(f"Truck: {obj.truck[15]}")
    print(f"{obj.truck[16]}: {obj.truck[17]}")
    print(f"{obj.truck[18]}: {obj.truck[19]}")
    print(f"{obj.truck[20]}: {obj.truck[21]}")
    print(f"{obj.truck[22]}: {obj.truck[23]}")
    print(f"{obj.truck[24]}: {obj.truck[25]}")
    print(f"{obj.truck[26]}: {obj.truck[27]}")
    print(f"{obj.truck[28]}: {obj.truck[29]}")
    
    
    
    
    print("\n\n\n")