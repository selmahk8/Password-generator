#generate password which is tough to break

import random
import tkinter as tk

def generate_password():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbols = "@#$%&*/?.!"
    
    use_for = lower_case + upper_case + number + symbols
    length_for_pass = 8
    
    password = "".join(random.sample(use_for, length_for_pass))
    
    result_label.config(text="Your generated password is : " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x150")

# Create and configure a label
label = tk.Label(root, text="Click the button to generate a password:")
label.pack(pady=10)

# Create and configure a button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Create and configure a label to display the generated password
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the GUI main loop
root.mainloop()
