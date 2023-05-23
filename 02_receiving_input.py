# receiving input
import datetime

today = datetime.date.today()
year = today.year

birth_year = int(input('Birth year: '))# casting from string input into int variable
print(f'Your birth year is: {birth_year}, You are {year - birth_year}.')
birth_year = str(birth_year)
print(birth_year) 
birth_year = float(birth_year)
print(birth_year)
