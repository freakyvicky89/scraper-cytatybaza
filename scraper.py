from lxml import html
from lxml.etree import XPath

gotolast_xpath = XPath("//a[@class='page-link bg-light' and contains(.,'»»')]")
author_xpath = XPath("//h4[@class='smBox']/a")
quotes_xpath = XPath("//p[@class='qt']/text()")

base_url = "http://cytatybaza.pl"
authors_url = "/autorzy/?pspn=%s"
authors_url_paging = "?ppn=%s"

authors_index = 1

while True:
    authors_page = html.parse(base_url + authors_url % authors_index)
    author_links = author_xpath(authors_page)

    for author_link in author_links:
        author_name = author_link.text
        author_url = author_link.get("href")
        print(author_name)
        quotes_index = 1
        author_quotes = []

        while True:
            quotes_page = html.parse(base_url + author_url + authors_url_paging % quotes_index)
            author_quotes.extend(quotes_xpath(quotes_page))

            if not gotolast_xpath(quotes_page):
                break
            else:
                quotes_index += 1

        print(author_quotes)

    if not gotolast_xpath(authors_page):
        break
    else:
        authors_index += 1
