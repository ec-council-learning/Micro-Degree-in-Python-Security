import requests
import threading


STATUS_CODES = {
    200: 'OK',
    404: 'Not Found',
    500: 'Internal Server Error',
    524: 'A timeout occured'
}


def ping(url):
    res = requests.get(url)
    print(f'{url}: {STATUS_CODES[res.status_code]}')


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    threads = []
    for url in lines:
        t = threading.Thread(target=ping, args=(url[:-1],))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
