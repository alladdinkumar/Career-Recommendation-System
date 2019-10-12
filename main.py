from tkinter import *
import sqlite3
def show_colleges():
    global top,window
    
    if window==1:
        top.withdraw()
    top=Toplevel()
    top.geometry("1400x700+0+0")
    top.title("Colleges")
   
    top.mainloop()
    
def path_selection():
    global top,window
    
    if window==1:
        top.withdraw()
    top=Toplevel()
    top.geometry("1400x700+0+0")
    top.title("Pathway Selection")
    image1 =PhotoImage(file="path.png")
    
    Form = Label(top, image=image1)
    Form.pack(side='top', fill='both', expand='yes')
    
    OptionList=["Animation/Graphics","Business",
                              "Computer/IT",
                              "Engineering and Architecture",
                              "Media/Communication",
                             "Art/Design",
                              "Banking",
                              "Law School",
                              "Education and Teaching",
                              "Medical"]
    variable = StringVar(top)
    variable.set(OptionList[0])

    opt = OptionMenu(top, variable, *OptionList)
    opt.config(width=20, font=('Helvetica', 12))
    opt.place(x=920,y=320)


    labelTest = Label(text="", font=('Helvetica', 12), fg='white')
    labelTest.place(x=920,y=320)

    def callback(*args):
        labelTest.configure(text="The selected item is {}".format(variable.get()))

    variable.trace("w", callback)

    
   
    btn_go = Button(Form, text="GO", width=25, command=show_colleges)
    btn_go.place(x=950, y=400)
    btn_go.bind('<Return>',show_colleges )
    top.mainloop()
    
def HomeWindow():
    print("end")
    if window==1:
        top.withdraw()
    
    Fill_details()
def Signup_window():
    global top,window
    
    if window==1:
        top.withdraw()
    window=1
    
    global flag,USERNAME,PASSWORD,lbl_text 
    
    top=Toplevel()
    top.geometry("1400x700+0+0")
    top.title("SIGNUP")
    image1 =PhotoImage(file="Signup.png")
    
    Form1 = Label(top, image=image1)
    Form1.pack(side='top', fill='both', expand='yes')
    
    USERNAME = StringVar()
    PASSWORD = StringVar()
   

    lbl_username = Label(Form1, text = "Email ID:", font=(14), bd=10)
    lbl_username.place(x=450,y=350)
    lbl_password = Label(Form1, text = "Password:", font=(14), bd=10)
    lbl_password.place(x=450,y=430 )
    lbl_text = Label(Form1)
    lbl_text.grid(row=2, columnspan=2)

    
   
    username = Entry(Form1, textvariable=USERNAME, font=(14))
    username.place(x=570, y=360)
    password = Entry(Form1, textvariable=PASSWORD, show="*", font=(14))
    password.place(x=570, y=440)
    
    btn_Signup = Button(Form1, text="Sign Up", width=45, command=Signup)
    btn_Signup.place(x=450, y=500)
    btn_Signup.bind('<Return>', Signup)
    btn_login = Button(Form1, text="Sign IN", width=25, command=login_window)
    btn_login.place(x=900, y=40)
    btn_login.bind('<Return>',login_window )
    top.mainloop()
def Signup():
        
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        Database_Signup()
        lbl_home = Label(root, text="Successfully Registered!", font=(20)).pack()
        login_window()
    USERNAME.set("")
    PASSWORD.set("")
    #lbl_text.config(text="")
       
    
def Database_Signup():
    global conn, cursor,flag,USERNAME,PASSWORD
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("CREATE TABLE member (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        
    except:
        cursor.execute("INSERT INTO member (username, password) VALUES(?,?)",(USERNAME.get(), PASSWORD.get()))
        
    conn.commit()
    cursor.close()
    conn.close()

    
def Fill_details():
    print("Inputs ")
    path_selection()
    
def login_window():
    global top,window
    if window==1:
        top.withdraw()
    window=1
    global flag,USERNAME,PASSWORD,lbl_text
    top=Toplevel()
    top.geometry("1400x700+0+0")
    top.title("Login")
    image1 =PhotoImage(file="login.png")
    
    Form = Label(top, image=image1)
    Form.pack(side='top', fill='both', expand='yes')
    USERNAME = StringVar()
    PASSWORD = StringVar()
    

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
    btn_login = Button(Form, text="Login", width=45, command=Login)
    btn_login.place(x=50, y=600)
    btn_login.bind('<Return>', Login)
    btn_signup = Button(Form, text="New User Sign Up", width=25, command=Signup_window)
    btn_signup.place(x=950, y=20)
    btn_signup.bind('<Return>', Signup_window)
    top.mainloop()

    
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
    cursor.close()
    conn.close()

    
    
def Login():
        
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        if flag==1:
            lbl_home = Label(root, text="Successfully Login!", font=(20)).pack()
            HomeWindow()
            
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    USERNAME.set("")
    PASSWORD.set("")
    #lbl_text.config(text="")
    



root=Tk()
root.withdraw()
global window
window=0
login_window()    

