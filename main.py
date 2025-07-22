# Code to generate colour palattes. 
import tkinter as tk
import random

root = tk.Tk()
root.title("Colour Palette Generator")
root.geometry("300x600")


select_filed = tk.StringVar()
select = tk.OptionMenu(root, select_filed, "1", "2", "3", "4", "5")
select.pack(side="top", pady=10)


root.mainloop()