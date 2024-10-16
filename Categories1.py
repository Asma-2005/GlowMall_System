import tkinter as tk
from tkinter import ttk, messagebox
from HomePage import HomePage
from cart import Cart
from item import Item
from tki import CartGUI
# CategoriesPages class


class CategoriesPages:
    def __init__(self, cart, is_admin=False):
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
            "Books": [{"name": "Harry Potter", "brand": "Penguin", "model_year": 2022, "price": 15},
                      {"name": "1984", "brand": "Hachette", "model_year": 2021, "price": 120},
                      {"name": "The Great Gatsby", "brand": "Scribner", "model_year": 2020, "price": 200},
                      {"name": "No Longer Human", "brand": "Penguin", "model_year": 2019, "price": 180},
                      {"name": "The Setting Sun", "brand": "Hachette", "model_year": 2018, "price": 120}],
            "Electronics": [{"name": "Smartphone", "brand": "Apple", "model_year": 2022, "price": 1000},
                            {"name": "Laptop", "brand": "Dell", "model_year": 2021, "price": 1800},
                            {"name": "Tablet", "brand": "Samsung", "model_year": 2020, "price": 500},
                            {"name": "Smartwatch", "brand": "Samsung", "model_year": 2019, "price": 200},
                            {"name": "Headphones", "brand": "Sony", "model_year": 2018, "price": 150}],
            "Fashion": [{"name": "T-Shirt", "brand": "Gucci", "model_year": 2022, "price": 50},
                        {"name": "Jeans", "brand": "Zara", "model_year": 2021, "price": 60},
                        {"name": "Dress", "brand": "Chanel", "model_year": 2020, "price": 100},
                        {"name": "Shoes", "brand": "Nike", "model_year": 2019, "price": 80},
                        {"name": "Jacket", "brand": "Zara", "model_year": 2018, "price": 120}]
        }
        self.cart = cart
        self.is_admin = is_admin

    def quicksort(self, items, key, descending=False):
        if len(items) <= 1:
            return items

        pivot = items[len(items) // 2]
        left = []
        middle = []
        right = []
        for item in items:
            if item[key] < pivot[key]:
                left.append(item)
            elif item[key] == pivot[key]:
                middle.append(item)
            else:
                right.append(item)

        left_sorted = self.quicksort(left, key, descending)
        right_sorted = self.quicksort(right, key, descending)

        if descending:
            return right_sorted + middle + left_sorted
        else:
            return left_sorted + middle + right_sorted

    def sort_items(self, category, attribute, order):
        # Check if the sorting order is descending
        if order == 'Descending':
            descending = True
        else:
            descending = False

        # Sort the items in the specified category by the given attribute and order
        sorted_items = self.quicksort(self.categories[category], attribute, descending)

        # Update the category with the sorted items
        self.categories[category] = sorted_items

        # Print a message indicating the sorting attribute and order
        if descending:
            print(f"Items in {category} sorted by {attribute} in descending order:")
        else:
            print(f"Items in {category} sorted by {attribute} in ascending order:")

        # Refresh the display to show the sorted items
        self.display_items(category, self.items_frame)

    def search_item(self, category, key, value):
        # Create an empty list to store matching results
        results = []

        # Loop through each item in the specified category
        for item in self.categories[category]:
            # Get the value of the specified key from the item, and convert both to strings for comparison
            item_value = str(item.get(key, '')).lower()
            search_value = str(value).lower()

            # If the item value matches the search value, add the item to the results list
            if item_value == search_value:
                results.append(item)

        # If matching results are found, display them
        if results:
            self.display_items(category, self.items_frame, results=results)
        else:
            # If no matching results are found, display a "Not Found" message
            not_found_item = {"name": "Not Found", "brand": "", "model_year": "", "price": ""}
            self.display_items(category, self.items_frame, results=[not_found_item])

    def open_category(self, category_name, root):
        # check if there is a key in the dict is equal to the category_name on the button
        if category_name in self.categories:
            # open new page for each category if category button is clicked
            items_window = tk.Toplevel(root)
            items_window.title(f"{category_name} Items")
            items_window.geometry("800x600")
            # create a frame for the items
            self.items_frame = tk.Frame(items_window)
            self.items_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

            sort_frame = tk.Frame(items_window)
            sort_frame.pack(pady=10, padx=10, fill=tk.X)

            # ComboBox for sorting attribute
            self.attribute_var = tk.StringVar()
            self.attribute_combo = ttk.Combobox(sort_frame, textvariable=self.attribute_var)
            self.attribute_combo['values'] = ['name', 'brand', 'model_year', 'price']
            self.attribute_combo.set('Select an Attribute')
            self.attribute_combo.pack(side=tk.LEFT, padx=5)

            # ComboBox for sorting order
            self.order_var = tk.StringVar()
            self.order_combo = ttk.Combobox(sort_frame, textvariable=self.order_var)
            self.order_combo['values'] = ['Ascending', 'Descending']
            self.order_combo.set('Select the Type')
            self.order_combo.pack(side=tk.LEFT, padx=5)

            # Sort button
            sort_button = tk.Button(sort_frame, text="Sort", command=lambda category=category_name: self.sort_items(category, self.attribute_combo.get(), self.order_combo.get()))
            sort_button.pack(side=tk.LEFT, padx=5)

            # Search frame
            search_frame = tk.Frame(items_window)
            search_frame.pack(pady=10, padx=10, fill=tk.X)

            # Search attribute combobox
            self.search_attribute_var = tk.StringVar()
            self.search_attribute_combo = ttk.Combobox(search_frame, textvariable=self.search_attribute_var)
            self.search_attribute_combo['values'] = ['name', 'brand', 'model_year', 'price']
            self.search_attribute_combo.set('Select an Attribute')
            self.search_attribute_combo.pack(side=tk.LEFT, padx=5)

            # Search entry
            self.search_var = tk.StringVar()
            self.search_entry = tk.Entry(search_frame, textvariable=self.search_var)
            self.search_entry.pack(side=tk.LEFT, padx=5)

            # Search button
            search_button = tk.Button(search_frame, text="Search", command=lambda category=category_name: self.search_item(category, self.search_attribute_combo.get(), self.search_var.get()))
            search_button.pack(side=tk.LEFT, padx=5)

            # Admin buttons frame
            admin_buttons_frame = tk.Frame(items_window)
            admin_buttons_frame.pack(pady=10, padx=10, fill=tk.X)

            if self.is_admin:
                add_button = tk.Button(admin_buttons_frame, text="Add New Item", command=lambda category=category_name: self.add_item(category))
                add_button.pack(side=tk.LEFT, padx=5)

                update_button = tk.Button(admin_buttons_frame, text="Update Item", command=lambda category=category_name: self.update_item(category))
                update_button.pack(side=tk.LEFT, padx=5)

                discount_button = tk.Button(admin_buttons_frame, text="Make Discount", command=lambda category=category_name: self.make_discount(category))
                discount_button.pack(side=tk.LEFT, padx=5)

            # Display items
            self.display_items(category_name, self.items_frame)

        else:
            print(f"Category {category_name} does not exist!")

    def add_item(self, category):
        # Create a new window for adding an item
        add_item_window = tk.Toplevel()
        add_item_window.title("Add New Item")

        # Create entry fields for item details
        name_label = tk.Label(add_item_window, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(add_item_window)
        name_entry.pack()

        brand_label = tk.Label(add_item_window, text="Brand:")
        brand_label.pack()
        brand_entry = tk.Entry(add_item_window)
        brand_entry.pack()

        model_year_label = tk.Label(add_item_window, text="Model Year:")
        model_year_label.pack()
        model_year_entry = tk.Entry(add_item_window)
        model_year_entry.pack()

        price_label = tk.Label(add_item_window, text="Price:")
        price_label.pack()
        price_entry = tk.Entry(add_item_window)
        price_entry.pack()

        # Button to add the item
        def add_item_to_category():
            item = {
                "name": name_entry.get(),
                "brand": brand_entry.get(),
                "model_year": int(model_year_entry.get()),
                "price": float(price_entry.get())
            }
            self.categories[category].append(item)
            add_item_window.destroy()
            self.display_items(category, self.items_frame)

        add_button = tk.Button(add_item_window, text="Add Item", command=add_item_to_category)
        add_button.pack()

    def update_item(self, category):
        # Create a new window for updating an item
        update_item_window = tk.Toplevel()
        update_item_window.title("Update Item")

        # Create entry fields for item details
        name_label = tk.Label(update_item_window, text="Name of Item to Update:")
        name_label.pack()
        name_entry = tk.Entry(update_item_window)
        name_entry.pack()

        attribute_label = tk.Label(update_item_window, text="Attribute to Update (name, brand, model_year, price):")
        attribute_label.pack()
        attribute_entry = tk.Entry(update_item_window)
        attribute_entry.pack()

        value_label = tk.Label(update_item_window, text="New Value:")
        value_label.pack()
        value_entry = tk.Entry(update_item_window)
        value_entry.pack()

        # Button to update the item
        def update_item_in_category():
            name = name_entry.get()
            attribute = attribute_entry.get()
            value = value_entry.get()

            for item in self.categories[category]:
                if item["name"] == name:
                    if attribute == "model_year":
                        item[attribute] = int(value)
                    elif attribute == "price":
                        item[attribute] = float(value)
                    else:
                        item[attribute] = value
                    update_item_window.destroy()
                    self.display_items(category, self.items_frame)
                    return

        update_button = tk.Button(update_item_window, text="Update Item", command=update_item_in_category)
        update_button.pack()

    def make_discount(self, category):
        # Create a new window for making a discount
        make_discount_window = tk.Toplevel()
        make_discount_window.title("Make Discount")

        # Create entry fields for item details
        name_label = tk.Label(make_discount_window, text="Name of Item to Discount:")
        name_label.pack()
        name_entry = tk.Entry(make_discount_window)
        name_entry.pack()

        discount_label = tk.Label(make_discount_window, text="Discount Percentage:")
        discount_label.pack()
        discount_entry = tk.Entry(make_discount_window)
        discount_entry.pack()

        # Button to apply the discount
        def apply_discount_to_item():
            name = name_entry.get()
            discount = float(discount_entry.get())

            for item in self.categories[category]:
                if item["name"] == name:
                    item["price"] -= item["price"] * (discount / 100)
                    make_discount_window.destroy()
                    self.display_items(category, self.items_frame)
                    return

        apply_discount_button = tk.Button(make_discount_window, text="Apply Discount", command=apply_discount_to_item)
        apply_discount_button.pack()

    def display_items(self, category, frame, results=None):
        print(f"Displaying items for category: {category}")  # Debug statement
        if frame is not None:
            for widget in frame.winfo_children():
                widget.destroy()

            if results is None:
                results = self.categories[category]

            for item in results:
                item_frame = tk.Frame(frame)
                item_frame.pack(pady=5, anchor=tk.W)

                item_label = tk.Label(item_frame, text=f"{item['name']} - {item['brand']} - {item['model_year']} - {item['price']}$")
                item_label.pack(side=tk.LEFT, padx=5)

                add_to_cart_button = tk.Button(item_frame, text="Add to Cart", command=lambda c=category, name=item['name']: self.add_to_cart(category, name))
                add_to_cart_button.pack(side=tk.LEFT, padx=5)

    def add_to_cart(self, category, name):
        for item in self.categories[ category ]:
            if item["name"] == name:
                self.cart.add_item(Item(item[ 'name'], int(item[ 'price' ]), item[ "brand" ], item[ "model_year" ]))
                print(f"Added {name} to cart.")
                return
        print(f"{name} not found in {category}.")

