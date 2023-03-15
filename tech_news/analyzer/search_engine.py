from tech_news.database import search_news

# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    found_news = search_news({"title": {"$regex": title, "$options": "i"}})
    response = []
    for news in found_news:
        response.append((news["title"], news["url"]))
    return response
   
    
    



# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
