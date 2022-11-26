import requests
from bs4 import BeautifulSoup
import csv
# import pdb
# from logging import getLogger, StreamHandler, DEBUG


DOMAIN_URL = "https://example.com"


def build_prefecture_urls():
    PREFECTURE_URL = "https://example.com"
    for i in range(1, 48):
        yield PREFECTURE_URL + str(i)


def request_soup(url):
    html_text = requests.get(url).text
    return BeautifulSoup(html_text, "lxml")


def crawl_prefecture_urls(url):
    soup = request_soup(url)
    index_page_url = soup.select(".grad-link")[0].attrs["href"]
    pagination_urls = crawl_pagination(DOMAIN_URL + index_page_url)
    return pagination_urls


def crawl_pagination(url):
    soup = request_soup(url)
    pagination_indices = soup.select(".p-works-pager > .p-works-pager-num > a")
    last_page = pagination_indices[-1].contents[0]
    for i in range(1, int(last_page) + 1):
        yield url + "?page=" + str(i)


def build_crawl_target_all_url():
    urls = list(build_prefecture_urls())
    for url in urls:
        yield crawl_prefecture_urls(url)


def main():
    all_url = build_crawl_target_all_url()
    with open("./beautiful_soup_proto//url_list.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["url"])
        writer.writeheader()
        for url in all_url:
            for u in list(url):
                writer.writerow({"url": u})


if __name__ == "__main__":
    main()
