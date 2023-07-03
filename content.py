import concurrent.futures
import multiprocessing
import random
import threading

from db.models import Ingest
from handlers import RequestHandler
from multiprocessing import Queue
from redis import Redis


def get_all_reviews(urls):
    random.shuffle(urls)
    print(f"starting get_all_reviews with {len(urls)} urls")

    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(get_page, url) for url in urls]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)

    return results


def get_page(url):
    request = RequestHandler(url)
    response = request.send_get_request()
    response = request.process_response(response)
    soup = request.get_soup(response) if response else None
    if soup:
        new_ingest = Ingest(url=url, content=soup.text)
        new_ingest.save()
        print(f"saved soup for {url}")
        return url
    else:
        print(f"no soup for {url}")
        get_page(url)