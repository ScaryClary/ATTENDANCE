import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Simple Tkinter App")
window.geometry("400x200")

def on_button_click():
    """
    This function is called when the button is clicked.
    It gets the text from the text box and displays it in the output label.
    """
    user_input = text_box.get()
    if user_input:
        output_label.config(text=f"You entered: {user_input}")
    else:
        messagebox.showwarning("Warning", "Please enter some text!")

# Create a text box (Entry widget)
text_box = tk.Entry(window, width=15)
text_box.pack(pady=10)

# Create a button
my_button = tk.Button(window, text="Click Me", command=on_button_click)
my_button.pack(pady=5)

# Create a label for output
output_label = tk.Label(window, text="", font=("Helvetica", 12))
output_label.pack(pady=10)

# Start the application's main loop
window.mainloop()