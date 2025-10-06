# Customer Information Management System

A simple desktop application built with Python and Tkinter for entering and viewing customer information. The application uses a local SQLite database to persist data.

---

## Features

* **Data Entry GUI**: A clean and simple form for users to input customer details.
* **Persistent Storage**: Customer data is saved to a local SQLite database file (`customers.db`).
* **Database Viewer**: A separate script that displays all customer records from the database in a clear, tabular format.
* **Live Refresh**: The database viewer includes a "Refresh" button to load new entries without restarting the application.

---

## Files in This Repository

* `FP5 main.py`
    * The main application file. Run this to open the GUI for customer data entry. Information submitted through this form is saved directly to `customers.db`.

* `readDatabase.py`
    * A utility script to view the contents of the database. Run this to open a separate window displaying all customer records in a table.

* `customers.db`
    * The SQLite database file where all customer information is stored. This file will be created automatically if it doesn't exist when you first submit a customer's data.

---

## How to Use

### Prerequisites

You need to have **Python 3** installed on your system. The required libraries (`tkinter` and `sqlite3`) are part of the standard Python library, so no additional installations are necessary.

### Running the Application

1.  **Clone or download the repository** to your local machine.
2.  Navigate to the project folder in your terminal.

#### To Add a New Customer:

Run the main data entry application.
```bash
python "FP5 main.py"