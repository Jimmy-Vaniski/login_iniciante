from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

# Colors
c1 = "#f0f3f5"  # Black
c2 = "#feffff"  # White
c3 = "#3fb5a3"  # Green
c4 = "#32576b"
c5 = "#403d3d"

# Creating window
window = Tk()
window.title("Login")
window.geometry("310x300")
window.configure(background=c2)
window.resizable(width=FALSE, height=FALSE)

# Slicing window
frame1 = Frame(window, width=310, height=50, bg=c2, relief=FLAT)
frame1.grid(row=0, column=0, padx=1, pady=0, sticky=NSEW)

frame2 = Frame(window, width=310, height=250, bg=c2, relief=FLAT)
frame2.grid(row=1, column=0, padx=1, pady=0, sticky=NSEW)

# configuring frame1
label_f1 = Label(frame1, text="LOGIN", anchor=NE, font="Ivy 25", bg=c2, fg=c5)
label_f1.place(x=5, y=5)

label_line_f1 = Label(frame1, text="", width=275, anchor=NW, font="Ivy 1", bg=c3, fg=c5)
label_line_f1.place(x=10, y=45)


# function get and compare credentials
def compare_user():
    name = entry_name.get()
    password = entry_password.get()

    if name == 'admin' and password == 'admin':
        messagebox.showinfo("Login", "Verified !")
    elif credentials[0] == name and credentials[1] == password:
        messagebox.showinfo("Login", "Wellcome back " + name + "!!")
        # Delete items in every frame
        for widget in frame1.winfo_children():
            widget.destroy()
        for widget in frame2.winfo_children():
            widget.destroy()

        new_window()
    else:
        messagebox.showinfo("Error", "Access denied, please try again.")


# function after verified.
def new_window():
    # configuring frame1
    label_f1 = Label(frame1, text="User: " + credentials[0], anchor=NE, font="Ivy 20", bg=c2, fg=c5)
    label_f1.place(x=5, y=5)

    label_line_f1 = Label(frame1, text="", width=275, anchor=NW, font="Ivy 1", bg=c3, fg=c5)
    label_line_f1.place(x=10, y=45)

    label_f1 = Label(frame2, text="Wellcome" + credentials[0], anchor=NE, font="Ivy 20", bg=c2, fg=c5)
    label_f1.place(x=5, y=105)


# configuring frame2
label_f2_name = Label(frame2, text="Name*", anchor=NW, font="Ivy 10", bg=c2, fg=c5)
label_f2_name.place(x=10, y=20)

entry_name = Entry(frame2, text="", width=25, justify="left", font="Ivy 15", highlightthickness=1, relief="solid")
entry_name.place(x=14, y=50)

label_f2_password = Label(frame2, text="Password*", anchor=NW, font="Ivy 10", bg=c2, fg=c5)
label_f2_password.place(x=10, y=95)

entry_password = Entry(frame2, text="", width=25, justify="left", show='*', font=" 15", highlightthickness=1,
                       relief="solid")
entry_password.place(x=14, y=130)

button = Button(frame2, command=compare_user, text="Entrar", width=34, height=2, font="Ivy 10 bold", relief=RAISED,
                overrelief=RIDGE, bg=c3,
                fg=c2)
button.place(x=15, y=180)

credentials = ["jimmy", "123"]

window.mainloop()
