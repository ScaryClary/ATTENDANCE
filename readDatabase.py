import tkinter as tk
from tkinter import ttk
import sqlite3

def fetch_data():
    """Fetches all customer data from the database."""
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('customers.db')
        cursor = conn.cursor()
        
        # Select all records from the customers table
        # We also select the 'rowid' which is a unique ID for each row
        cursor.execute("SELECT rowid, * FROM customers")
        rows = cursor.fetchall()
        
        return rows
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        if conn:
            conn.close()

def populate_treeview():
    """Clears the treeview and populates it with fresh data from the database."""
    # Clear existing items in the treeview
    for item in tree.get_children():
        tree.delete(item)
    
    # Fetch data and insert into the treeview
    customer_data = fetch_data()
    for row in customer_data:
        tree.insert("", "end", values=row)

# --- GUI Setup ---
# Create the main window
root = tk.Tk()
root.title("Customer Database Viewer")
root.geometry("950x500") # Set a default size

# Create a frame for the Treeview and Scrollbar
frame = tk.Frame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Define the columns for the Treeview
columns = ("id", "name", "birthday", "email", "phone", "address", "contact_method")

tree = ttk.Treeview(frame, columns=columns, show="headings")

# Define headings
tree.heading("id", text="ID")
tree.heading("name", text="Name")
tree.heading("birthday", text="Birthday")
tree.heading("email", text="Email")
tree.heading("phone", text="Phone")
tree.heading("address", text="Address")
tree.heading("contact_method", text="Preferred Contact")

# Configure column widths
tree.column("id", width=40)
tree.column("name", width=150)
tree.column("birthday", width=100)
tree.column("email", width=180)
tree.column("phone", width=120)
tree.column("address", width=200)
tree.column("contact_method", width=120)

# Add a vertical scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.grid(row=0, column=0, sticky='nsew')
scrollbar.grid(row=0, column=1, sticky='ns')

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Create a Refresh button
refresh_button = ttk.Button(root, text="Refresh Data", command=populate_treeview)
refresh_button.pack(pady=10)

# --- Initial Data Load ---
# Populate the treeview with data when the app starts
populate_treeview()

# Start the Tkinter event loop
root.mainloop()