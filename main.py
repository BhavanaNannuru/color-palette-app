# Code to generate colour palattes. 
import tkinter as tk
import random

def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)  
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'

def generate_palette():
    num_colors = int(select_filed.get())
    for widget in color_frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()
    for i in range(num_colors):
        color = generate_color()
        color_label = tk.Label(color_frame, text="", bg=color, width=10, height=5)
        color_label.grid(row=i, column=0, padx=5, pady=5)
        hex_label = tk.Label(color_frame, text=color, width=10, bg="#F5F5DC", fg="black", font=("Arial", 10))
        hex_label.grid(row=i, column=1, padx=5, pady=5)


root = tk.Tk()
root.configure(bg="#F5F5DC")
root.title("Colour Palette Generator")
root.geometry("300x600")


select_filed = tk.StringVar()
select = tk.OptionMenu(root, select_filed, "1", "2", "3", "4", "5")
select.config(bg="#FFF8E7", fg="black", activebackground="#E8E4C9", activeforeground="black", highlightthickness=0)
select["menu"].config(bg="#FFF8E7", fg="black")
select.pack(side="top", pady=10)
select_filed.set("1")  # Default value

generate_button = tk.Button(root, text="Generate Palette", command=generate_palette, bg="#FFF8E7", fg="black", activebackground="#E8E4C9", activeforeground="black")

generate_button.pack(side="top")

color_frame = tk.Frame(root, bg="#F5F5DC")
color_frame.pack(pady=10)


root.mainloop()