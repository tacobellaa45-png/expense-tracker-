
import tkinter as tk
from tkinter import ttk, messagebox

trades = []

def add_trade():
    name = entry_name.get()
    buy_price = entry_buy.get()
    sell_price = entry_sell.get()
    qty = entry_qty.get()

    if not name or not buy_price or not sell_price or not qty:
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    try:
        buy_price = float(buy_price)
        sell_price = float(sell_price)
        qty = int(qty)
    except ValueError:
        messagebox.showwarning("Input Error", "Enter valid numbers")
        return

    profit_loss = (sell_price - buy_price) * qty
    trades.append((name, buy_price, sell_price, qty, profit_loss))
    update_table()

    # Clear fields after adding
    entry_name.delete(0, tk.END)
    entry_buy.delete(0, tk.END)
    entry_sell.delete(0, tk.END)
    entry_qty.delete(0, tk.END)

def update_table():
    for row in tree.get_children():
        tree.delete(row)

    for trade in trades:
        tree.insert("", tk.END, values=trade)

# Tkinter Window
root = tk.Tk()
root.title("Simple Trading Tracker")

# Labels and Entries
tk.Label(root, text="Stock/Crypto Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Buy Price:").grid(row=1, column=0, padx=5, pady=5)
entry_buy = tk.Entry(root)
entry_buy.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Sell Price:").grid(row=2, column=0, padx=5, pady=5)
entry_sell = tk.Entry(root)
entry_sell.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Quantity:").grid(row=3, column=0, padx=5, pady=5)
entry_qty = tk.Entry(root)
entry_qty.grid(row=3, column=1, padx=5, pady=5)

tk.Button(root, text="Add Trade", command=add_trade).grid(row=4, column=0, columnspan=2, pady=10)

# Table
columns = ("Name", "Buy Price", "Sell Price", "Quantity", "Profit/Loss")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()