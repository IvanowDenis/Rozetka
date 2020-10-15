from urllib import parse
# import logging
from testing_data import *


# logging.basicConfig(
#     level=logging.DEBUG,
#     format='(%(threadName)-10s) %(message)s',
# )


BASE_API_URL = "product-api.rozetka.com.ua"





class Product:
    def __init__(self, item_id):
        self.item_id = item_id
        # self.data = {}
        self.data = data

    def get_data(self, session):
        # the url should looks like:
        # https://product-api.rozetka.com.ua/v4/goods/get-main?front-type=xl&id={self.item_id}&is_canonical=0&lang=ua
        url_path = "v4/goods/get-main"
        query = {
            "front-type": "xl",
            "id": self.item_id,
            "is_canonical": "0",
            "lang": "ua",
        }
        url = parse.urlunsplit(("https", BASE_API_URL, url_path, parse.urlencode(query), ""))
        # return url
        response = session.get(url)
        if response:
            self.data = response.json()
            return self.data['success']

    def get_price(self):
        return self.data["data"]["price"]

    def get_price_usd(self):
        return self.data["data"]["price_pcs"]

    def get_old_price(self):
        return self.data["data"]["old_price"]

    def get_title(self):
        return self.data["data"]["title"]

    def get_href(self):
        return self.data["data"]["href"]

    def get_comments_amount(self) -> int:
        return self.data["data"]["comments_amount"]

    def get_comments_mark(self) -> int:
        return self.data["data"]["comments_mark"]

    def get_category_id(self):
        return self.data["data"]["category_id"]

    def get_brand_name(self):
        return self.data["data"]["brand_name"]

    def get_brand_id(self):
        return self.data["data"]["brand_id"]

    def get_article(self):
        return self.data["data"]["article"]

    def get_(self):
        # Template for new methods
        return self.data["data"][""]
