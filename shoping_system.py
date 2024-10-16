class ShoppingSystem:
    def __init__(self):
        self.categories = {
            "Home Appliances": [{"name": "Fridge", "brand": "Samsung", "model_year": 2022, "price": 1500},
                                {"name": "Washing Machine", "brand": "LG", "model_year": 2021, "price": 1800},
                                {"name": "Oven", "brand": "Bosch", "model_year": 2020, "price": 1600},
                                {"name": "Dishwasher", "brand": "LG", "model_year": 2019, "price": 1700},
                                {"name": "Microwave", "brand": "Toshiba", "model_year": 2018, "price": 1300}],
            "Sports": [{"name": "Football", "brand": "Nike", "model_year": 2022, "price": 150},
                       {"name": "Basketball", "brand": "Adidas", "model_year": 2021, "price": 160},
                       {"name": "Tennis Racket", "brand": "Wilson", "model_year": 2020, "price": 100},
                       {"name": "Golf Clubs", "brand": "Adidas", "model_year": 2019, "price": 200},
                       {"name": "Running Shoes", "brand": "Nike", "model_year": 2018, "price": 180}],
            "Books": [{"name": "Harry Potter", "brand": "Bloomsbury", "model_year": 2001, "price": 50},
                      {"name": "The Hobbit", "brand": "HarperCollins", "model_year": 1937, "price": 40},
                      {"name": "Game of Thrones", "brand": "Bantam", "model_year": 1996, "price": 45},
                      {"name": "The Catcher in the Rye", "brand": "Little, Brown", "model_year": 1951, "price": 30},
                      {"name": "To Kill a Mockingbird", "brand": "J.B. Lippincott", "model_year": 1960, "price": 35}],
            "Electronics": [{"name": "Smartphone", "brand": "Apple", "model_year": 2022, "price": 1200},
                            {"name": "Laptop", "brand": "Dell", "model_year": 2021, "price": 1800},
                            {"name": "Tablet", "brand": "Samsung", "model_year": 2020, "price": 900},
                            {"name": "Smartwatch", "brand": "Apple", "model_year": 2019, "price": 200},
                            {"name": "Headphones", "brand": "Sony", "model_year": 2018, "price": 300}]
        }

