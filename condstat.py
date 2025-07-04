#conditonal expression = A one-line shortcut for thr if-else statement(trnanry opreator)
#                      it print or assign one of two values based on acondtion
#                       x if condtion else y {basic formula}

num = 5 
a = 6
b = 7
age = 13
tepm =20
user_role = "guest"

print("postive" if num>0 else "negative")
result = "even" if num % 2==0 else"ood"
max_num = a if a>b else b
min_num = a if a<b else b
status = "adult" if age >= 18 else"child"
weather = "hot" if tepm >=20 else "cold"
print(weather)
print(result)
print(max_num)
print(min_num)
print(status)
