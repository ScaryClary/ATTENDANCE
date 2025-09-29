import tkinter as tk

def create_gui():
    """
    This function creates the main Tkinter window with a greeting, 
    four language selection buttons, and a label for the output.
    """
    window = tk.Tk()
    window.title("Language Selector")
    window.geometry("300x250")

    # A dictionary to store the "Hello" translations
    greetings = {
        "espanol": "Hola",
        "francais": "Bonjour",
        "deutsch": "Hallo",
        "english": "Hello"
    }

    # Greeting label
    greeting_label = tk.Label(window, text="Welcome. Select any language.", font=("Arial", 14))
    greeting_label.pack(pady=10)

    # Function to update the output label based on the button clicked
    def update_label(language):
        """
        Updates the output label with the correct greeting.
        """
        output_label.config(text=greetings[language.lower()])

    # Create and pack the buttons in a column
    # The order of these pack() calls is what determines their placement
    languages = ["Espanol", "Francais", "Deutsch", "English"]
    for lang in languages:
        button = tk.Button(window, text=lang, command=lambda l=lang: update_label(l))
        button.pack(pady=5)
    
    # Output label (initially blank)
    # This label is created and packed last, so it will appear at the bottom
    output_label = tk.Label(window, text="", font=("Arial", 16, "bold"))
    output_label.pack(pady=10)
    
    # Start the GUI event loop
    window.mainloop()

# Run the function to create the GUI
create_gui()