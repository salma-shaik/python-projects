import re

# print('\tTab')
# print(r'\tTab')

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890


Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )


coreyms.com

321-555-4321
123.555.1234
345*555.4292
800-555.4292
900-555.4292

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat


'''

sentence = 'Start a sentence and then bring it to an end'


# pattern = re.compile(r'abc')
# pattern = re.compile(r'cba')
# pattern = re.compile(r'.')  # . matches any char except new line
# pattern = re.compile(r'\.') # only . hence need to escape it so that every char is not matched
# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'\d') # \d - digit (0-9)
# pattern = re.compile(r'\D') # D - Not a digit (0-9)
# pattern = re.compile(r'\w') # w - word char (a-z) (A-Z) (0-9) _
# pattern = re.compile(r'\W') # W - not a word char
# pattern = re.compile(r'\s') # s - whitespace (space, tab, newline
# pattern = re.compile(r'\S') # S not s
# pattern = re.compile(r'\bHa') # b - word boundary before the word
# pattern = re.compile(r'\BHa') # B - that don't have a word boundary
# pattern = re.compile(r'^Start')  # ^ - matches chars at the beginning of a string
# pattern = re.compile(r'^tart')
# pattern = re.compile(r'end$') # $ - matches chars at the end of a string
# pattern = re.compile(r'nd$')
# pattern = re.compile(r'd$')
# pattern = re.compile(r'a$')
# pattern = re.compile(r'an end$')
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') # [] - char set. matches only the given chars. don't need to escape chars in char set
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[1-5]')
# pattern = re.compile(r'[a-z]')
# pattern = re.compile(r'[a-z][A-Z]')
# pattern = re.compile(r'[a-zA-Z]')
# pattern = re.compile(r'[^a-zA-Z]') # matches everything not in the char set. negates the char set
# pattern = re.compile(r'[^b]at')

# quantifiers - to match more than one char at once
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # * - 0 or more, + - 1 or more, ? - 0 or one, {3} - match exact no of digits here 3, {3,4} - matches the given range of no of digits


# pattern = re.compile(r'Mr\.?\s[A-Z]\w+')
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

# groups allow us to match several different patterns at once
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

#matches = pattern.finditer(text_to_search) #finditer returns all the matches with extra info and functionality

# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# matches = pattern.findall(text_to_search) # just returns the matches as a list of strings. If we are matching groups then it will only return groups
# matches = pattern.finditer(sentence)
# match - determines if the regex matches at the beginning of the string
# pattern = re.compile(r'Start')
# search - search the entire str for a pattern. just gives the 1 st  match it finds
# pattern = re.compile(r'dne')
# matches = pattern.match(sentence)
# matches = pattern.search(sentence)

# pattern = re.compile(r'start', re.IGNORECASE)
pattern = re.compile(r'start', re.I)
matches = pattern.search(sentence)

print(matches)

# for match in matches:
#     print(match)

# with open('persons_info_regex.txt', 'r') as f: camelCase [a-z][a-z]
#     contents = f.read()
#
#     matches = pattern.finditer(contents)
#
#     for match in matches:
#         print(match)

# print(text_to_search[1:4])