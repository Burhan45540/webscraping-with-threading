import threading
import requests
from bs4 import BeautifulSoup
urls=[
  'https://en.wikipedia.org/wiki/Muhammad',
  'https://en.wikipedia.org/wiki/Ali',
  'https://en.wikipedia.org/wiki/Dawoodi_Bohra'
]

def fetch_content(url):

  response=requests.get(url)
  soup=BeautifulSoup(response.content,'html.parser')
  print(f"Fetched {(soup.text)} characters from this {url}")


threads=[]

for url in urls:
  t=threading.Thread(target=fetch_content,args=(url,))
  threads.append(t)
  t.start()


for i in threads:
  i.join()