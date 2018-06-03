from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("http://coreyms.com").text

soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

# find one article
"""
# # grab 1st headline/article and summary
article = soup.find('article')

# print(article.prettify())

headline = article.h2.a.text
print(headline)

summary = article.find('div', class_='entry-content').p.text
print(summary)

vid_src = article.find('iframe', class_='youtube-player')['src']
# --> http://www.youtube.com/embed/VGgTmxXp7xQ?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent
# Need to get the vid id i.e 'VGgTmxXp7xQ'. We see that it comes after a / so let's split the string based on the /s
# print(vid_src)

vid_id = vid_src.split('/')[4]
# --> VGgTmxXp7xQ?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent
# comes before ? so need to split the above str on the basis of ?

vid_id = vid_id.split('?')[0]
print(vid_id)

# creare a utube vid link
yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
"""

csv_file = open('bs4_webdata_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headlines', 'summary', 'video_link'])

# find all articles
articles = soup.find_all('article')

for article in articles:
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'

    except Exception as e:
       # raise e or pass
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()

