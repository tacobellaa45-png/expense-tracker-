import tkinter as tk

#create window 
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x300")
root.config(bg =  "#fae6f5")

total = 0

#functions
def add_expense():
    global total

    name = entry.get()
    amount = amount_entry.get()
    
   
    if name != "" and amount.isdigit():
     listbox.insert(tk.END, f"{name} - Rs.{amount}")
     total += int(amount)
     total_label.config(text = f"Total: Rs.{total}")
     entry.delete(0,tk.END)
     amount_entry.delete(0,tk.END)
    else:
        total_label.config(text = "Enter valid name and amount")

entry = tk.Entry(root)
entry.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

add_button = tk.Button(root,text = "Add", command = add_expense)
add_button.pack()

listbox = tk.Listbox(root)
listbox.pack()

total_label = tk.Label(root, text = "Total: Rs.0")
total_label.pack()
#UI
label = tk.Label(root,text = "Expense", font = ("georgia",28), bg = "#fae6f5")
label.pack(pady = 40)

root.mainloop()