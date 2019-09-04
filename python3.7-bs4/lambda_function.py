import json
import re
import requests
from bs4 import BeautifulSoup as bs

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    prefix = 'https://www.youtube.com/channel/'
    suffix = '/about'
    channelId = event['id']

    res = requests.get(prefix + channelId + suffix)
    soup = bs(res.text, 'html.parser')

    aboutStat = soup.find_all('span', {'class': 'about-stat'})

    subscriber = re.search('(?<=<b>)[0-9,]+(?=</b>명)', str(aboutStat))
    if str(type(subscriber)) == "<class 're.Match'>":
        subscriber = subscriber.group().replace(',', '')
    else:
        subscriber = -1

    views = re.search('(?<=<b>)[0-9,]+(?=</b>회)', str(aboutStat))
    if str(type(views)) == "<class 're.Match'>":
        views = views.group().replace(',', '')
    else:
        views = None

    joinDate = re.search('(?<=가입일:)[0-9. ]*', str(aboutStat))
    if str(type(joinDate)) == "<class 're.Match'>":
        joinDate = joinDate.group()
    else:
        joinDate = None

    title = soup.find('meta', {'property':'og:title'})['content']
    content = soup.find('meta', {'property': 'og:description'})['content']
    image = soup.find('meta', {'property': 'og:image'})['content']

    channel = {
        'subscriber' : subscriber,
        'views' : views,
        'joinDate' : joinDate,
        'title' : title,
        'content' : content,
        'image' : image
    }

    return json.dumps(channel)

if __name__ == "__main__":
    response = lambda_handler({'id':'UC3SyT4_WLHzN7JmHQwKQZww'},{})
    print(response)