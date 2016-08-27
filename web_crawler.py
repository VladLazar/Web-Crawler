import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "<Set URL>" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.find_all('a', {'class': 'title text-semibold'}):
            href = link.get('href')
            # print(href)
            get_single_topic_data(href)
        page += 1


def get_single_topic_data(topic_url):
    source_code = requests.get(topic_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for topic_name in soup.find_all('h1' , {'class': '<Set Class>'}):
        print (topic_name.string)

trade_spider(1)
