import tkinter as tk
from tkinter import ttk
from tki import CartGUI
from PIL import Image, ImageTk


class HomePage:
    def __init__(self, categories_pages, cart_gui):
        self.categories_pages = categories_pages
        self.cart_gui = cart_gui
        self.root = tk.Tk()
        self.root.title("Home page")
        self.root.geometry("800x600")
        self.root.config(bg="#2d677d")


        # Navigation Bar
        self.navbar = tk.Frame(self.root, bg="#2d677d")
        self.navbar.pack(side=tk.TOP, fill=tk.X)
        nav_buttons = ["Home", "Cart", "Login"]
        for button in nav_buttons:
            if button == "Cart":
                bt = tk.Button(self.navbar, text=button, font="Helvetica 12 bold", bg="#f5c6aa", fg="#e06666",
                          command=lambda: self.cart_gui.open_cart(self.root))
                bt.pack(side=tk.RIGHT, padx=10, pady=10)
            else:
                tk.Button(self.navbar, text=button, font="Helvetica 12 bold", bg="#f5c6aa", fg="#e06666").pack(
                    side=tk.RIGHT, padx=10, pady=10)

        # Footer
        self.footer = tk.Frame(self.root, bg="#0e2d74")
        self.footer.pack(side=tk.BOTTOM, fill=tk.X)

        # Content
        self.contact_label = tk.Label(self.footer, text="Contact Us: +164829435  | Email: SupportTeam@GlowMall.com", font="Verdana 11", fg="white", bg="#0e2d74")
        self.contact_label.pack(side=tk.LEFT, padx=20, pady=10)

        # Title Label
        self.title_label = tk.Label(self.root, text="Welcome to Glow Mall online store", font="Times 40 bold", fg="white", bg="#2d677d")
        self.title_label.pack(pady=10)

        # Text Label
        self.text_label = tk.Label(self.root, text="ORDER ONLINE RIGHT NOW!!", font=" Verdana 40 bold", fg="#f5c6aa", bg="#2d677d")
        self.text_label.pack(side=tk.TOP, anchor=tk.W, padx=10)

        # Categories the user will select
        self.categories = ["Home Appliances", "Electronics", "Fashion", "Books", "Sports"]

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10, padx=10)

        for category in self.categories:
            button = tk.Button(button_frame, text=category, width=15, height=2, font="Verdana 15 bold", fg="#2d677d", bg="#add4e6",
                               command=lambda c=category: self.categories_pages.open_category(c, self.root))  # Call open_category from Categories_pages
            button.pack(side=tk.LEFT, padx=5, pady=5)

        self.root.mainloop()