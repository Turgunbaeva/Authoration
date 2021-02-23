from tkinter import *
from tkinter import messagebox
import  pickle

root = Tk()
root.geometry('500x500')
root.title('Enter to system')

def registration():
    text = Label(text="Для входа в систему зарегистрируйтесь")
    text_log = Label(text="Enter your login")
    register_login = Entry()
    text_password1 = Label(text="Enter your password")
    register_password1 = Entry(show='*')
    text_password2 = Label(text='Enter again your password')
    register_password2 = Entry(show="*")
    button_register = Button(text='Register', command=lambda: save())
    text.pack()
    text_log.pack()
    register_login.pack()
    text_password1.pack()
    register_password1.pack()
    text_password2.pack()
    register_password2.pack()
    button_register.pack()

    def save():
        login_pass_save = {}
        login_pass_save[register_login.get()] = register_password1.get()
        f = open('login.txt', "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()


def login():
    text_log = Label(text='Congrats! Now you can enter to the system!')
    text_enter_login = Label(text='Enter your login')
    enter_login =Entry()
    text_enter_password = Label(text='Enter your password')
    enter_password = Entry(show='*')
    button_enter = Button(text='Login', command=lambda: log_pass())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_password.pack()
    enter_password.pack()
    button_enter.pack()

    def log_pass():
        f = open('login.txt', 'rb')
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() == a[enter_login.get()]:
                messagebox.showinfo('You enter successfully!', 'Hello! You have 5 new messages')
            else:
                messagebox.showerror('Error!', 'You enter incorrect login or password! ')
        else:
            messagebox.showerror('Error!', 'Incorrect login!')



registration()
root.mainloop()
