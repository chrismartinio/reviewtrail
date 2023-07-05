import concurrent.futures
import multiprocessing
import random
import threading

from db.models import Ingest, Review
from handlers import RequestHandler
from multiprocessing import Queue
from redis import Redis


def get_all_reviews(urls):
    random.shuffle(urls)
    print(f"starting get_all_reviews with {len(urls)} urls")

    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(get_page, url) for url in urls]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)

    return results


def get_page(url, retries: int = 0):
    retries += 1
    request = RequestHandler(url)
    response = request.send_get_request()
    response = request.process_response(response)
    soup = request.get_soup(response) if response else None
    if soup:
        reviews = soup.find_all("div", attrs={"data-hook": "review"})
        if reviews:
            for review in reviews:
                new_review = Review(
                    review_id=review.attrs["id"],
                    user=review.find("span", attrs={"class": "a-profile-name"}).text if review.find("span",
                                                                                                    attrs={"class":
                                                                                                               "a-profile-name"}).text else None,
                    title=review.find("a", attrs={"data-hook": "review-title"}).text if review.find("a",
                                                                                                    attrs={"data-hook":
                                                                                                               "review-title"}) else None,
                    content=review.find("span", attrs={"data-hook": "review-body"}).text if review.find("span",
                                                                                                        attrs={
                                                                                                            "data-hook": "review-body"}) else None,
                )
                new_review.save()
                print(f"saved review {new_review.id} for {url}")
        else:
            print(f"no reviews for {url}")
        # new_ingest = Ingest(url=url, content=soup.text)
        # new_ingest.save()
        # print(f"saved soup for {url}")
        return url
    else:
        print(f"no soup for {url}")
        if retries > 3:
            print(f"retries exceeded for {url}")
            return None
        else:
            get_page(url, retries)