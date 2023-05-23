def fibo(terms):
  a, b = 0, 1
  for i in range(0, terms):
    yield f"{i+1}: {a}" # using yield (generator) 
    a, b = b, a + b

for item in fibo(10):
  print(item)