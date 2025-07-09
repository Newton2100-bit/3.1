import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My App")

# Create widgets
label = ttk.Label(root, text="Hello, Tkinter!")
button = ttk.Button(root, text="Click Me", command=lambda: label.config(text="Clicked!"))

# Layout widgets
label.pack(pady=100)
button.pack(pady=100)

root.mainloop()
