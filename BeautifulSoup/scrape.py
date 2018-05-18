import requests
from bs4 import BeautifulSoup 
url = 'https://opentrolley.com.sg/subcategory/antiques-collectibles/toys';
html = BeautifulSoup(requests.get(url).text, "html.parser")


items = html.find_all('div', {'class': 'book w3-row'})
#items = html.find_all('div', {'class': 'book-control w3-col l3 m3 s-margin-top-sm'})

#print(html)
#print(items)
#print(len(items), " items found")

for item in items:
    print('')
    print("Name: ", item.find('div', {'class': "book-title"}).text)
    #print("PriBlk: ", item.find_all('div', {'class': "price-after-disc"}))
    #print("", item.find('p', {'class': "skuthumb"}).text)