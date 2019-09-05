import re
import requests
from bs4 import BeautifulSoup as bs

def crawling(channelId):
    prefix = 'https://www.youtube.com/channel/'
    suffix = '/about'

    res = requests.get(prefix + channelId + suffix)
    soup = bs(res.text, 'html.parser')

    aboutStat = soup.find_all('span', {'class': 'about-stat'})

    subscriber = re.search('(?<=<b>)[0-9,]+(?=</b>명)', str(aboutStat))
    if str(type(subscriber)) == "<class 're.Match'>":
        subscriber = subscriber.group().replace(',', '')
    else:
        subscriber = -1

    channelLog = {
        'subscriber': subscriber
    }

    return channelLog