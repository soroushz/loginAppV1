# Login App
import tkinter as tk
from tkinter import messagebox

def loginFunc():
    logUsername = usernamelogEntry.get()
    logPass = passLogEntry.get()

    if logUsername == "admin" and logPass == "1234":
        messagebox.showinfo("Login", "Login information correct")
    else:
        messagebox.showerror("Login Failed", "Incorrect Information")

def regFunc():
    regUsername = usernameRegEntry.get()
    regPass = passRegEntry.get()
    regPassConf = passRegEntryConf.get()

    if regPass == regPassConf:
        messagebox.showinfo("Registration Successful", "You have been registered")
    else:
        messagebox.showerror("Registration Failed", "Passwords do not match!")

root = tk.Tk()

root.title("Login & Registration")

loginFrame = tk.Frame(root)
regFrame = tk.Frame(root)

loginFrame.pack(padx=92, pady=10)
regFrame.pack(padx=92, pady=10)

usernameLogLbl = tk.Label(loginFrame, text="Username")
usernameLogLbl.pack(pady=5)

usernamelogEntry = tk.Entry(loginFrame)
usernamelogEntry.pack(pady=5)

passLogLbl = tk.Label(loginFrame, text="Password")
passLogLbl.pack(pady=5)

passLogEntry = tk.Entry(loginFrame, show="*")
passLogEntry.pack(pady=5)

loginBtn = tk.Button(loginFrame, text="Login", command=loginFunc)
loginBtn.pack(pady=5)

usernameRegLbl = tk.Label(regFrame, text="Username")
usernameRegLbl.pack(pady=5)

usernameRegEntry = tk.Entry(regFrame)
usernameRegEntry.pack(pady=5)

passRegLbl = tk.Label(regFrame, text="Password")
passRegLbl.pack(pady=5)

passRegEntry = tk.Entry(regFrame, show="+")
passRegEntry.pack(pady=5)

passRegLblConf = tk.Label(regFrame, text="Password Re-type")
passRegLblConf.pack(pady=5)

passRegEntryConf = tk.Entry(regFrame, show="+")
passRegEntryConf.pack(pady=5)

regBtn = tk.Button(regFrame, text="Sing Up", command=regFunc)
regBtn.pack(pady=5)



root.mainloop()