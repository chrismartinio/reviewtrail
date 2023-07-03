import random
from bs4 import BeautifulSoup

import requests


user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0",
    # "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    # "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Safari/605.1.15"
    # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
    # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
]

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "www.amazon.com",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "TE": "trailers",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": random.choice(user_agents),
}

http_proxy = "http://kayjitsu:auMYDwfm8Su4K0ph@proxy.packetstream.io:31112"
https_proxy = "http://kayjitsu:auMYDwfm8Su4K0ph@proxy.packetstream.io:31112"

proxy_dict = {
    "http": http_proxy,
    "https": https_proxy,
}


class RequestHandler:
    def __init__(self, url, headers=headers, proxies=proxy_dict, params=None):
        self.url = url
        self.headers = headers
        self.params = params
        self.proxies = proxies

    def send_get_request(self):
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, proxies=self.proxies)
            return response
        except:
            return None


    def process_response(self, response):
        if response:
            if response.status_code == 200:
                return response
        else:
            return None

    def get_soup(self, response):
        soup = BeautifulSoup(response.content, "html.parser")
        soup.prettify()
        return soup


class IngestHandler:
    def __init__(self, url_list: list):
        self.asins_list = url_list

    def ingest_asins(self):
        pass