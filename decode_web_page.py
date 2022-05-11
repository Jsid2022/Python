import urllib.request
from bs4 import BeautifulSoup

f = open("Newyork_articles.txt", 'w')
html = 'http://www.nytimes.com/'
open_url = urllib.request.urlopen(html)
soup = BeautifulSoup(open_url, 'html.parser')
article_headings = soup.find_all(class_="indicate-hover")
head = "Articles for Today:\n"
i = 0
f.write(head)
for heading in article_headings:
    i += 1
    f.write("\n"+str(i)+"."+heading.string+"\n")
f.close()
