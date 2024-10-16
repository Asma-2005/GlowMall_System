import tkinter as tk
from tkinter import ttk
from cart import Cart
from item import Item


class CartGUI:
    def __init__(self, cart):
        self.cart = cart

    def open_cart(self, root):
        cart_window = tk.Toplevel(root)
        cart_window.title("Glow Mall Cart")
        cart_window.geometry("800x600")
        cart_window.configure(bg="lightblue")

        # create a frame
        self.cart_window = tk.Frame(cart_window, bg="lightblue")
        self.cart_window.pack(pady=10, fill="both", expand=True)

        # Governorate selection for calculating delivery fees
        self.governorate_var = tk.StringVar(value="Cairo")
        # Title Label
        title_label = tk.Label(self.cart_window, text="Shopping Cart", font=("Arial", 24), bg="lightblue",
                               fg="darkblue")
        title_label.pack(pady=10)

        # Items in Cart label
        cart_items_label = tk.Label(self.cart_window, text="Items in Cart:", font=("Arial", 16), bg="lightblue",
                                    fg="darkblue")
        cart_items_label.pack(pady=10)

        # Listbox to display cart items
        self.cart_items_listbox = tk.Listbox(self.cart_window, height=10, font=("Arial", 12), bg="white", fg="black")
        self.cart_items_listbox.pack(pady=10, fill="both", expand=True)

        # Listbox with cart items
        for item in self.cart.items:
            self.cart_items_listbox.insert(tk.END, f"{item.name} - ${item.price}")

        # Total price
        total = self.cart.get_total_price()
        total_label = tk.Label(self.cart_window, text=f"Total: ${total}", font=("Arial", 16), bg="lightblue",
                               fg="black")
        total_label.pack(pady=5)

        # Gove selection
        governorate_label = tk.Label(self.cart_window, text="Select Governorate:", bg="lightblue")
        governorate_label.pack(pady=5)

        self.governorate_combo = ttk.Combobox(self.cart_window, textvariable=self.governorate_var)
        self.governorate_combo[ 'values' ] = list(self.cart.governorate_distance.keys())  # Using keys from Cart class
        self.governorate_combo.pack(pady=5)

        # Total with delivery
        total_with_delivery = self.cart.get_total_with_delivery(self.governorate_var.get())
        self.total_with_delivery_label = tk.Label(self.cart_window, text=f"Total with Delivery: ${total_with_delivery}",
                                                  font=("Arial", 16), bg="lightblue", fg="black")
        self.total_with_delivery_label.pack(pady=5)

        # Update delivery total when gove is selected
        self.governorate_combo.bind("<<ComboboxSelected>>", self.update_total)

    def update_total(self, event):
        total_with_delivery = self.cart.get_total_with_delivery(self.governorate_var.get())
        self.total_with_delivery_label.config(text=f"Total with Delivery: ${total_with_delivery}")

