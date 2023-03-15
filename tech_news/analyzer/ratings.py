from tech_news.database import get_collection

# Requisito 10
def top_5_categories():
    """Seu código deve vir aqui"""
    news = get_collection()
    categories = news.aggregate(
        [
            {"$group": {"_id": "$category", "count": {"$sum": 1}}},
            {"$sort": {"count": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )
    response = []
    for category in categories:
        response.append(category["_id"])
    return response


