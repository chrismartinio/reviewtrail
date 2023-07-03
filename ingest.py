from handlers import RequestHandler, user_agents, headers
import re


def ingest_asins():
    pass

def generate_request_urls(asins_list: list):
    request_urls = []

    i = 0
    while len(asins_list) > 0 and i < 10:
        i += 1
        asin = asins_list.pop()
        initial_url = f"https://www.amazon.com/product-reviews/{asin}?reviewerType=all_reviews&sortBy=recent&pageNumber=1"
        request = RequestHandler(initial_url)
        response = request.send_get_request()
        response = request.process_response(response)
        soup = request.get_soup(response) if response else None

        if soup:
            review_count_block = soup.find_all("div", attrs={"data-hook": "cr-filter-info-review-rating-count"})
            review_count = get_number_from_string(review_count_block[0].text)
            page_count = review_count // 10

            request_urls.extend(get_urls(asin, page_count))
            print("added urls for asin", asin, "page_count", page_count)
        else:
            asins_list.append(asin)
            print("no soup for url gather")

    return request_urls


def get_number_from_string(string: str):
    pattern = r'(\d+)\s+with reviews'
    matches = re.findall(pattern, string)

    if matches:
        return int(matches[0])

    return None


def get_urls(asin: str, page_count):
    urls = []
    for page in range(1, page_count):
        url = f"https://www.amazon.com/product-reviews/{asin}?reviewerType=all_reviews&sortBy=recent&pageNumber={page}"
        urls.append(url)

    return urls