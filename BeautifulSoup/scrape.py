import requests
from bs4 import BeautifulSoup 
url = 'https://www.seek.com.au/PHP-jobs/in-All-Melbourne-VIC'
html = BeautifulSoup(requests.get(url).text, "html.parser")

foundCount = html.find('strong', {'data-automation': 'totalJobsCount'})
#items = html.find_all('div', {'class': 'book-control w3-col l3 m3 s-margin-top-sm'})
#print(items)
print(foundCount.text)
#print(len(items), " items found")

#for item in items:
    #print('')
    #print(item)
    #print("Count: ", item.find('strong', {'class': 'lwHBT6d'}))
    #print("PriBlk: ", item.find_all('div', {'class': "price-after-disc"}))
    #print("", item.find('p', {'class': "skuthumb"}).text)