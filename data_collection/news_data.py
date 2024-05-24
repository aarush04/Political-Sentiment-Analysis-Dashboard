#List of keywords
keywords =['Trump', 'Biden', 'Immigration', 'Unemployment', 'Democrat', 'Republican', 'Palestine', 'Israel']

from newsapi import NewsApiClient
from datetime import date, timedelta

week_before = date.today() - timedelta(days=7)

API_key="6de831c22296464bb0323ebb5b9a9bfd"
newsapi = NewsApiClient(api_key=API_key)

news_data={}

for keyword in keywords:
    title=[]
    description=[]
    content=[]
    all_articles = newsapi.get_everything(q=keyword,
                                      sources="cnn, the-washington-post, fox-news, abc-news, nbc-news, reuters, bbc-news, usa-today, al-jazeera-english, politico, bloomberg",
                                      from_param=week_before,
                                      language='en',
                                      sort_by='relevancy')
    for i in all_articles['articles']:
        title.append(i['title'])
        description.append(i['description'])
        content.append(i['content'])
    news_data[keyword]=[title,description,content]