import sys
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_category )

from tech_news.analyzer.ratings import top_5_categories

from tech_news.scraper import get_tech_news

# Requisitos 11 e 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    input_user = input(
    """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
"""
    )
    match input_user:
        case "0":
            amount = input("Digite quantas notícias serem buscadas:")
            get_tech_news(int(amount))
            print("Notícias importadas com sucesso!")
        case "1":
            title = input("Digite o título:")
            print(search_by_title(title))
        case "2":
            date = input("Digite a data no formato aaaa-mm-dd:")
            print(search_by_date(date))
        case "3":
            category = input("Digite a categoria:")
            print(search_by_category(category))
        case "4":
            print(top_5_categories())   
        case "5":
            sys.exit()
        case _:
            sys.stderr.write("Opção inválida\n")

    return input_user


