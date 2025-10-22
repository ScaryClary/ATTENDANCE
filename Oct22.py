import tkinter as tk
from openai import OpenAI  # <-- 1. Added the OpenAI import
import grantsAPIKey

apikey = grantsAPIKey.OPENAI_API_KEY
# --- Initialize the OpenAI client ---
# This attempts to initialize the client when the script starts.
# It relies on the OPENAI_API_KEY environment variable being set.
try:
    client = OpenAI(
        api_key=apikey
    )
    CLIENT_INITIALIZED = True
    print("OpenAI client initialized successfully.")
except Exception as e:
    print(f"Error: Failed to initialize OpenAI client: {e}")
    print("Please make sure your OPENAI_API_KEY environment variable is set.")
    client = None
    CLIENT_INITIALIZED = False

def submit_question():
    """
    Gets the question from the input box, sends it to the
    OpenAI API (using the structure you provided),
    and displays the answer.
    """
    question = question_entry.get("1.0", tk.END).strip()
    answer = "" # Initialize answer variable

    if not question:
        answer = "Please enter a question first!"
    elif not CLIENT_INITIALIZED:
        # Check if the client failed to initialize earlier
        answer = "Error: OpenAI client is not initialized.\nDid you set your OPENAI_API_KEY?"
    else:
        try:
            # --- 2. This is the API logic you provided ---
            # Show a "loading" message in the GUI
            answer_output.config(state='normal')
            answer_output.delete("1.0", tk.END)
            answer_output.insert(tk.END, "Getting answer...")
            answer_output.config(state='disabled')
            # Force the GUI to update *now* before the API call (which can be slow)
            root.update_idletasks() 

            # Make the API call using your code structure
            response = client.responses.create(
                model="gpt-5",   # Using the model from your documentation
                input=question   # Passing the user's question as input
            )
            
            answer = response.output_text  # Getting the answer as specified
            # ----------------------------------------------

        except Exception as e:
            # Handle API errors (e.g., key invalid, model doesn't exist)
            answer = f"An API error occurred:\n{e}"

    # --- 3. Update the answer box with the final answer ---
    # Set the state to 'normal' so we can modify it
    answer_output.config(state='normal')
    
    # Clear any previous content (like the "Getting answer..." message)
    answer_output.delete("1.0", tk.END)
    
    # Insert the new answer
    answer_output.insert(tk.END, answer)
    
    # Set the state back to 'disabled' to make it read-only
    answer_output.config(state='disabled')

# --- Create the main window ---
root = tk.Tk()
root.title("Simple Q&A GUI")
root.geometry("500x450")

# --- Create the Widgets ---
question_label = tk.Label(root, text="Ask your question:")
question_entry = tk.Text(root, height=5, width=60)
submit_button = tk.Button(root, text="Submit", command=submit_question)
answer_label = tk.Label(root, text="Answer:")
answer_output = tk.Text(root, height=10, width=60, state='disabled', wrap='word')

# --- Arrange the Widgets on the Window ---
question_label.pack(pady=(10, 5))
question_entry.pack(pady=5, padx=10)
submit_button.pack(pady=10)
answer_label.pack(pady=5)
answer_output.pack(pady=5, padx=10)

# --- Start the Application ---
root.mainloop()