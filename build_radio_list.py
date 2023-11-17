import pdb
from turtle import pd
import requests
from bs4 import BeautifulSoup


PAGES = 2
BASE_URL = 'https://www.gcores.com'
RADIO_LIST_URL = "https://www.gcores.com/radios?page={}"
LIVE_STREAM_TEMPLATE = """SiiNunit
{
live_stream_def: gcores {
    %s
}
}"""

RECORD_TEMPLATE = 'stream_data[{count}]: "{url}|{title}|{category}|CN|0|0"\n'


latest_radio_list = []


def get_radio_info(radio_link):
    response = requests.get(BASE_URL + radio_link)
    soup = BeautifulSoup(response.text)
    # import pdb;pdb.set_trace()
    mp3 = soup.select('a[href*=".mp3"]')[0].get('href')
    if not soup.select('a[href*=".mp3"]'):
        return None, None
    category = soup.select('span.original_category')[0].get_text()
    return mp3, category


def generate_gadio_list():
    count = 0
    live_stream_str = ''
    for page in range(PAGES):
        response = requests.get(RADIO_LIST_URL.format(page + 1))
        soup = BeautifulSoup(response.text)
        # import pdb;pdb.set_trace()
        for radio in soup.select('a[href*="radios/"]'):
            title = radio.get_text().replace('|', ',')
            link = radio.get('href')
            mp3, category = get_radio_info(link)
            if mp3 or category:
                live_stream_str += RECORD_TEMPLATE.format(count=count, url=mp3, title=title, category=category)
                count += 1
    live_stream_str = f"stream_data: {count}\n" + live_stream_str
    return LIVE_STREAM_TEMPLATE % live_stream_str    
