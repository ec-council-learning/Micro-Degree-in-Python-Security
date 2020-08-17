import os
import requests


URLS = [
    'http://httpstat.us/200',
    'http://httpstat.us/200?sleep=2000',
    'http://httpstat.us/404',
    'http://httpstat.us/500?sleep=3000',
    'http://httpstat.us/524'
]


def download_html(url):
    res = requests.get(url)
    with open(f'output/{os.path.basename(url).replace("?", "")}.html', 'w') as f:
        f.write(res.text)


if __name__ == '__main__':
    for url in URLS:
        download_html(url)
