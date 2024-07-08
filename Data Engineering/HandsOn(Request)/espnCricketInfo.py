import json

import requests
with open('crick_news.txt', 'w') as f:
    for i in range(1, 6):
        url = f'https://www.espncricinfo.com/ci/content/story/data/index.json?:type=7;page={i}'
        res = requests.get(url)
        data = json.loads(res.text)
        for news in data:

            print(news['author'], '\n', news['summary'])
            print('------------')
            f.write(news['author'] + '|' + news['summary'])
            f.write('\n')
