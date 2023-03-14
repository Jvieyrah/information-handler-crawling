import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup
from tech_news.database import create_news

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
    selector = Selector(html_content)
    link =  selector.css(
         '.nav-links > a.next::attr(href)'
    ).get()
    if link is not None: 
        return link
    else:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    soup = BeautifulSoup(html_content, "html.parser")

    url = soup.find("link", rel="canonical").get("href")
    title = soup.find("h1", class_="entry-title").text.strip()
    timestamp = soup.find("li", class_="meta-date").text
    writer = soup.find("a", class_="url fn n").text
    reading_time = soup.find("li", class_="meta-reading-time").text[:2]
    summary = soup.find_all("p")[0].text.strip()
    category = soup.find("span", class_="label").text
    # print(summary)

    dict_news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time),
        "summary": summary,
        "category": category,
    }
    # print(dict_news)
    return dict_news
# def scrape_news(html_content):
#     """Seu código deve vir aqui"""
#     selector = Selector(html_content)
#     url = selector.css("link[rel='canonical']::attr(href)").get().strip()
#     title = selector.css('h1.entry-title::text').get().strip()
#     timestamp = selector.css('li.meta-date::text').get().strip()
#     writer = selector.css('span.author > a::text').get().strip(),
#     reading_time = int(
#             selector.css('li.meta-reading-time::text').get()[0:2]
#             )
#     summary = selector.css(
#         'div.entry-content:first-child > p::text'
#         ).get().strip() + selector.css(
#             'div.entry-content:first-child p > a::text'
#             ).get().strip()
#     category = selector.css('a.category-style > span.label::text').get().strip()

#     return {
#         'url': url,
#         'title': title,
#         'timestamp': timestamp,
#         'writer': writer,
#         'reading_time': reading_time ,
#         'summary': summary,
#         'category': category
#     }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    response = 'https://blog.betrybe.com/'
    fetch_url = response
    true_or_false = True
    list_news = []
    while true_or_false:
        res = fetch(fetch_url)
        urls = scrape_updates(res)
        fetch_url = scrape_next_page_link(res)
        for url in urls:
            if len(list_news) < amount:
                new = fetch(url)
                list_news.append(scrape_news(new))
            else:
                true_or_false = False
                break
    create_news(list_news)
    return list_news
    
 
        