import json
from collections import Counter
import xml.etree.ElementTree as ET


json_news = dict()
with open('newsafr.json', encoding="utf-8") as newsafr_file:
    json_news = json.load(newsafr_file)

count_json = Counter()

for i in json_news['rss']['channel']['items']:
    list_news = i['description'].split()
    list_news = [x.lower() for x in list_news if len(x) > 6]
    # list_n = []
    # for x in list_news:
    #     if len(x) > 6:
    #         list_n.append(x)
    count_json += Counter(list_news)
result = count_json.most_common(10)
print('10 наиболее часто встречаемых слов в статьях (json):')
for r in result:
    print(f'Слово "{r[0]}" - {r[1]} раз(а)')
                            


tree = ET.parse('newsafr.xml')
root = tree.getroot()
description = root.find(r'channel/description')
items = root.findall('channel/item')

count_xml = Counter()

for i in items:
    list_news = i.find('description').text.split()
    list_news = [x.lower() for x in list_news if len(x) > 6]
    count_xml += Counter(list_news)
result = count_xml.most_common(10)
print('10 наиболее часто встречаемых слов в статьях (xml):')
for r in result:
    print(f'Слово "{r[0]}" - {r[1]} раз(а)')



