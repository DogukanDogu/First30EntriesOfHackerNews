from bs4 import BeautifulSoup
import httpx

def getHackerNewsFromWeb(url):
    response = httpx.get(url)
    yc_web_page = response.content

    soup = BeautifulSoup(yc_web_page, features="html.parser")
    articles = soup.find_all(class_="athing")

    news_data = []

    for article in articles:
        data = {
            "URL": article.find(class_="titleline").find("a").get('href'),
            "title": article.find(class_="titleline").getText(),
            "rank": article.find(class_="rank").getText().replace(".", "")
        }
        news_data.append(data)

    return news_data


news_data = getHackerNewsFromWeb("https://news.ycombinator.com/news")

print(news_data)





