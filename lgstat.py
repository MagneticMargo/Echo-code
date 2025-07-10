#logical oprators = used on condtional statements
# and = check two or more coditions if True , if one stat. is false so entire stat. will go flase 
# or = cheks if at least one condtion is true then it is true
# not = (it converts) True if condtion is Flase and vice versa 

#for "or"

temp = float(input("Enter the temp : "))
sunny = True 
if temp <=0 or temp >=30 :
    print("the temperature is bad")
else:
    print("the temperature is good")

# for "not"

if temp <=0 or temp >=30:
    print("the temp is bad")
else :
    print("the temp is good")

if not sunny :
    print("It is cloudy outside")
else:
    print("It is sunny outside")

# for "and"

if temp > 0 and temp <30:
    print("The temp is good")
else:
    print("the temp is bad")
