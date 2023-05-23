def greet_user(name="Foo"): # default value
  print(f"Hiya {name}!")
  
greet_user("Foo Bar")
greet_user()
# greet_user("Foo", "Bar") # Runtime ERROR!
# Hiya Foo Bar!
# Hiya Foo!

def square(number): # no define return!
  return number + number # got a return "surprise hahaha!"
print("square(2):", square(2))
# square(2): 4
