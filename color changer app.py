import tkinter as tk
import random 

#CREATE WINDOW 
root = tk.Tk()
root.title("Color Changer App")
root.geometry("300x200")
root.config(bg="#fae6f5")

#COLORS 
color = {
    "Light Pink": "#ffb6b6",
    "Sky Blue":"#00bfff",
    "Peach Pink": "#f569ff",
    "Mint Blue": "#b2dfdb",
    "Lavender": "#d1f2eb",
    "Cream": "#fef9f5",
    "Soft Yellw": "#ffddc1",
    "Neon Green": "#00ff7f"
}

#FUNCTION TO CHANGE
def change_color():
    name, hex_code = random.choice(list(color.items()))
    root.config(bg = hex_code)
    label.config(bg= hex_code, text = f"current color:{name} ({hex_code}")
    button.config(bg=hex_code,text = "change color", command = change_color)

#UI
label = tk.Label(root, text = "Namaste",font = ("georgia",22),bg = "#fae6f5")
label.pack(pady=40)
button = tk.Button(root, text = "magic color",font= ("segoe UI",20),bg ="#ffd6e0",command = change_color)
button.pack(pady=20)

root.mainloop()
