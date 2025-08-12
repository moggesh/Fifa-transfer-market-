import tkinter as tk

root = tk.Tk()
root.title("Fifa Transfer Market")
root.geometry("500x700")
root.configure(bg="lightblue")

    

def on_clubs():
    for widget in root.winfo_children():
        widget.destroy()

    available = tk.Label(root, text="These are the available clubs ",font=("Arial", 14), fg="blue")
    available.pack(pady=10)


def on_player():
    for widget in root.winfo_children():
        widget.destroy()
        
    application = tk.Label(root, text="Please submit your details ",font=("Arial", 14))
    application.pack(pady=10)
    
    name1 = tk.Entry(root,width = 50)
    name1.pack(pady=5)
    name1.insert(0,"Enter player name: ")

    nationality1 = tk.Entry(root,width = 50)
    nationality1.pack(pady=5)
    nationality1.insert(0,"Enter player nationality: ")

    position1 = tk.Entry(root,width = 50)
    position1.pack(pady=5)
    position1.insert(0,"Enter player position: ")

    
    salary1 = tk.Entry(root,width = 50, )
    salary1.pack(pady=5)
    salary1.insert(0,"Enter expected salary: ",)

    age1 = tk.Entry(root,width = 50)
    age1.pack(pady=5)
    age1.insert(0,"Enter player age: ")

    enter1 = tk.Button(root, text="Enter", width=15, command=on_clubs)
    enter1.pack(pady=5)

def on_player_list():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Name", width=15, bg="lightblue", font=('Arial', 10, 'bold'), relief="solid").grid(row=0, column=0)
    tk.Label(root, text="Age", width=10, bg="lightblue", font=('Arial', 10, 'bold'), relief="solid").grid(row=0, column=1)
    tk.Label(root, text="Salary", width=15, bg="lightblue", font=('Arial', 10, 'bold'), relief="solid").grid(row=0, column=2)

    tk.Label(root, text="Virat Kohli", width=15, relief="solid").grid(row=1, column=0)
    tk.Label(root, text="36", width=10, relief="solid").grid(row=1, column=1)
    tk.Label(root, text="$1,000,000", width=15, relief="solid").grid(row=1, column=2)

    # Row 2
    tk.Label(root, text="Rohit Sharma", width=15, relief="solid").grid(row=2, column=0)
    tk.Label(root, text="38", width=10, relief="solid").grid(row=2, column=1)
    tk.Label(root, text="$950,000", width=15, relief="solid").grid(row=2, column=2)

    # Row 3
    tk.Label(root, text="Shubman Gill", width=15, relief="solid").grid(row=3, column=0)
    tk.Label(root, text="25", width=10, relief="solid").grid(row=3, column=1)
    tk.Label(root, text="$700,000", width=15, relief="solid").grid(row=3, column=2)

    # Row 4
    tk.Label(root, text="Jasprit Bumrah", width=15, relief="solid").grid(row=4, column=0)
    tk.Label(root, text="31", width=10, relief="solid").grid(row=4, column=1)
    tk.Label(root, text="$800,000", width=15, relief="solid").grid(row=4, column=2)

    # Row 5
    tk.Label(root, text="Ravindra Jadeja", width=15, relief="solid").grid(row=5, column=0)
    tk.Label(root, text="37", width=10, relief="solid").grid(row=5, column=1)
    tk.Label(root, text="$850,000", width=15, relief="solid").grid(row=5, column=2)
    
def on_manager():
    for widget in root.winfo_children():
        widget.destroy()

    position2 = tk.Label(root, text="Select position",bg="lightblue", font=("Arial", 14))
    position2.pack(pady=10)

    button_frame = tk.Frame(root,bg="lightblue")
    button_frame.pack(pady=20)

    cb = tk.Button(button_frame, text="GK", width=10, bg="lightgreen")
    cb.pack(side="left", padx=5)

    fb = tk.Button(button_frame, text="CB", width=10, bg="lightgreen")
    fb.pack(side="left", padx=5)

    gk = tk.Button(button_frame, text="FB", width=10, bg="lightgreen")
    gk.pack(side="left", padx=5)

    cm = tk.Button(button_frame, text="CM", width=10, bg="lightgreen")
    cm.pack(side="left", padx=5)

    st = tk.Button(button_frame, text="ST", width=10, bg="lightgreen")
    st.pack(side="left", padx=5)

    age2 = tk.Label(root, text="Select age",bg="lightblue", font=("Arial", 14))
    age2.pack(pady=10)

    button_frame_2 = tk.Frame(root,bg="lightblue")
    button_frame_2.pack(pady=20)

    a = tk.Button(button_frame_2, text="14-19", width=10, bg="lightgreen")
    a.pack(side="left", padx=5)

    b = tk.Button(button_frame_2, text="20-25", width=10, bg="lightgreen")
    b.pack(side="left", padx=5)

    c = tk.Button(button_frame_2, text="25-30", width=10, bg="lightgreen")
    c.pack(side="left", padx=5)

    d = tk.Button(button_frame_2, text="30-35", width=10, bg="lightgreen")
    d.pack(side="left", padx=5)

    e = tk.Button(button_frame_2, text="35+", width=10, bg="lightgreen")
    e.pack(side="left", padx=5)

    salary3 = tk.Label(root, text="How much can you pay(Daily wage)",bg="lightblue", font=("Arial", 14))
    salary3.pack(pady=10)

    button_frame_3 = tk.Frame(root,bg="lightblue")
    button_frame_3.pack(pady=20)

    f = tk.Button(button_frame_3, text="€1000", width=10, bg="lightgreen",command=fade)
    f.pack(side="left", padx=5)

    g = tk.Button(button_frame_3, text="€5000", width=10, bg="lightgreen")
    g.pack(side="left", padx=5)

    h = tk.Button(button_frame_3, text="€10000", width=10, bg="lightgreen")
    h.pack(side="left", padx=5)

    i = tk.Button(button_frame_3, text="€30000", width=10, bg="lightgreen")
    i.pack(side="left", padx=5)

    j = tk.Button(button_frame_3, text="€50000", width=10, bg="lightgreen")
    j.pack(side="left", padx=5)

    entering_market = tk.Label(root, text="Hereby, you are entering the transfer market:", font=("Arial", 10), bg="lightblue")
    entering_market.place(x=40,y=375)

    entering_market_2= tk.Button(root, text="Enter", width=15, command=on_player_list)
    entering_market_2.place(x=40,y=400)



instruction = tk.Label(root, text="WELCOME TO THE TRANSFER MARKET", font=("Arial", 14))
instruction.pack(pady=10)

player_button = tk.Button(root, text="Player", width=15, command=on_player)
player_button.pack(pady=5)
manager_button = tk.Button(root, text="Manager", width=15, command=on_manager)
manager_button.pack(pady=5)


root.mainloop()