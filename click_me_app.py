import tkinter as tk
import random

# Create window
root = tk.Tk()
root.title("Click Me App")
root.geometry("400x300")
root.configure(bg="#fef9f5")

# Fun messages
messages = ["You're awesome!", "Keep smiling 😊", "Have a great day!", "You rock 🤘", "Hello sunshine! 🌞"]

# Function to change text
def on_click():
    new_text = random.choice(messages)
    label.config(text=new_text)
    button.config(text="Click Me Again!")

# UI
label = tk.Label(root, text="Welcome!", font=("Arial", 18), bg="#fef9f5")
label.pack(pady=40)

button = tk.Button(root, text="Click Me!", font=("Arial", 16), bg="#ffd6e0", command=on_click)
button.pack(pady=20)

# Run the app
root.mainloop()
