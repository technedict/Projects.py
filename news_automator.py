import requests,os
from sys import argv

API_KEY = '8b093b3050b04bdca35b1408560b349c'

URL = ('https://newsapi.org/v2/top-headlines?')


def get_artciles_by_category(category="technology"):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "ng",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def get_artciles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "gb",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []
        
    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        print(result['title'])
        print(result['url'])
        print('')
        with open('news.txt', 'a') as news:
            news.write(f"\n{result['title']}\nLink: {result['url']}\n")

def get_sources_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines/sources'
    query_parameters = {
        "category": category,
        "language": "en",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=query_parameters)

    sources = response.json()['sources']

    for source in sources:
        print(source['name'])
        print(source['url'])


if __name__ == "__main__":
    try:
        print(f"Getting news for {argv[1]}...\n")
        get_artciles_by_category(argv[1])
        print(f"Successfully retrieved top {argv[1]} headlines")
        print(f'Saved in a news.txt file at {os.getcwd()}')
    except IndexError:
        print("Getting news for technology...\n")
        get_artciles_by_category()
        print("Successfully retrieved top tech headlines")
        print(f'Saved in a news.txt file at {os.getcwd()}')
        # get_artciles_by_query("Liz Truss"))
        #print_sources_by_category("technology")
