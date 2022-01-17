import requests
from bs4 import BeautifulSoup as bs
import logging
import pandas as pd

url = ('https://portalcafebrasil.com.br/todos/podcasts')

#ret = requests.get(url)

#soup = bs(ret.text)

#print(soup.find('h5').a['href'])

#listPodcast = soup.find_all('h5')

#for item in listPodcast:
#    print(f'Ep: {item.text}, link: {item.a["href"]}')

#get all podcasts:

url = 'https://portalcafebrasil.com.br/todos/podcasts/page/{}/?ajax=true'    

#fill page parameter:
#print(requests.get(url.format(5)).text)

def get_podcast(url):
    ret = requests.get(url)
    soup = bs(ret.text)
    return soup.find_all('h5')

#print(get_podcast(url.format(5)))

log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)



i = 1
listPodcast = []
listGet = get_podcast(url.format(i))

log.debug(f"{len(listGet)} Data retrieved from link: {url.format(i)}")

while len(listGet) > 0:
    listPodcast = listPodcast + listGet
    i += 1
    listGet = get_podcast(url.format(i))
    #log.debug(f"{len(listGet)} Data retrieved from link: {url.format(i)}")

df = pd.DataFrame(columns=['name', 'link'])

print(df.shape)

for item in listPodcast:
    df.loc[df.shape[0]] = [item.text, item.a["href"]]

print(df.shape)    

df.to_csv("podcasts.csv", sep=";", index=False)





