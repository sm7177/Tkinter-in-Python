# from tkinter import *

# window=Tk()
# window.title("New File")
# window.geometry("300x300")

# greetings=Label(text="Hello,Welcome",fg="blue",bg="yellow")

# button=Button(text="Click me", bg="yellow",fg="white", width=50, bd=3)

# enter=Entry(fg="blue",bg="yellow")

# frame=Frame(master=window, relief=RAISED, borderwidth=5)

# label=Label(master=frame, text="example")

# text=Text(fg="blue",bg="yellow")



# greetings.pack()
# button.pack()
# enter.pack()
# frame.pack()
# label.pack()
# text.pack()



# window.mainloop()














import tkinter as tk
window=tk.Tk()

for i in range(3):
    for j in range(3):
        frame=tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=5, pady=5)
        lable=tk.Label(master=frame, text=f"row{i}\n column{j}")
        lable.pack()
window.mainloop()