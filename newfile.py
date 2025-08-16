import customtkinter as ctk
from tkinter import ttk

# ==== App Theme Settings ====
ctk.set_appearance_mode("Dark")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")

# ==== Main Window ====
app = ctk.CTk()
app.geometry("500x300")
app.title("CustomTkinter + Treeview Example")

# ==== Frame for Treeview ====
frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# ==== Scrollbar ====
tree_scroll = ctk.CTkScrollbar(frame)
tree_scroll.pack(side="right", fill="y")

# ==== Treeview Widget ====
tree = ttk.Treeview(frame, columns=("Age", "City"), show="headings", yscrollcommand=tree_scroll.set)
tree.heading("Age", text="Age")
tree.heading("City", text="City")
tree.column("Age", width=100)
tree.column("City", width=200)

# Link scrollbar to treeview
tree_scroll.configure(command=tree.yview)

# ==== Sample Data ====
data = [
    (25, "New York"),
    (30, "London"),
    (22, "Tokyo"),
    (28, "Paris"),
    (35, "Sydney")
]

for row in data:
    tree.insert("", "end", values=row)

tree.pack(fill="both", expand=True)

# ==== Treeview Styling ====
style = ttk.Style()
style.theme_use("clam")  # More modern look

# Set background colors to match CustomTkinter
bg_color = "#2b2b2b" if ctk.get_appearance_mode() == "Dark" else "#f0f0f0"
fg_color = "white" if ctk.get_appearance_mode() == "Dark" else "black"

style.configure(
    "Treeview",
    background=bg_color,
    foreground=fg_color,
    rowheight=25,
    fieldbackground=bg_color
)
style.map("Treeview", background=[("selected", "#1f6aa5")])

app.mainloop()
