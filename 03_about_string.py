course_name = 'Learning Python'

# get char from string
print(course_name[0], type(course_name[0])) # L
print(course_name[1]) # e
print(course_name[-1]) # n
print(course_name[-2]) # o

# Slice
print(len(course_name)) # 15
print(course_name[9:len(course_name)]) # Python

# Split
splited_course_name = course_name.split()# default delemiter is any whitespace
print(splited_course_name)# ['Learning', 'Python']
course_name = 'Learning-Python'
splited_course_name = course_name.split('-')# split by separator/delimiter
print(splited_course_name)# ['Learning', 'Python']

name = 'Unsha'
message = f'Hello {name}!'# formatted string

print(message.upper())
print(message.lower())
print(message.title())
print(message.find('l'))# index of the first occurrence (-1 if not found)
print(message.replace('U', 'A'))# case sensitive

print('Python' in course_name)# True
