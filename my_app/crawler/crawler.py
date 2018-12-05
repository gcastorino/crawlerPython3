
def curl(url='https://www.valor.com.br/rss'):
    """
    --> Search all news
    :rtype: object
    :return: result find crawler
    """
    from bs4 import BeautifulSoup
    import requests
    page = requests.get(url)
    crawler = BeautifulSoup(page.content, features="lxml")

    return crawler
