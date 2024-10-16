import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Categories1 import CategoriesPages
from HomePage import HomePage
from cart import Cart
from item import Item
from tki import CartGUI
# UserManagement and LoginRegisterApp class
class UserManagement:
    def __init__(self):
        self.data_user = [{"name": "Aya", "password": "aya1223", "national_id": 12345, "mail": "aya@gmail.com",
                           "phone_number": 1273152849, "gender": "female", "age": 19, "government": "Cairo"}]
        self.admin_mail = "admin@gmail.com"
        self.admin_password = "admin123"

    def register_user(self, name, password, national_id, mail, phone_number, gender, age, government):
        self.data_user.append({
            "name": name,
            "password": password,
            "national_id": national_id,
            "mail": mail,
            "phone_number": phone_number,
            "gender": gender,
            "age": age,
            "government": government
        })
        messagebox.showinfo("Registration", "Registration successful!")

    def authenticate_user(self, mail, password):
        if mail == self.admin_mail and password == self.admin_password:
            return "admin"
        for user in self.data_user:
            if user["mail"] == mail and user["password"] == password:
                return user["name"]
        return None


class LoginRegisterApp:
    def __init__(self):
        self.user_management = UserManagement()

        self.root = tk.Tk()
        self.root.title("Roe Store")
        self.root.geometry("800x600")
        self.root.configure(bg="#26333b")
        self.cart_gui = CartGUI(cart)
        self.cart = Cart()
        self.current_page = "login"
        self.show_login_page()


    def show_login_page(self):
        self.clear_frame()
        self.current_page = "login"

        tk.Label(self.root, text="USER LOGIN", font="Times 30 bold", bg="#26333b", fg="white").pack(pady=20)
        tk.Label(self.root, text="Email:", font="Georgia 12 bold", bg="#26333b", fg="white").pack(pady=5)
        self.email_entry = tk.Entry(self.root, width=30, font="Georgia 11")
        self.email_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", font="Georgia 12 bold", bg="#26333b", fg="white").pack(pady=5)
        self.password_entry = tk.Entry(self.root, width=30, font="Georgia 11", show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login", font="Times 16", bg="#15355a", fg="white", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Register", font="Times 16", bg="#26333b", fg="white", command=self.show_register_page).pack(pady=10)

    def show_register_page(self):
        self.clear_frame()
        self.current_page = "register"

        tk.Label(self.root, text="USER REGISTRATION", font="Times 30 bold", bg="#2b4951", fg="white").pack(pady=20)
        self.create_register_form()

        tk.Button(self.root, text="Register", font="Times 16", bg="#2b4951", fg="white", command=self.register).pack(pady=10)
        tk.Button(self.root, text="Back to Login", font="Times 16", bg="#2b4951", fg="white", command=self.show_login_page).pack(pady=10)

    def create_register_form(self):
        self.name_entry = self.create_entry("Name:", "#2b4951")
        self.password_entry = self.create_entry("Password:", "#2b4951", show="*")
        self.national_id_entry = self.create_entry("National ID:", "#2b4951")
        self.mail_entry = self.create_entry("Email:", "#2b4951")
        self.phone_number_entry = self.create_entry("Phone Number:", "#2b4951")
        self.gender_entry = self.create_entry("Gender:", "#2b4951")
        self.age_entry = self.create_entry("Age:", "#2b4951")
        self.government_entry = self.create_entry("Government:", "#2b4951")

    def create_entry(self, label_text, bg_color, show=None):
        tk.Label(self.root, text=label_text, font="Georgia 12 bold", bg=bg_color, fg="white").pack(pady=5)
        entry = tk.Entry(self.root, width=30, font="Georgia 11", show=show)
        entry.pack(pady=5)
        return entry

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        mail = self.email_entry.get()
        password = self.password_entry.get()
        result = self.user_management.authenticate_user(mail, password)

        if result == "admin":
            messagebox.showinfo("Login", "Admin logged in successfully!")
            self.redirect_to_home_page(True)
        elif result:
            messagebox.showinfo("Login", f"Welcome back, {result}!")
            self.redirect_to_home_page(False)
        else:
            messagebox.showerror("Login Error", "Invalid email or password!")

    def register(self):
        name = self.name_entry.get()
        password = self.password_entry.get()
        national_id = self.national_id_entry.get()
        mail = self.mail_entry.get()
        phone_number = self.phone_number_entry.get()
        gender = self.gender_entry.get()
        age = self.age_entry.get()
        government = self.government_entry.get()

        if not (name and password and national_id and mail and phone_number and gender and age and government):
            messagebox.showwarning("Registration Error", "All fields must be filled!")
            return

        self.user_management.register_user(name, password, national_id, mail, phone_number, gender, age, government)
        self.show_login_page()  # Redirect back to login page after registration

    def redirect_to_home_page(self, is_admin):
        self.clear_frame()
        self.root.destroy()  # Close the current window
        home_page = HomePage(CategoriesPages(cart, is_admin), self.cart_gui)  # Create an instance of CategoriesPages and pass it to HomePage
        home_page.root.mainloop()

# Main execution
cart = Cart()
is_admin = False
categories_pages= CategoriesPages(cart, is_admin)
cart_gui = CartGUI(cart)
login_app = LoginRegisterApp()
login_app.root.mainloop()
