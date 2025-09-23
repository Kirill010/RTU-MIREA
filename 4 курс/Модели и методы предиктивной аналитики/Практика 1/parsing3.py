import requests
import pandas as pd
import time
from datetime import datetime, timedelta

# Наборы текста
# https://newsapi.org/

NEWS_API_KEY = "98a99dffe46c409e81bc6398aff29096"
NEWS_URL = "https://newsapi.org/v2/everything"
CATEGORIES = [
    'sports', 'technology', 'health',
    'business', 'science', 'politics',
    'music', 'environment', 'entertainment',
    'ai', 'cybersecurity',
    'crypto', 'gaming', 'space', 'fashion',
    'travel', 'food', 'books', 'wellness',
    'renewables', 'edtech', 'robotics', 'philanthropy'
]
DOMAINS = {
    'sports': 'espn.com,bbc.com/sport',
    'technology': 'techcrunch.com,engadget.com',
    'health': 'who.int,webmd.com',
    'business': 'reuters.com,bloomberg.com',
    'science': 'sciencemag.org,nature.com',
    'music': 'rollingstone.com, billboard.com, pitchfork.com, nme.com, spin.com',
    'politics': 'reuters.com/politics, politico.com, theguardian.com/world',
    'environment': 'ipcc.ch, grist.org, carbonbrief.org',
    'entertainment': 'variety.com, hollywoodreporter.com',
    'ai': 'syncedreview.com, arxiv.org, towardsdatascience.com',
    'cybersecurity': 'krebsonsecurity.com, therecord.media, darkreading.com',
    'crypto': 'coindesk.com, theblock.co, cointelegraph.com',
    'gaming': 'ign.com, polygon.com, eurogamer.net',
    'space': 'nasa.gov, spacex.com, skyandtelescope.org',
    'fashion': 'vogue.com, wwd.com, businessoffashion.com',
    'travel': 'cntraveler.com, lonelyplanet.com, skyradar.com, travelandleisure.com',
    'food': 'eater.com, bonappetit.com, foodandwine.com, theinfatuation.com',
    'books': 'nytimes.com/books, theguardian.com/books, lrb.co.uk, bookforum.com',
    'wellness': 'goop.com, mindbodygreen.com, well.blogs.nytimes.com, tinyhearts.com',
    'renewables': 'renewableenergyworld.com, greentechmedia.com, insideclimatenews.org',
    'edtech': 'edutopia.org, edsurge.com, timeshighereducation.com/edtech',
    'robotics': 'therobotreport.com, ieee.org/spectrum, robohub.org',
    'philanthropy': 'ssir.org, philanthropy.com, globalgiving.org'
}


def fetch_news_by_category(category, days=30, limit=50):
    from_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    to_date = datetime.now().strftime('%Y-%m-%d')
    domain_filter = DOMAINS.get(category, "")

    params = {
        'q': category,
        'from': from_date,
        'to': to_date,
        'sortBy': 'publishedAt',
        'language': 'en',
        'pageSize': 100,
        'page': 1,
        'domains': domain_filter,
        'apiKey': NEWS_API_KEY
    }

    try:
        response = requests.get(NEWS_URL, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        articles = []
        for item in data.get('articles', []):
            if len(articles) >= limit:
                break
            articles.append({
                'source_api': 'newsapi.org',
                'category': category,
                'source_id': item['source']['id'],
                'source_name': item['source']['name'],
                'author': item.get('author'),
                'title': item['title'],
                'description': item.get('description'),
                'url': item['url'],
                'image_url': item.get('urlToImage'),
                'published_at': item['publishedAt'],
                'content': item.get('content'),
                'collected_at': datetime.now().isoformat()
            })
        print(f"Получено {len(articles)} новостей по теме '{category}'")
        return articles
    except Exception as e:
        print(f"Ошибка при загрузке новостей ({category}): {e}")
        return []


print("Сбор текстовых данных (новости)...")
all_articles = []

for category in CATEGORIES:
    articles = fetch_news_by_category(category, days=30, limit=30)
    all_articles.extend(articles)
    time.sleep(1.5)

if all_articles:
    df_news = pd.DataFrame(all_articles)
    df_news['published_at'] = pd.to_datetime(df_news['published_at'])
    df_news.sort_values(by='published_at', ascending=False, inplace=True)

    df_news.to_csv('news_data.csv', index=False)
    print(f"Сохранено {len(df_news)} новостных записей в textual_news_data.csv")
