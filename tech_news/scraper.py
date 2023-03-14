import requests
import time
from parsel import Selector

url = 'https://blog.betrybe.com/'
# Requisito 1


def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        headers = {'User-Agent': 'Fake user-agent'}
        web_page = requests.get(url, headers)
        if web_page.status_code == 200:
            webtext = web_page.text
            return webtext
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    return selector.css('.entry-title > a::attr(href)').getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
