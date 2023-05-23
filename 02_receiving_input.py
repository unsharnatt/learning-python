# receiving input
import datetime

today = datetime.date.today()
year = today.year

birth_year = int(input('Birth year: '))# converting from string input into int variable
print(f'Your birth year is: {birth_year}, You are {year - birth_year}.')
