import urllib2
from bs4 import BeautifulSoup

url = "http://www.steamcommunity.com/id/jadd22/friends"

r = urllib2.urlopen(url)
soup = BeautifulSoup(r)

friend = soup.find_all('div',{'class' : 'friendBlockContent'},{'class' : 'friendSmallText'})

for online in friend:
    online.extract()
    print('').join(online.findAll(text=True)).strip('\t\r\n')




