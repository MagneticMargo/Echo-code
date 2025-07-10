

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()


# 2x2 list

food =["rice","pulse","pizza","burger"]
car=["bugati","audi","bmw","jaugar"]
dress=["frock","shorts","pants","shirt"]

items= [[food],
        [car],
        [dress]]

for meow in items:
    for cat in meow:
        print(items, end=" ")
    print()


#3
groceries = [["apple",'mango','banana','coconut'],
             ['celery','carrots','potatoes','rice'],
             ['cat','dog','eleu','lino']]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
   
