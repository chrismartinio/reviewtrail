import time
import datetime

from content import get_all_reviews
from ingest import generate_request_urls

if __name__ == '__main__':

    start_time = time.time()
    request_urls = generate_request_urls([
        'B09X8RZ55Z',
        'B0B3PQV3RV',
        'B08KQ567GB'
    ])

    ingest_results = get_all_reviews(request_urls)

    elapsed_time = time.time() - start_time

    print(dict(request_urls=len(request_urls), ingest_results=len(ingest_results), elapsed_time=str(
        datetime.timedelta(seconds=elapsed_time))))