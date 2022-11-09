from os import name
from bs4 import BeautifulSoup
import requests

class TheToyTrovePreorderScraper():
    NAME = 'Test Vendor'
    BASE_URL = 'https://thetoytrove.crystalcommerce.com'
    URL = 'https://thetoytrove.crystalcommerce.com/advanced_search?buylist_mode=0&commit=Search&search%5Bbuy_price_gte%5D=&search%5Bbuy_price_lte%5D=&search%5Bcatalog_group_id_eq%5D=&search%5Bcategory_ids_with_descendants%5D%5B%5D=&search%5Bdirection%5D=ascend&search%5Bfuzzy_search%5D=&search%5Bin_stock%5D=0&search%5Bsell_price_gte%5D=&search%5Bsell_price_lte%5D=&search%5Bsort%5D=name&search%5Btags_name_eq%5D=preorders&utf8=%E2%9C%93'

    @classmethod
    def get_items(cls):
        return cls._scrape_items(cls.URL)

    @classmethod
    def _scrape_items(cls, url, page_number=1, item_list=None):
        if item_list is None:
            item_list = []

        page_soup = cls._get_page_soup(url)
        item_list.extend(cls._get_page_items(page_soup))

        if cls._get_next_button(page_soup):
            page_number += 1
            url = cls._build_next_url(page_number)
            return cls._scrape_items(url, page_number, item_list)

        return item_list

    @classmethod
    def _get_page_items(cls, page_soup):
        page_items = []
        li_elements = cls._get_li_elements(page_soup)

        for li_element in li_elements:
            description = cls._get_description_value(li_element)
            category = cls._get_category_value(li_element)
            url = cls._build_item_url(cls.BASE_URL, cls._get_url_value(li_element))

            item = {
                'description': description,
                'category': category,
                'url': url
            }
            page_items.append(item)

        return page_items

    def _build_item_url(base_url, url):
        item_url = base_url
        item_url += url
        return item_url

    def _build_next_url(page_number):
        url = 'https://thetoytrove.crystalcommerce.com/advanced_search?buylist_mode=0&commit=Search&page='
        url += str(page_number)
        url += '&search%5Bbuy_price_gte%5D=&search%5Bbuy_price_lte%5D=&search%5Bcatalog_group_id_eq%5D=&search%5Bcategory_ids_with_descendants%5D%5B%5D=&search%5Bdirection%5D=ascend&search%5Bfuzzy_search%5D=&search%5Bin_stock%5D=0&search%5Bsell_price_gte%5D=&search%5Bsell_price_lte%5D=&search%5Bsort%5D=name&search%5Btags_name_eq%5D=preorders&utf8=%E2%9C%93'
        return url

    def _get_category_value(list_item_soup):
        span_tags = list_item_soup.findAll('span', 'category')
        return span_tags[0].getText()

    def _get_description_value(list_item_soup):
        header_tags = list_item_soup.findAll('h4', itemprop='name')
        tag_attributes = header_tags[0].attrs
        return tag_attributes['title']

    def _get_li_elements(page_soup):
        return page_soup.findAll('li', 'product')

    def _get_next_button(page_soup):
        return page_soup.findAll('a', 'next_page')

    def _get_page_soup(url):
        r = requests.get(url)
        return BeautifulSoup(r.content, 'html.parser')

    def _get_url_value(list_item_soup):
        anchor_tags = list_item_soup.findAll('a', itemprop='url')
        tag_attributes = anchor_tags[0].attrs
        return tag_attributes['href']


if __name__ == '__main__':
    item_list = TheToyTrovePreorderScraper.get_items()
    print(len(item_list))
    for item in item_list:
        print(item)
