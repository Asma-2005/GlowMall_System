class Item:
    def __init__(self, name, price, brand, model_year):
        self.name = name
        self.price = float(price)
        self.brand = brand
        self.model_year = model_year

    def __repr__(self):
        return f"{self.name} ({self.brand}, {self.model_year}) - {self.price}"
