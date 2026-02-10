import tkinter as tk
window = tk.Tk()

for i in range(2):
    for j in range(6):
        frame = tk.Frame(
            master = window,
            relief = tk.RAISED,
            bd = 5)
        frame.grid(row = i, column = j, padx = 5, pady = 5)
        label = tk.Label(master=frame, text="◼️")
        label.pack()

window.mainloop()