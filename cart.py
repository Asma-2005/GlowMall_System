class Cart:
    def __init__(self):
        self.items = []
        self.memoized_total = 0.0
        self.governorate_distance = {
            "Cairo": 0,
            "Giza": 20,
            "Alexandria": 220,
            "Aswan": 900,
        }
        self.delivery_fee_per_km = 0.5

    def add_item(self, item):
        self.items.append(item)
        self.memoized_total += item.price

    def get_total_price(self):
        return self.memoized_total

    def get_delivery_fees(self, gove):
        distance = self.governorate_distance.get(gove, 100)
        return distance * self.delivery_fee_per_km

    def get_total_with_delivery(self, gove):
        total_price = self.get_total_price()
        delivery_fees = self.get_delivery_fees(gove)
        return total_price + delivery_fees

    def display_cart(self):
        return [f"{item}" for item in self.items]

