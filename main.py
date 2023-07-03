import time
import datetime

from content import get_all_reviews
from ingest import generate_request_urls

asins = [
    'B09X8RZ55Z',
    'B0B3PQV3RV',
    'B08KQ567GB',
    'B0B3NJHTKG',
    'B09ZH1HG7T',
    'B0C4YVJMF3',
    'B07S1WGYX2',
    'B0BYDCHNCF',
    'B0BYXHPRT4',
    'B0BDCNC4JJ',
    'B0B6WBQH3S',
    'B0C2WVTRYH',
    'B0C2WQL646',
    'B084Y8NZR6',
    'B09Z71V6XP',
    'B0BFCN3VS2',
    'B09WJH6J15',
    'B07K8TK3P8',
    'B07PGW8PVN',
    'B07MP3MQSG',
    'B07QSBYHC7',
    'B0B8FT2CDP',
    'B0C2JMT7VY',
    'B07G68YMTB',
    'B07X27RKMR',
    'B07KCJ96FD',
    'B07RX88X49',
    'B07N1SKPYD',
    'B082DKN8FL',
    'B081HVT3MB',
    'B0795Y1WJK',
    'B09JPKCG67',
    'B08HFSXHZB',
    'B07V9Y4XSZ',
    'B07XQL9SJ6',
    'B07N1PDCJT',
    'B078MNV759',
    'B074663H8C',
    'B09VVKD912',
    'B07RCK2LPR',
    'B08BQ72S1Y',
    'B08TYBP3DQ',
    'B08BS64L6Y',
    'B08MV7GWS8',
    'B07WDZ44S3',
    'B0998DNBCL',
    'B07XVTB6NG',
    'B07TKCGVBT',
    'B08CG22DS6',
    'B08BQX9RYL',
    'B07CJH4J1X',
    'B08J9TB2L1',
    'B07GVN5QRH',
    'B07PJTVHHV',
    'B08DTDFPV3',
    'B07N1WZMV6',
    'B07MZ9DT4Z',
    'B08SCHKXZ9',
    'B093CGZ6B9',
    'B09983Y3Z4',
    'B07MLB25GB',
    'B07JJCD94D',
    'B07WVTHTDH',
    'B08HFQXQ3Q',
    'B08J9M41H3',
    'B08MQVYZ48',
    'B08CG29DFN',
    'B0C2JQFKYF',
    'B08TYYCG7P',
    'B09RQ8LLHQ',
    'B08TYM97DD',
]

def get_urls_one_page(asin: str):
    url = f"https://www.amazon.com/product-reviews/{asin}?reviewerType=all_reviews&sortBy=recent&pageNumber=1"
    return url

if __name__ == '__main__':

    start_time = time.time()
    # request_urls = generate_request_urls([
    #     'B076DMSCHV',
    # ])

    request_urls = []
    for asin in asins:
        new_url = get_urls_one_page(asin)
        request_urls.append(new_url)

    ingest_results = get_all_reviews(request_urls)

    elapsed_time = time.time() - start_time

    print(dict(request_urls=len(request_urls), ingest_results=len(ingest_results), elapsed_time=str(
        datetime.timedelta(seconds=elapsed_time))))