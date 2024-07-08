

import requests

for i in range(1, 11):
    url = f"https://quotes.toscrape.com/page/{i}/"
    print(f"https://quotes.toscrape.com/page/{i}/")
    r = requests.get(url)
    html = r.text
    with open('authors.txt', 'a', encoding='utf-8') as f:
        for line in html.split('\n'):

            if '<span class="text" itemprop="text">' in line:
                quotes = line.replace(
                '<span class="text" itemprop="text">“', '').replace('”</span>', '')
                quotes = quotes.strip()
                if '<span>by <small class="author" itemprop="author">' in line:
                    author = line.replace(
                        '<span>by <small class="author" itemprop="author">', '')
                    author = line.replace('</small>', '')
                    print(line)
                author = line.strip()
                f.write(f'{author,",",quotes}')
                f.write('\n')
