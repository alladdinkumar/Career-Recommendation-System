from tkinter import *
import sqlite3
def fuzzy_calculator():
    inputs=[90,28,90,27]
    import numpy as np
    import skfuzzy as fuzz
    from skfuzzy import control as ctrl

    theory= ctrl.Antecedent(np.arange(0,101,1),'theory')
    practical=ctrl.Antecedent(np.arange(0,31,1,),'practical')
    attendance= ctrl.Antecedent(np.arange(0,101,1),'attendance')
    project= ctrl.Antecedent(np.arange(0,31,1),'project')
    grade=ctrl.Consequent(np.arange(0,101,1),'grade')



    practical['l']=fuzz.trimf(practical.universe,[0,10,15])
    practical['m']=fuzz.trimf(practical.universe,[10,15,20])
    practical['h']=fuzz.trimf(practical.universe,[15,20,30])

    theory['l']=fuzz.trimf(theory.universe,[0,40,60])
    theory['m']=fuzz.trimf(theory.universe,[40,60,80])
    theory['h']=fuzz.trimf(theory.universe,[60,80,100])

    attendance['l']=fuzz.trimf(attendance.universe,[0,40,60])
    attendance['m']=fuzz.trimf(attendance.universe,[40,60,80])
    attendance['h']=fuzz.trimf(attendance.universe,[60,80,100])

    project['l']=fuzz.trimf(project.universe,[0,10,15])
    project['m']=fuzz.trimf(project.universe,[10,15,20])
    project['h']=fuzz.trimf(project.universe,[15,20,30])

    grade['l']=fuzz.trimf(grade.universe,[0,40,60])
    grade['m']=fuzz.trimf(grade.universe,[40,60,80])
    grade['h']=fuzz.trimf(grade.universe,[60,80,100])

    practical.view()
    theory.view()
    project.view()


    rule1 = ctrl.Rule( theory['l'] & practical['l'] & attendance['l'] & project['l'] , grade['l'])
    rule2 = ctrl.Rule( theory['l'] & practical['l'] & attendance['l'] & project['m'] , grade['l'])
    rule3 = ctrl.Rule( theory['l'] & practical['l'] & attendance['l'] & project['h'] , grade['l'])
    rule4 = ctrl.Rule( theory['l'] & practical['l'] & attendance['m'] & project['l'] , grade['l'])
    rule5 = ctrl.Rule( theory['l'] & practical['l'] & attendance['m'] & project['m'] , grade['l'])
    rule6 = ctrl.Rule( theory['l'] & practical['l'] & attendance['m'] & project['h'] , grade['m'])
    rule7 = ctrl.Rule( theory['l'] & practical['l'] & attendance['h'] & project['l'] , grade['l'])
    rule8 = ctrl.Rule( theory['l'] & practical['l'] & attendance['h'] & project['m'] , grade['m'])
    rule9 = ctrl.Rule( theory['l'] & practical['l'] & attendance['h'] & project['h'] , grade['m'])
    rule10= ctrl.Rule( theory['l'] & practical['m'] & attendance['l'] & project['l'] , grade['l'])
    rule11= ctrl.Rule( theory['l'] & practical['m'] & attendance['l'] & project['m'] , grade['l'])
    rule12= ctrl.Rule( theory['l'] & practical['m'] & attendance['l'] & project['h'] , grade['l'])
    rule13= ctrl.Rule( theory['l'] & practical['m'] & attendance['m'] & project['l'] , grade['l'])
    rule14= ctrl.Rule( theory['l'] & practical['m'] & attendance['m'] & project['m'] , grade['l'])
    rule15= ctrl.Rule( theory['l'] & practical['m'] & attendance['m'] & project['h'] , grade['l'])
    rule16= ctrl.Rule( theory['l'] & practical['m'] & attendance['h'] & project['l'] , grade['l'])
    rule17= ctrl.Rule( theory['l'] & practical['m'] & attendance['h'] & project['m'] , grade['m'])
    rule18= ctrl.Rule( theory['l'] & practical['m'] & attendance['h'] & project['h'] , grade['m'])
    rule19= ctrl.Rule( theory['l'] & practical['h'] & attendance['l'] & project['l'] , grade['l'])
    rule20= ctrl.Rule( theory['l'] & practical['h'] & attendance['l'] & project['m'] , grade['l'])
    rule21= ctrl.Rule( theory['l'] & practical['h'] & attendance['l'] & project['h'] , grade['l'])
    rule22= ctrl.Rule( theory['l'] & practical['h'] & attendance['m'] & project['l'] , grade['l'])
    rule23= ctrl.Rule( theory['l'] & practical['h'] & attendance['m'] & project['m'] , grade['l'])
    rule24= ctrl.Rule( theory['l'] & practical['h'] & attendance['m'] & project['h'] , grade['m'])
    rule25= ctrl.Rule( theory['l'] & practical['h'] & attendance['h'] & project['l'] , grade['l'])
    rule26= ctrl.Rule( theory['l'] & practical['h'] & attendance['h'] & project['m'] , grade['m'])
    rule27= ctrl.Rule( theory['l'] & practical['h'] & attendance['h'] & project['h'] , grade['m'])

    rule28= ctrl.Rule( theory['m'] & practical['l'] & attendance['l'] & project['l'] , grade['l'])
    rule29= ctrl.Rule( theory['m'] & practical['l'] & attendance['l'] & project['m'] , grade['l'])
    rule30= ctrl.Rule( theory['m'] & practical['l'] & attendance['l'] & project['h'] , grade['m'])
    rule31= ctrl.Rule( theory['m'] & practical['l'] & attendance['m'] & project['l'] , grade['l'])
    rule32= ctrl.Rule( theory['m'] & practical['l'] & attendance['m'] & project['m'] , grade['m'])
    rule33= ctrl.Rule( theory['m'] & practical['l'] & attendance['m'] & project['h'] , grade['m'])
    rule34= ctrl.Rule( theory['m'] & practical['l'] & attendance['h'] & project['l'] , grade['l'])
    rule35= ctrl.Rule( theory['m'] & practical['l'] & attendance['h'] & project['m'] , grade['l'])
    rule36= ctrl.Rule( theory['m'] & practical['l'] & attendance['h'] & project['h'] , grade['m'])
    rule37= ctrl.Rule( theory['m'] & practical['m'] & attendance['l'] & project['l'] , grade['l'])
    rule38= ctrl.Rule( theory['m'] & practical['m'] & attendance['l'] & project['m'] , grade['l'])
    rule39= ctrl.Rule( theory['m'] & practical['m'] & attendance['l'] & project['h'] , grade['m'])
    rule40= ctrl.Rule( theory['m'] & practical['m'] & attendance['m'] & project['l'] , grade['m'])
    rule41= ctrl.Rule( theory['m'] & practical['m'] & attendance['m'] & project['m'] , grade['m'])
    rule42= ctrl.Rule( theory['m'] & practical['m'] & attendance['m'] & project['h'] , grade['m'])
    rule43= ctrl.Rule( theory['m'] & practical['m'] & attendance['h'] & project['l'] , grade['m'])
    rule44= ctrl.Rule( theory['m'] & practical['m'] & attendance['h'] & project['m'] , grade['m'])
    rule45= ctrl.Rule( theory['m'] & practical['m'] & attendance['h'] & project['h'] , grade['h'])
    rule46= ctrl.Rule( theory['m'] & practical['h'] & attendance['l'] & project['l'] , grade['l'])
    rule47= ctrl.Rule( theory['m'] & practical['h'] & attendance['l'] & project['m'] , grade['m'])
    rule48= ctrl.Rule( theory['m'] & practical['h'] & attendance['l'] & project['h'] , grade['m'])
    rule49= ctrl.Rule( theory['m'] & practical['h'] & attendance['m'] & project['l'] , grade['m'])
    rule50= ctrl.Rule( theory['m'] & practical['h'] & attendance['m'] & project['m'] , grade['m'])
    rule51= ctrl.Rule( theory['m'] & practical['h'] & attendance['m'] & project['h'] , grade['m'])
    rule52= ctrl.Rule( theory['m'] & practical['h'] & attendance['h'] & project['l'] , grade['m'])
    rule53= ctrl.Rule( theory['m'] & practical['h'] & attendance['h'] & project['m'] , grade['h'])
    rule54= ctrl.Rule( theory['m'] & practical['h'] & attendance['h'] & project['h'] , grade['h'])

    rule55= ctrl.Rule( theory['h'] & practical['l'] & attendance['l'] & project['l'] , grade['l'])
    rule56= ctrl.Rule( theory['h'] & practical['l'] & attendance['l'] & project['m'] , grade['l'])
    rule57= ctrl.Rule( theory['h'] & practical['l'] & attendance['l'] & project['h'] , grade['l'])
    rule58= ctrl.Rule( theory['h'] & practical['l'] & attendance['m'] & project['l'] , grade['l'])
    rule59= ctrl.Rule( theory['h'] & practical['l'] & attendance['m'] & project['m'] , grade['m'])
    rule60= ctrl.Rule( theory['h'] & practical['l'] & attendance['m'] & project['h'] , grade['m'])
    rule61= ctrl.Rule( theory['h'] & practical['l'] & attendance['h'] & project['l'] , grade['l'])
    rule62= ctrl.Rule( theory['h'] & practical['l'] & attendance['h'] & project['m'] , grade['m'])
    rule63= ctrl.Rule( theory['h'] & practical['l'] & attendance['h'] & project['h'] , grade['m'])
    rule64= ctrl.Rule( theory['h'] & practical['m'] & attendance['l'] & project['l'] , grade['l'])
    rule65= ctrl.Rule( theory['h'] & practical['m'] & attendance['l'] & project['m'] , grade['m'])
    rule66= ctrl.Rule( theory['h'] & practical['m'] & attendance['l'] & project['h'] , grade['m'])
    rule67= ctrl.Rule( theory['h'] & practical['m'] & attendance['m'] & project['l'] , grade['m'])
    rule68= ctrl.Rule( theory['h'] & practical['m'] & attendance['m'] & project['m'] , grade['m'])
    rule69= ctrl.Rule( theory['h'] & practical['m'] & attendance['m'] & project['h'] , grade['h'])
    rule70= ctrl.Rule( theory['h'] & practical['m'] & attendance['h'] & project['l'] , grade['m'])
    rule71= ctrl.Rule( theory['h'] & practical['m'] & attendance['h'] & project['m'] , grade['m'])
    rule72= ctrl.Rule( theory['h'] & practical['m'] & attendance['h'] & project['h'] , grade['h'])
    rule73= ctrl.Rule( theory['h'] & practical['h'] & attendance['l'] & project['l'] , grade['m'])
    rule74= ctrl.Rule( theory['h'] & practical['h'] & attendance['l'] & project['m'] , grade['m'])
    rule75= ctrl.Rule( theory['h'] & practical['h'] & attendance['l'] & project['h'] , grade['h'])
    rule76= ctrl.Rule( theory['h'] & practical['h'] & attendance['m'] & project['l'] , grade['m'])
    rule77= ctrl.Rule( theory['h'] & practical['h'] & attendance['m'] & project['m'] , grade['m'])
    rule78= ctrl.Rule( theory['h'] & practical['h'] & attendance['m'] & project['h'] , grade['h'])
    rule79= ctrl.Rule( theory['h'] & practical['h'] & attendance['h'] & project['l'] , grade['h'])
    rule80= ctrl.Rule( theory['h'] & practical['h'] & attendance['h'] & project['m'] , grade['h'])
    rule81= ctrl.Rule( theory['h'] & practical['h'] & attendance['h'] & project['h'] , grade['h'])



    wm_ctrl= ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,rule32,rule33,rule34,rule35,rule36,rule37
                                ,rule38,rule39,rule40,rule41,rule42,rule43,rule44,rule45,rule46,rule47,rule48,rule49,rule50,rule51,rule52,rule53,rule54,rule55,rule56,rule57,rule58,rule59,rule60,rule61,rule62,rule63,rule64,rule65,rule66,rule67,rule68,rule69,rule70,rule71,rule72,rule73,rule74
                                ,rule75,rule76,rule77,rule78,rule79,rule80,rule81])
    wm= ctrl.ControlSystemSimulation(wm_ctrl)

    wm.input['theory']=inputs[0]
    wm.input['practical']=inputs[1]
    wm.input['attendance']=inputs[3]
    wm.input['project']=inputs[4]

    wm.compute()
    out=wm.output['grade']
    print(out)
    grade.view(sim=wm)




def Home():
    global top,window
    if window==1:
        top.withdraw()
    window=1
    top=Toplevel()
    top.geometry("1400x743+0+0")
    top.title("Home Page")
    image1 =PhotoImage(file="students.png")
    
    Form = Label(top, image=image1)
    Form.pack(side='top', fill='both', expand='yes')
    btn_login = Button(Form, text="Sign IN", width=25, command=login_window)
    btn_login.place(x=900, y=40)
    btn_login.bind('<Return>',login_window )
    top.mainloop()
    
    
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
Home()
   

