import tkinter as tk
from tkinter import ttk

# --- FUNCTIONS ---
def submit_feedback():
    """
    This function is called when the submit button is clicked.
    It retrieves the text from the input fields, prints it to the console,
    and then clears the fields.
    """
    name = name_entry.get()
    email = email_entry.get()
    # For the Text widget, get text from the beginning (1.0) to the end (tk.END).
    # The .strip() removes any extra newline character that get() often includes.
    feedback = feedback_text.get("1.0", tk.END).strip()

    print("--- FEEDBACK SUBMITTED ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Feedback: {feedback}")
    print("--------------------------\n")

    # Clear the entry and text widgets after submission
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    feedback_text.delete("1.0", tk.END)

# --- GUI SETUP ---
# Create the main application window
window = tk.Tk()
window.title("tk")
window.geometry("480x350") # Set a fixed initial size
window.resizable(False, False) # Prevent the window from being resized

# Create a main frame to hold all the widgets
frame = ttk.Frame(window, padding="20")
frame.pack(fill="both", expand=True)

# --- WIDGETS ---
# 1. Header Label
header_label = ttk.Label(
    frame,
    text="Please provide feedback on your experience",
    font=("Helvetica", 16, "bold") # Set a larger, bold font
)
# Place the header in the grid, spanning two columns
header_label.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="w")

# 2. Name Label and Entry Box
name_label = ttk.Label(frame, text="Name:")
name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e") # Align right
name_entry = ttk.Entry(frame, width=40)
name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w") # Align left
name_entry.insert(0, "Grant Clary") # Pre-fill with sample text

# 3. Email Label and Entry Box
email_label = ttk.Label(frame, text="Email:")
email_label.grid(row=2, column=0, padx=5, pady=5, sticky="e") # Align right
email_entry = ttk.Entry(frame, width=40)
email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w") # Align left
email_entry.insert(0, "gclary@tntech.edu") # Pre-fill with sample text

# 4. Feedback Label and Text Box
feedback_label = ttk.Label(frame, text="Feedback:")
feedback_label.grid(row=3, column=0, padx=5, pady=5, sticky="ne") # Align top-right
# Use a standard tk.Text widget for multi-line input
feedback_text = tk.Text(frame, width=30, height=8, wrap="word")
feedback_text.grid(row=3, column=1, padx=5, pady=5, sticky="w") # Align left
feedback_text.insert("1.0", "Sample of feedback comments.") # Pre-fill

# 5. Submit Button
submit_button = ttk.Button(frame, text="Submit", command=submit_feedback)
submit_button.grid(row=4, column=1, pady=20, sticky="e") # Align right

# --- START THE APPLICATION ---
# This line starts the Tkinter event loop, which waits for user actions.
window.mainloop()