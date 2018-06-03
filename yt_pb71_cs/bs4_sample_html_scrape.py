from bs4 import BeautifulSoup
import requests

with open('bs4_sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())

# # gets the 1st tag match on the page
# match = soup.title.text
# print(match)
#
# # 1st div on the page
# match = soup.div
# print(match)

# # with find method, we can pass down the args of attrs which narrow down exactly what we are trying to find
# match = soup.find('div', class_='footer')
# print(match)

# # get an article headlines and summaries from page. find - returns the 1st tag that matches the arg
# article = soup.find('div', class_='article')
# # print(article)
#
# headline = article.h2.a.text
# print(headline)
#
# summary = article.p.text
# print(summary)

# get all the articles with find all
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()


