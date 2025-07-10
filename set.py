#set() = {} unordered and immutable , but add/remove ok ... no duplicates 
# we cant change the value of set ..indexing dont work
fruits={"apple","orange","cherry","mango","grapes","banana","coco","coco"}

print(len(fruits))
print(type(fruits))

fruits.add("cat")
fruits.pop()  # it is random 
print(fruits)

#TUPLES =() ordered , unchangeble , duplicate , faster than list

