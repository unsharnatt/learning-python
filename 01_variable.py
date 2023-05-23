# auto type
product_name = 'Banana Ripe at Home(will turn to yellow soon)'
price_usd = 1.6
counter = 10
is_purchased = True

print(counter, type(counter))
print(price_usd, type(price_usd))
print(product_name, type(product_name))
print(is_purchased, type(is_purchased))

# Python Banana Ripe at Home(will turn to yellow soon) <class 'str'>
# 1.6 <class 'float'>
# 10 <class 'int'>
# True <class 'bool'>

# ***Try to play around to prove it, simulate to get results from different platform***
# is_purchased = False
is_purchased = is_purchased and "Y" or "N" # Y|N for some reason
print(is_purchased, type(is_purchased))
# Y <class 'str'>

is_purchased = 'No'
is_purchased = is_purchased.lower() in ("y","yes", "true", "t", "1")
print(is_purchased, type(is_purchased))# type casting from str to bool after getting result from other system/API
# False <class 'bool'>
