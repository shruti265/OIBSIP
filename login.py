import tkinter as tk
from tkinter import messagebox

# Dictionary to store user data
user_data = {}

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login App")
        self.geometry("300x250")

        # Create labels and entry fields
        tk.Label(self, text="Username:").pack(pady=10)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password:").pack(pady=10)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        # Create login button
        login_button = tk.Button(self, text="Login", command=self.login)
        login_button.pack(pady=10)

        # Create sign up button
        signup_button = tk.Button(self, text="Sign Up", command=self.open_signup_window)
        signup_button.pack(pady=10)

        # Initialize the homepage frame
        self.home_page_frame = tk.Frame(self)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if username and password match stored data
        if username in user_data and user_data[username] == password:
            # Clear the login window
            for widget in self.winfo_children():
                widget.destroy()

            # Create the homepage frame and add it to the window
            self.home_page_frame = tk.Frame(self)
            self.home_page_frame.pack()

            # Create the homepage content
            HomePage(self.home_page_frame, self)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def open_signup_window(self):
        SignUpWindow(self)

class SignUpWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Sign Up")
        self.geometry("300x250")

        # Create labels and entry fields for sign up
        tk.Label(self, text="Username:").pack(pady=10)
        self.new_username_entry = tk.Entry(self)
        self.new_username_entry.pack()

        tk.Label(self, text="Password:").pack(pady=10)
        self.new_password_entry = tk.Entry(self, show="*")
        self.new_password_entry.pack()

        tk.Label(self, text="Confirm Password:").pack(pady=10)
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry.pack()

        # Create sign up button
        signup_button = tk.Button(self, text="Sign Up", command=self.sign_up)
        signup_button.pack(pady=20)

    def sign_up(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Perform sign up logic here
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
        elif username in user_data:
            messagebox.showerror("Error", "Username already exists")
        else:
            user_data[username] = password  # Store user data
            messagebox.showinfo("Success", "Sign up successful!")
            self.destroy()  # Close the sign up window

class HomePage:
    def __init__(self, parent_frame, parent_window):
        self.parent_frame = parent_frame
        self.parent_window = parent_window

        # Add your home page design and content here
        tk.Label(self.parent_frame, text="Welcome to the Home Page", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.parent_frame, text="Logout", command=self.logout).pack(pady=10)

    def logout(self):
        # Clear the homepage frame
        for widget in self.parent_frame.winfo_children():
            widget.destroy()

        # Recreate the login window
        tk.Label(self.parent_window, text="Username:").pack(pady=10)
        self.parent_window.username_entry = tk.Entry(self.parent_window)
        self.parent_window.username_entry.pack()

        tk.Label(self.parent_window, text="Password:").pack(pady=10)
        self.parent_window.password_entry = tk.Entry(self.parent_window, show="*")
        self.parent_window.password_entry.pack()

        login_button = tk.Button(self.parent_window, text="Login", command=self.parent_window.login)
        login_button.pack(pady=10)

        signup_button = tk.Button(self.parent_window, text="Sign Up", command=self.parent_window.open_signup_window)
        signup_button.pack(pady=10)

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
