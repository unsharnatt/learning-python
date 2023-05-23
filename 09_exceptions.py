try:
  age = int(input('age:'))# try 0 and fourty
  income = 20000
  risk = income / age
  print(age)

except ValueError:
  print("Not a valid number!")
except ZeroDivisionError:
  print("Age cannot be zero!")
# except:
#   print('An exception occurred')