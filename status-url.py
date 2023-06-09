import requests
from fake_useragent import UserAgent

urls = [
    'https://scout.kz/product-category/tractors/',
    'https://scout.kz/product-category/tractors/1',
    'https://scout.kz/product-category/tractors/2',
]

ua = UserAgent().random
headers = {
    'user-agent': ua
}

for url in urls:
    response = requests.get(url=url, headers=headers).status_code

    if response != 200:
        print(f'{response}: {url}')