import requests
r = requests.get('https://quotes.toscrape.com/')

with open ('quotes.txt','w') as f:
    html = r.text
    for line in html.split('\n'):
        if '<span class="text" itemprop="text">' in line:
            quotes = line.replace(
                '<span class="text" itemprop="text">“', '').replace('”</span>', '')
            line = line.strip()
            print(line)
            f.write(line)
            f.write('\n')
