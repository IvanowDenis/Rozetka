







class Product():
    PRODUCT_URL = "https://product-api.rozetka.com.ua/v4/goods/get-main?front-type=xl&id=17009888&is_canonical=0&lang=ua"

    def __init__(self, item_id):
        self.item_id = item_id
        self.data = []

    def get_data(self, session):
        url = f"https://product-api.rozetka.com.ua/v4/goods/get-main?front-type=xl&id={self.item_id}&is_canonical=0&lang=ua"
        response = session.get(url)
        if response:
            self.data = response.json()
