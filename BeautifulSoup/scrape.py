import requests
from bs4 import BeautifulSoup 

keywordArray = ['PHP','PMP', 'ITIL']
arr = []
for keyword in keywordArray:
    url = 'https://www.seek.com.au/'+ keyword +'-jobs/in-All-Melbourne-VIC'
    html = BeautifulSoup(requests.get(url).text, "html.parser")
    foundCount = html.find('strong', {'data-automation': 'totalJobsCount'})
    arr.append(foundCount.text)

print(arr)