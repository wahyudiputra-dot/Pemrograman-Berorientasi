import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Aplikasi Tkinter")
root.geometry("300x200")

# Header Label
tk.Label(root, text="Widget", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Contoh", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)

# Button 
tk.Label(root, text="Button").grid(row=1, column=0, sticky='w', padx=10)
tk.Button(root, text="Klik Saya").grid(row=1, column=1, sticky='w', padx=10)

# Check Button
tk.Label(root, text="Checkbutton").grid(row=2, column=0, sticky='w', padx=10)
check_var = tk.BooleanVar()
tk.Checkbutton(root, text="Centang Saya", variable=check_var).grid(row=2, column=1, sticky='w', padx=10)

# Entry
tk.Label(root, text="Entry").grid(row=3, column=0, sticky='w', padx=10)
tk.Entry(root).grid(row=3, column=1, sticky='w', padx=10)

# Text
tk.Label(root, text="Text").grid(row=4, column=0, sticky='nw', padx=10)
text_box = tk. Text(root, height=3, width=30)
text_box.grid(row=4, column=1, sticky='w', padx=10)

# Canvas
tk.Label(root, text="Canvas").grid(row=5, column=0, sticky='w', padx=10)
canvas = tk.Canvas(root, width=100, height=50, bg='lightblue')
canvas.create_oval(10, 10, 90, 40, fill="green")
canvas.grid(row=5, column=1, sticky='w', padx=10)

# Radiobutton
tk.Label(root, text="Radiobutton").grid(row=6, column=0, sticky='w', padx=10)
radio_var = tk.StringVar()
tk.Radiobutton(root, text="Opsi A", variable=radio_var, value="A").grid(row=6, column=1, sticky='w')
tk.Radiobutton(root, text="Opsi B", variable=radio_var, value="B").grid(row=6, column=1, padx=100, sticky='w')

# Listbox
tk.Label(root, text="Listbox").grid(row=7, column=0, sticky='w', padx=10)
listbox = tk.Listbox(root, height=3)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.grid(row=7, column=1, sticky='w')

# Scale
tk.Label(root, text="Scale").grid(row=9, column=0, sticky='w', padx=10)
tk.Scale(root, from_= 0, to=10, orient='horizontal').grid(row=9, column=1, sticky='w')

# Scrollbar
tk.Label(root, text="Scrollbar").grid(row=10, column=0, sticky='nw', padx=10)
scroll_text = tk.Text(root, height=3, width=30)
scrollbar = tk.Scrollbar(root, command=scroll_text.yview)
scroll_text.config(yscrollcommand=scrollbar.set)
scroll_text.grid(row=10, column=1, sticky='w')
scrollbar.grid(row=10, column=2, sticky='ns')

root.mainloop()
