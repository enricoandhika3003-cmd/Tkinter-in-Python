from tkinter import *
window = Tk()

window.title("Tkinter")
window.geometry("500x600")

greeting = Label(text = "Hello, World!", fg="black", bg="white", height=5, width=20)
submit = Button(text = "Submit", fg="black", bg="lime", height=5, width=30, bd=3) #command = submit
entry = Entry(fg="black", bg="gray", width=50)
greeting.pack()
submit.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=3) 
frame.pack()

label = Label(master=frame, text="Frame")
label.pack()

textbox = Text(fg="white", bg="black")
textbox.pack()

window.mainloop()