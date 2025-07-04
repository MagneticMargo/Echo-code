#pyhton wt convertor

wt = float(input("Enter your wt:"))
unit = input("kg or pounds? (K or L): ")
if unit == "K" :
    wt = wt* 2.205
    unit = "Lbs."
    print(f"your wt is :{round(wt,1)}{unit}")
elif unit == "L" :
    wt =wt/2.205
    unit = "Kgs."
    print(f"your wt is :{round(wt,1)}{unit}")
else : 
    print(f"{unit}was not valid")
