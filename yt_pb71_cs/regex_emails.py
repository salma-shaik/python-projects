import re

emails = '''
JustinMPorter@gmail.com
jamie.jensen@university.edu
tom-321-jones@my-work.net
'''

# Sample regex for email

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')

matches = pattern.finditer(emails)

for match in matches:
    print(match)
