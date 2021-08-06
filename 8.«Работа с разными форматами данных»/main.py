import json

from collections import Counter
temp = []

with open("newsafr.json", "r", encoding='UTF8') as news_file:
    all_news = json.load(news_file)

for desk in all_news['rss']['channel']["items"]:
    for i in desk['description'].split():
        if len(i) > 6:
            temp.append(i)

sorted_temp = sorted(temp)
count_of_entres = Counter(sorted_temp)
print('Топ-10 самых употребляемых слов в ленте новостей длиннее 6 символов:')
for i in count_of_entres.most_common(10):
    print(i[0])
