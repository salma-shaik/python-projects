import re

urls = '''
https://www.google.com
https://youtube.com
http://yahoo.com
https://www.nasa.gov
'''
# ? makes s optional
# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')


# back references which reference the group
subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

# matches = pattern.finditer(urls)
#
# for url in matches:
#     # print(url)
#     #print(url.group(0)) # entire martch i.e the entire url
#     # print(url.group(1))
#     # print(url.group(2))
#     print(url.group(3))