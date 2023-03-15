from tech_news.database import search_news
from datetime import datetime


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
    response = []
    try:
        date_param_format = datetime.strptime(date, "%Y-%m-%d")
        date_db_format = date_param_format.strftime("%d/%m/%Y")
        found_news = search_news(
            {"timestamp": {"$regex": date_db_format, "$options": "i"}}
        )
        for news in found_news:
            response.append((news["title"], news["url"]))
        return response
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    found_news = search_news(
        {"category": {"$regex": category, "$options": "i"}}
        )
    response = []
    for news in found_news:
        response.append((news["title"], news["url"]))
    return response
