#typecasting = the process of coverting a value of one data type to another 
#we can do it explicitly and implicitly 

name = "magnetic"
age = 20
student = True
gpa = 8.9

print(type(name))
print(type(age))
print(type(student))
print(type(gpa))
print(age)

# explicit conversion : it is done manually
age = float(age)
print(type(age))
print(age)

gpa=int(gpa)
print(type(gpa))
print(gpa)

student=str(student)
print(type(student))
print(student)

# implicit conersion : it is done automatically
x=2
y=2.0
x=x/y
print(x)
print(type(x))
print(f"x is : {x}")

