# List, Set and Dictionary are mutable(editable)
# list = []
# set = {}
# dict = {key: val}
# tuples = ()

# ***List***
# strong order
# store duplicated
# able to access/insert by index
numbers = [1, 2, 3,4 ,5, "6"]
print(numbers)
print("numbers[0]", numbers[0])
print("numbers[1]", numbers[1])
print("numbers[-1]", numbers[-1])
print("numbers[-2]", numbers[-2])

numbers.append(6)
print("numbers.append(6)", numbers)

numbers.insert(0, 6)
print("numbers.insert(0, 6)", numbers)

numbers.remove(6)
print("numbers.remove(6)", numbers)

numbers.pop()
print("numbers.pop()", numbers.pop())
print("numbers", numbers)

print("numbers.index(4)", numbers.index(4)) # error if not in list

numbers.reverse()
print("numbers.reverse()", numbers)

numbers.sort()
print("numbers.sort()", numbers)

numII = numbers.copy()
print("numbers.copy()", numII)

numbers.clear()
print("numbers.clear()", numbers)


# ***Dictionaries***
# store key-value pairs
# no duplicated name
# no sequence
customer = {
  "name": "Johny Walking",
  "age": 32,
  "is_valid": True
}

print("customer name:", customer["name"])

# print("customer name:", customer["type"]) # ERROR!!!
print("customer name:", customer.get("name", "Jocker"))# Default value

customer["name"] = "Alan Butter"
print("customer name:", customer["name"])


# ***Sets***
# Once a set is created, you cannot change its items, 
# but you can add new items.
# XXX no sequence ordered
# XXX no duplicate item (allow to add)
myset = {"apple", "banana", "banana", "cherry", True, 1}
print("myset:", myset)

for x in myset:
  print("myset", x)

print("is banana in set?","banana" in myset)

myset.add("orange")
print("added orange:", myset)

tropical = {"pineapple", "mango", "papaya"}
myset.update(tropical)
print("updated myset by add item from another set:\n", myset)

mylist = ["kiwi", "orange"]
myset.update(mylist)
print("updated myset by add item from another list:\n", myset)

set1 = {"apple"}
set2 = {"banana"}
set3 = set1.union(set2)
print("set1 union set2 = set3:", set3)

myset.remove("banana") 
print("myset after removed banana:\n", myset)
# myset.remove("banana") # XXX error if not exist
# print("myset after removed banana again:", myset)
myset.discard("banana")
print("myset after removed banana again by using discard:\n", myset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop() # XXX randomly remove item
print("pop set:", x)
print("set after poped:", thisset)

thisset.clear()
print("clear set:", thisset)
del thisset
# print("del set:", thisset) XXX error no more thisset ref. after del


# Read-Only list
# *** Tuples ***
items = (1, 2, 3, "4")
print("my tuples", items)

x, y, z, a = items
print(x, y, z, a)

