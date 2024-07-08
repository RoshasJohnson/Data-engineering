
import requests  # type: ignore

for i in range(1, 11):
    url = f"https://quotes.toscrape.com/page/{i}/"
    print(f"https://quotes.toscrape.com/page/{i}/")
    r = requests.get(url)
    with open('quotes_and_authors.csv', 'a', encoding='utf-8') as f:
        html = r.text
        for line in html.split('\n'):
            if '<span class="text" itemprop="text">' in line:
                line = line.replace(
                    '<span class="text" itemprop="text">“', '').replace('”</span>', '')
                quotes = line.strip()

            if '<span>by <small class="author" itemprop="author">' in line:
                line = line.replace(
                    '<span>by <small class="author" itemprop="author">', '')
                line = line.replace('</small>', '')
                author = line.strip()
                print(quotes)
                print(author)
                f.write(f"{author}, \"{quotes}\"\n")
