import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# --- Database Functions ---

def setup_database():
    """Creates the database and the customers table if they don't exist."""
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()
    # Create table with an auto-incrementing primary key for unique identification
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birthday TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            contact_method TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_customer_data(name, birthday, email, phone, address, contact_method):
    """Saves a new customer's data to the database."""
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()
    sql = '''
        INSERT INTO customers (name, birthday, email, phone, address, contact_method)
        VALUES (?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(sql, (name, birthday, email, phone, address, contact_method))
    conn.commit()
    conn.close()

# --- GUI Functions ---

def submit_data():
    """Handles the submit button click event."""
    # Get data from entry fields
    name = name_entry.get()
    birthday = birthday_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    contact_method = contact_var.get()

    # Basic validation: Ensure name is not empty
    if not name:
        messagebox.showerror("Error", "Name field cannot be empty.")
        return

    # Save data to the database
    save_customer_data(name, birthday, email, phone, address, contact_method)

    # Show success message
    messagebox.showinfo("Success", "Customer information saved successfully!")

    # Clear the form
    clear_form()

def clear_form():
    """Clears all the input fields in the GUI."""
    name_entry.delete(0, tk.END)
    birthday_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    contact_var.set(contact_options[0]) # Reset dropdown to the first option

# --- GUI Setup ---
# Initialize the main window
root = tk.Tk()
root.title("Customer Information Form")
root.geometry("450x300")
root.resizable(False, False)

# Create a frame for the form
frame = ttk.Frame(root, padding="20")
frame.pack(fill="both", expand=True)

# --- Form Fields ---

# Name
ttk.Label(frame, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
name_entry = ttk.Entry(frame, width=40)
name_entry.grid(row=0, column=1, sticky="ew")

# Birthday
ttk.Label(frame, text="Birthday (YYYY-MM-DD):").grid(row=1, column=0, sticky="w", pady=5)
birthday_entry = ttk.Entry(frame, width=40)
birthday_entry.grid(row=1, column=1, sticky="ew")

# Email
ttk.Label(frame, text="Email:").grid(row=2, column=0, sticky="w", pady=5)
email_entry = ttk.Entry(frame, width=40)
email_entry.grid(row=2, column=1, sticky="ew")

# Phone Number
ttk.Label(frame, text="Phone Number:").grid(row=3, column=0, sticky="w", pady=5)
phone_entry = ttk.Entry(frame, width=40)
phone_entry.grid(row=3, column=1, sticky="ew")

# Address
ttk.Label(frame, text="Address:").grid(row=4, column=0, sticky="w", pady=5)
address_entry = ttk.Entry(frame, width=40)
address_entry.grid(row=4, column=1, sticky="ew")

# Preferred Contact Method Dropdown
ttk.Label(frame, text="Contact Method:").grid(row=5, column=0, sticky="w", pady=5)
contact_options = ["Email", "Phone", "Mail"]
contact_var = tk.StringVar(root)
contact_var.set(contact_options[0]) # Set default value
contact_menu = ttk.OptionMenu(frame, contact_var, contact_options[0], *contact_options)
contact_menu.grid(row=5, column=1, sticky="ew")

# --- Submit Button ---
submit_button = ttk.Button(frame, text="Submit", command=submit_data)
submit_button.grid(row=6, column=0, columnspan=2, pady=20)


# --- Main Loop ---
if __name__ == "__main__":
    setup_database() # Ensure the database and table are ready
    root.mainloop() # Start the GUI event loop