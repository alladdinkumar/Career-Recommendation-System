from tkinter import *
import sqlite3
root = Tk()
root.title("HOMEPAGE")
root.geometry("1400x700+0+0")

Top = Frame(root, bd=2)
Top.pack(side=TOP)
image1 =PhotoImage(file="login.png")
Form  = Label(root, image=image1)
Form.pack(side='top', fill='both', expand='yes')
USERNAME = StringVar()
PASSWORD = StringVar()
img =PhotoImage(file="login2.png")

lbl_username = Label(Form, text = "Username:", font=(14), bd=10)
lbl_username.place(x=50,y=450)
lbl_password = Label(Form, text = "Password:", font=(14), bd=10)
lbl_password.place(x=50,y=530 )
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)
 
username = Entry(Form, textvariable=USERNAME, font=(14))
username.place(x=170, y=460)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.place(x=170, y=540)

flag=0
def Database():
    global conn, cursor,flag
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("CREATE TABLE member (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        cursor.execute("INSERT INTO member (username, password) VALUES('admin', 'admin')")
    except:
        cursor.execute("SELECT * FROM member WHERE username = ? AND password = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            flag=1
    conn.commit()

    
    
def Login():
        
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        if flag==1:
            lbl_home = Label(root, text="Successfully Login!", font=(20)).pack()
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()
def Signup():
    print("Signup")
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.place(x=50, y=600)
btn_login.bind('<Return>', Login)
btn_signup = Button(Form, text="New User Sign Up", width=25, command=Signup)
btn_signup.place(x=950, y=20)
btn_signup.bind('<Return>', Signup)
Form.wm_attributes('-transparentcolor')
if __name__ == '__main__':
    root.mainloop()

def HomeWindow():
    global Home
    root.withdraw()
    Fill_details()
def Fill_details():
    print("end")
    

