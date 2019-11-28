#importing required libraries
from tkinter import *
import sqlite3
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pandas as pd
global variable,lb,window,recommendation


#==================================================


from tkcalendar import Calendar
from tkinter import ttk
import datetime

#declaring the variables used as global
global listStr,listS1,listS2,listS3,listS4,listS5
global second, sub1T ,sub1Tv,sub1Prc,sub1A,sub1P
global sub2T,sub2Prc,sub2P,sub2A
global sub3T,sub3Prc,sub3P,sub3A
global sub4T,sub4Prc,sub4P,sub4A
global sub5T,sub5Prc,sub5P,sub5A
global sub1Tv, sub1Prcv, sub1Av, sub1Pv, sub1
global sub2Tv, sub2Prcv, sub2Av, sub2Pv, sub2
global sub3Tv, sub3Prcv, sub3Av, sub3Pv, sub3 
global sub4Tv, sub4Prcv, sub4Av, sub4Pv, sub4
global sub5Tv, sub5Prcv, sub5Av, sub5Pv, sub5
global streamVal
nameVal, boardVal , genVal, dobVal,dobVal="","", "", "",""
first, second, lb= None, None, None
lightBG, darkBG = "#eafde7", "#44484b"
splash = None
nik=None
name, board, gender,dob , info,stream= None, None , None, None, None, None

#===============================================
from tkinter import messagebox
global v6,v5,v4,v3,v2,v1

def Home():
    global top,window
    if window==1:
        top.withdraw()
    window=1
    top=Toplevel()
    #top.geometry("1400x743+0+0")
    top.title("Home Page")
    image1 =PhotoImage(file="students.png")
    top.wm_attributes('-fullscreen', 'true')
    Form = Label(top, image=image1)
    Form.pack(side='top', fill='both', expand='yes')
    close = PhotoImage(master=top, file="close.png")
    Button(top, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=top.destroy).place(x=1320,y=10)
    sign_in = PhotoImage(file="sign_in.png")
    btn_sign = Button(Form, text="Sign IN",image=sign_in, command=login_window)
    btn_sign.place(x=1200, y=10)
    btn_sign.bind('<Return>',login_window )
    top.mainloop()

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
    top.wm_attributes('-fullscreen', 'true')
    Form1 = Label(top, image=image1)
    Form1.pack(side='top', fill='both', expand='yes')
    close = PhotoImage(master=top, file="close.png")
    Button(top, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=top.destroy).place(x=1320,y=10)
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
    
    sign_up = PhotoImage(file="signup_button.png")
    btn_Signup = Button(Form1, text="Sign Up", image=sign_up, command=Signup)
    btn_Signup.place(x=450, y=500)
    btn_Signup.bind('<Return>', Signup)
    sign_in = PhotoImage(file="sign_in.png")
    btn_sign = Button(Form1, text="Sign IN",image=sign_in, command=login_window)
    btn_sign.place(x=1200, y=10)
    btn_sign.bind('<Return>',login_window )
    top.mainloop()
def Signup():
        
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
        USERNAME.set("")
        PASSWORD.set("")
    else:
        Database_Signup()
        lbl_home = Label(root, text="Successfully Registered!", font=(20)).pack()
        login_window()
    
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
    top.wm_attributes('-fullscreen', 'true')
    Form = Label(top, image=image1)
    Form.pack(side='top', fill='both', expand='yes')
    close = PhotoImage(master=top, file="close.png")
    Button(top, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=top.destroy).place(x=1320,y=10)
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
    login_button = PhotoImage(file="login_button.png")
    btn_login = Button(Form, text="Login", image=login_button, command=Login)
    btn_login.place(x=50, y=600)
    btn_login.bind('<Return>', Login)
    register_button = PhotoImage(file="register_button.png")
    btn_signup = Button(Form,image=register_button, command=Signup_window)
    btn_signup.place(x=1200, y=10)
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
        USERNAME.set("")
        PASSWORD.set("")
    else:
        Database()
        if flag==1:
            lbl_home = Label(top, text="Successfully Login!", font=(20)).pack()
            HomeWindow()
            
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    
    #lbl_text.config(text="")

def HomeWindow():
    print("end")
    if window==1:
        top.withdraw()
    
    Fill_details()


def Fill_details():
    #letsGO
    #updated validation for subjects
    global lb
    def Splash():
        #firstWINDOW
        global splash
        splash = Toplevel()
        splash.wm_attributes("-fullscreen","true")
        bg = PhotoImage(file="yu.png")
        Label(splash, image=bg).place(relwidth=1, relheight=1)
        close = PhotoImage(file="close.png")
        Button(splash, bd=0, image=close, bg="#eafde7", activebackground="#eafde7",command=splash.destroy).place(x=1320, y=10)
        start_img = PhotoImage(file="start.png")
        
        Button(splash, bd=0, image=start_img, bg="#44484b", activebackground="#44484b",command=loadUI).place(x=970, y=560)

        splash.mainloop()
        return

    def loadUI():
        splash.destroy()
        firstUI()
        return

    def firstUI():
        #secondWINDOW
        #filling_details
        global fin, board, stream, name, info, first, gender,dob
        global sub1Tv, sub1Prcv, sub1Av, sub1Pv, sub1T
        global listStr,listS1,listS2,listS3
        global dobVal
        global window
        window=1
        first = Toplevel()
        first.title("Home Page")
        first.wm_attributes('-fullscreen', 'true')
        bg = PhotoImage(master=first,file="bg.png")
        Label(first, image=bg).place(relwidth=1, relheight=1)
        close = PhotoImage(master=first, file="close.png")
        Button(first, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=first.destroy).place(x=1320,y=10)
        Label(first,text="Enter Your Details", font=("Courier",30,"bold underline"),bg=lightBG, fg="#27292b").place(x=490,y=130)
        Label(first, text="Name*: ", fg="#27292b",font=("Arial Black",12), bg=lightBG).place(x=520, y=260)
        #gender
        Label(first, text="Gender*: ",fg="#27292b" , font=("Arial Black",12), bg=lightBG). place(x=520, y=290)
        
        Label(first, text="12th Board*: ", fg="#27292b",font=("Arial Black",12), bg=lightBG).place(x=520, y=320)
        
        Label(first, text="DOB*: ",fg="#27292b" ,font=("Arial Black",12), bg=lightBG).place(x=520,y=350)
        
        Label(first, text="Stream*: ",fg="#27292b" ,font=("Arial Black",12), bg=lightBG). place(x=520, y=390)
        name = Entry(first, font=("Arial",12))
        board = IntVar()
        
        Radiobutton(first, text="CBSE",font=("Arial",12), bg=lightBG , variable=board, value=1).place(x=720, y=320)
        Radiobutton(first, text="SSC",font=("Arial",12), bg=lightBG, variable=board, value=2).place(x=820, y=320)
        Radiobutton(first, text="OTHERS",font=("Arial",12), bg=lightBG, variable=board, value=3).place(x=920, y=320)
        
        gender=IntVar()   
        level = IntVar()
        stream= IntVar()
        
        name.place(x=720, y=260)
        #calendar_CODE
        def example1():
            def print_sel():
                cal.destroy()
                global dobVal
                dobVal=cal.selection_get()
                print(dobVal)
                fin.config(text="YYYY/MM/DD : "+str(dobVal))
                
            
            mindate = datetime.date(year=1999, month=1, day=20)
            maxdate = datetime.date(year=2003, month=1, day=20)
            cal = Calendar(first, font="Arial 14", selectmode='day', locale='en_US',
            mindate=mindate, maxdate=maxdate, disabledforeground='red')
            
            cal.place(x=720,y=360)
            ttk.Button(first, text="save", command=print_sel).place(x=1100,y=350)

        
        ttk.Button(first, text='-select-', command=example1).place(x=720,y=350)    
        Radiobutton(first, text="Male",font=("Arial",12), bg=lightBG , variable=gender, value=1).place(x=720, y=290)
        Radiobutton(first, text="Female",font=("Arial",12), bg=lightBG , variable=gender, value=2).place(x=820, y=290)
        Radiobutton(first, text="Science",font=("Arial",12), bg=lightBG , variable=stream, value=1).place(x=720, y=390)
        Radiobutton(first, text="Humanities/Arts",font=("Arial",12), bg=lightBG, variable=stream, value=2).place(x=720, y=420)
        Radiobutton(first, text="Commerce",font=("Arial",12), bg=lightBG, variable=stream, value=3).place(x=720, y=450)
        #ERROR_messages_FONT & COLOUR
        start_img = PhotoImage(file="continue.png")
        Button(first, text="Click Here", relief=RIDGE, image=start_img, bg=darkBG, activebackground=darkBG, bd=0, command=startQuiz).place(x=640, y=590)
        info = Label(first, text="", font=("Helvetica",10), bg=lightBG, fg="red")
        info.place(x=620, y=475)
        
        fin=Label(first,text="",font=("Helvetica",12),bg=lightBG,fg="black")
        fin.place(x=800,y=350)
        
        first.mainloop()
        return

    def startQuiz():
        #DO VALIDATION for each INPUT recieved
        global nameVal, regVal, boardVal, dobVal, genVal, difLevel, streamVal,year,checkVal
        global sub1Tv,nik,sub1Prcv,sub1Av,sub1Pv
        nameVal = str(name.get()).title()
        boardVal= board.get()
        streamVal=stream.get()
        genVal = gender.get()
        
        if len(nameVal) == 0:
            info.config(text="*Please Enter Valid Name")
            return
        elif gender.get() not in range(1,3):
            info.config(text="*Please Select gender to proceed")
            return
        
        elif board.get() not in range(1,4):
            info.config(text="*Please Select valid BOARD to proceed")
            return
        elif stream.get() not in range(1,4):
            info.config(text="*Please Select valid STREAM to proceed")
            return      
        else:
            
            global first
            first.destroy()
            secondIN()
            
                                    
    def secondIN():
        #entering MARKS of diff_SUBJECTS
        global listStr,listS1,listS2,listS3,listS4,listS5
        global name, board,stream,info, first, gender,dobf,fin,check,nik
        global second, sub1T ,sub1Tv,sub1Prc,sub1A,sub1P
        global sub2T,sub2Prc,sub2P,sub2A
        global sub3T,sub3Prc,sub3P,sub3A
        global sub4T,sub4Prc,sub4P,sub4A
        global sub5T,sub5Prc,sub5P,sub5A
        global sub1Tv, sub1Prcv, sub1Av, sub1Pv, sub1
        global sub2Tv, sub2Prcv, sub2Av, sub2Pv, sub2
        global sub3Tv, sub3Prcv, sub3Av, sub3Pv, sub3 
        global sub4Tv, sub4Prcv, sub4Av, sub4Pv, sub4
        global sub5Tv, sub5Prcv, sub5Av, sub5Pv, sub5
        second = Toplevel()
        second.title(" Quizi")
        second.wm_attributes('-fullscreen', 'true')
        bg = PhotoImage(master=second,file="bg.png")
        Label(second, image=bg).place(relwidth=1, relheight=1)
        close = PhotoImage(master=second, file="close.png")
        Button(second, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=second.destroy).place(x=1320,y=10)

        Label(second,text="Enter Your Academic Details", font=("Courier",30,"bold underline"),bg=lightBG, fg="#27292b").place(x=350,y=25)

        
        
        Label(second, text="Subject", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=480, y=100)   
        Label(second, text="Theory(70)", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=660, y=100)
        Label(second, text="Practical(30)", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=810, y=100)
        Label(second, text="Attend.(100)", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=985,y=100)
        Label(second, text="Project(30)", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=1150, y=100)

        if(streamVal==1):
            Label(second, text="Physics",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=140)
        elif(streamVal==2):
            Label(second, text="History",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=140)
        else:
            Label(second, text="Bussiness",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=140)
        
        if(streamVal==1):
            Label(second, text="Chemistry",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=180)
        elif(streamVal==2):
            Label(second, text="Geography",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=180)
        else:
            Label(second, text="Accountancy",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=180)

      
        if(streamVal==1):
            Label(second, text="Biology",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=220)
        elif(streamVal==2):
            Label(second, text="Political Sci.",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=220)
        else:
            Label(second, text="Economics",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=220)

        if(streamVal==1):
            Label(second, text="Mathematics",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=260)
        elif(streamVal==2):
            Label(second, text="Physical Edu.",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=260)
        else:
            Label(second, text="Mathematics",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=260)
                  
        Label(second, text="English",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=300)


     #sub2
        sub1T=IntVar()
        sub1Prc=IntVar()
        sub1A=IntVar()
        sub1P=IntVar()
        
        sub1T=Entry(second,font=("Arial",14))
        sub1T.place(x=660,y=140)
        sub1Prc=Entry(second,font=("Arial",14))
        sub1Prc.place(x=810,y=140)
        sub1A=Entry(second,font=("Arial",14))
        sub1A.place(x=980,y=140)
        sub1P=Entry(second,font=("Arial",14))
        sub1P.place(x=1120,y=140)
        sub1Tv=sub1T.get()
        sub1Prcv=sub1Prc.get()
        sub1Av=sub1A.get()
        sub1Pv=sub1P.get()
       
        #sub2
        sub2T=IntVar()
        sub2Prc=IntVar()
        sub2A=IntVar()
        sub2P=IntVar()
            
        sub2T=Entry(second,font=("Arial",14))
        sub2T.place(x=660,y=180)
        sub2Prc=Entry(second,font=("Arial",14))
        sub2Prc.place(x=810,y=180)
        sub2A=Entry(second,font=("Arial",14))
        sub2A.place(x=980,y=180)
        sub2P=Entry(second,font=("Arial",14))
        sub2P.place(x=1120,y=180)
        
        sub2Tv=sub2T.get()
        sub2Prcv=sub2Prc.get()
        sub2Av=sub2A.get()
        sub2Pv=sub2P.get()        

        #sub3
        sub3T=IntVar()
        sub3Prc=IntVar()
        sub3A=IntVar()
        sub3P=IntVar()

          
        sub3T=Entry(second,font=("Arial",14))
        sub3T.place(x=660,y=220)
        sub3Prc=Entry(second,font=("Arial",14))
        sub3Prc.place(x=810,y=220)
        sub3A=Entry(second,font=("Arial",14))
        sub3A.place(x=980,y=220)
        sub3P=Entry(second,font=("Arial",14))
        sub3P.place(x=1120,y=220)
        
        sub3Tv=sub3T.get()
        sub3Prcv=sub3Prc.get()
        sub3Av=sub3A.get()
        sub3Pv=sub3P.get()        

        #sub3

    #sub4
        sub4T=IntVar()
        sub4Prc=IntVar()
        sub4A=IntVar()
        sub4P=IntVar()
          
        sub4T=Entry(second,font=("Arial",14))
        sub4T.place(x=660,y=260)
        sub4Prc=Entry(second,font=("Arial",14))
        sub4Prc.place(x=810,y=260)
        sub4A=Entry(second,font=("Arial",14))
        sub4A.place(x=980,y=260)
        sub4P=Entry(second,font=("Arial",14))
        sub4P.place(x=1120,y=260)
        
             
        

    #sub5
        sub5T=IntVar()
        sub5Prc=IntVar()
        sub5A=IntVar()
        sub5P=IntVar()
          
        sub5T=Entry(second,font=("Arial",14))
        sub5T.place(x=660,y=300)
        sub5Prc=Entry(second,font=("Arial",14))
        sub5Prc.place(x=810,y=300)
        sub5A=Entry(second,font=("Arial",14))
        sub5A.place(x=980,y=300)
        sub5P=Entry(second,font=("Arial",14))
        sub5P.place(x=1120,y=300)
        
        
        Label(second,text="Guidelines :",font=("Arial",12),bg=darkBG,fg="red").place(x=510,y=520)
        Label(second,text="*SCIENCE-Physics,Chemistry,Biology,Mathematics,English", font=("Arial",12),bg=darkBG, fg="red").place(x=520,y=550)
        Label(second,text="*HUMANITIES/ARTS-History,Geography,Political Sci.,Physical Education.,", font=("Arial",12),bg=darkBG, fg="red").place(x=520,y=580)       
        Label(second,text="*COMMERCE-Bussiness,Accountancy,Economics,Mathematics,English", font=("Arial",12),bg=darkBG, fg="red").place(x=520,y=610)
        Label(second,text="*It is mandatory for the candidate to enter the marks for all the above mentioned subjects. ", font=("Arial",12),bg=darkBG, fg="red").place(x=520,y=640)
        Label(second,text="*If subject entry is not applicable enter full marks and convert the marks according to full marks. ", font=("Arial",12),bg=darkBG, fg="red").place(x=520,y=670)
        board= IntVar()
        gender=IntVar()   
        level = IntVar()
        stream= IntVar()
        res = PhotoImage(file="sub_img.png")
        Button(second, text="submit", bd=0,relief=RIDGE, image=res,bg=lightBG,activebackground=lightBG, command=proceed).place(x=700, y=420)
        nik = Label(second, text="", font=("Helvetica",10,"bold"), bg=lightBG, fg="red")
        nik.place(x=680, y=400)
          
        
        second.mainloop()
        return
    def proceed():
        #creating_LISTS to STORE_INPUTDATA
        global sub1Tv,nik,sub1Prcv,sub1Av,sub1Pv
        global second,std_id 
        global listStr,listS1,listS2,listS3,listS4,listS5
        
        
        sub1Tv=sub1T.get()
        sub1Prcv=sub1Prc.get()
        sub1Av=sub1A.get()
        sub1Pv=sub1P.get()

        sub2Tv=sub2T.get()
        sub2Prcv=sub2Prc.get()
        sub2Av=sub2A.get()
        sub2Pv=sub2P.get()

        sub3Tv=sub3T.get()
        sub3Prcv=sub3Prc.get()
        sub3Av=sub3A.get()
        sub3Pv=sub3P.get()
        
        sub4Tv=sub4T.get()
        sub4Prcv=sub4Prc.get()
        sub4Av=sub4A.get()
        sub4Pv=sub4P.get()

        sub5Tv=sub5T.get()
        sub5Prcv=sub5Prc.get()
        sub5Av=sub5A.get()
        sub5Pv=sub5P.get()

        #VALIDATION applied_to_SUBJECTS
        
        if (len(sub1Tv)==0 or len(sub1Tv)>=4) or (len(sub2Tv)==0 or len(sub2Tv)>=4) or(len(sub3Tv)==0 or len(sub3Tv)>=4) or (len(sub4Tv)==0 or len(sub4Tv)>=4) or (len(sub5Tv)==0 or len(sub5Tv)>=4) :
            nik.config(text="Please Enter valid Theory marks!")
            return 
        elif (len(sub1Prcv)==0 or len(sub1Prcv)>=3)or(len(sub2Prcv)==0 or len(sub2Prcv)>=3)or(len(sub3Prcv)==0 or len(sub3Prcv)>=3)or(len(sub4Prcv)==0 or len(sub4Prcv)>=3)or(len(sub5Prcv)==0 or len(sub5Prcv)>=3):
            nik.config(text="Please Enter valid  Practical marks!")
            return 
        elif (len(sub1Av)==0 or len(sub1Av)>=4) or(len(sub2Av)==0 or len(sub2Av)>=4)or(len(sub3Av)==0 or len(sub3Av)>=4)or(len(sub4Av)==0 or len(sub4Av)>=4)or(len(sub5Av)==0 or len(sub5Av)>=4):
            nik.config(text="Please Enter valid Attendance!")
            return
        elif (len(sub1Pv)==0 or len(sub1Pv)>=3) or (len(sub2Pv)==0 or len(sub2Pv)>=3) or (len(sub3Pv)==0 or len(sub3Pv)>=3) or (len(sub4Pv)==0 or len(sub4Pv)>=3) or (len(sub5Pv)==0 or len(sub5Pv)>=3):
            nik.config(text="Please Enter valid Project marks!")
            return     
        else:
            nik.config(text="click to continue")
            
        #prints the LIST_CREATED
       
        print("final values")                     
        listS1=[]
        listS1.extend([sub1Tv,sub1Prcv,sub1Av,sub1Pv])
        listS2=[]
        listS2.extend([sub2Tv,sub2Prcv,sub2Av,sub2Pv])
        listS3=[]
        listS3.extend([sub3Tv,sub3Prcv,sub3Av,sub3Pv])
        listS4=[]
        listS4.extend([sub4Tv,sub4Prcv,sub4Av,sub4Pv])
        listS5=[]
        listS5.extend([sub5Tv,sub5Prcv,sub5Av,sub5Pv])
        
        print(listS1)
        print(listS2)
        print(listS3)
        print(listS4)
        print(listS5)

        
        #DATABASECODE_to_STORE_INPUTDATA::

        global coc, cursor,flag,std_id
        coc = sqlite3.connect("databaseNK.db")
        cursor = coc.cursor()
        
        
        def get_var_value(filename="fileML.txt"):
            with open(filename,"a+") as f:
                f.seek(0)
                val=int(f.read() or 0) + 1
                f.seek(0)
                f.truncate()
                f.write(str(val))
                return val
        std_id=get_var_value()
        try:
            cursor.execute("CREATE TABLE guide (std_id INTEGER NOT NULL,theory INTEGER,practical INTEGER,attendance INTEGER,project INTEGER )")
        except:
            cursor.execute("INSERT INTO guide values(?,?,?,?,?) ",(std_id,sub1Tv,sub1Prcv,sub1Av,sub1Pv))
            cursor.execute("INSERT INTO guide values(?,?,?,?,?) ",(std_id,sub2Tv,sub2Prcv,sub2Av,sub2Pv))
            cursor.execute("INSERT INTO guide values(?,?,?,?,?) ",(std_id,sub3Tv,sub3Prcv,sub3Av,sub3Pv))
            cursor.execute("INSERT INTO guide values(?,?,?,?,?) ",(std_id,sub4Tv,sub4Prcv,sub4Av,sub4Pv))
            cursor.execute("INSERT INTO guide values(?,?,?,?,?) ",(std_id,sub5Tv,sub5Prcv,sub5Av,sub5Pv))
            
        coc.commit()
        cursor.close()
        coc.close()
        
        
        second.destroy()
        global lb

        lb = Toplevel()
        lb.wm_attributes("-fullscreen", "true")
        bg = PhotoImage(file="bg.png")
        listStr=[]
        Label(lb, image=bg).place(relwidth=1, relheight=1)
        close = PhotoImage(file="close.png")
        Button(lb, bd=0, image=close, bg="#eafde7", activebackground="#eafde7", command=lb.destroy).place(x=1320,y=10)    
        #Label(lb, text="Here are the details you have provided!",font=("Courier",20,"bold"),bg=lightBG).place(x=580,y=30)
        Button(lb, bd=0, image=close, bg="#eafde7", activebackground="#eafde7", command=lb.destroy).place(x=1320,y=10)
        if boardVal==1:
            boardtext="CBSE"
        elif boardVal==2:
            boardtext="SSC"
        else:
            boardtext="OTHERS"
            
        if genVal==1:
            gentext="Male"

        else:
            gentext="Female"
            
        if streamVal==1:
            streamtext="Science"
            listStr.extend(['physics','chemistry','biology','mathematics','English'])
        elif streamVal==2:
            streamtext="Humanities/Arts"
            listStr.extend(['History','Geography','Political Science','Physical Education','English'])

        else:
            streamtext="Commerce"
            listStr.extend(['Bussiness','Accounts','Economics','Mathematics','English'])

            
            
        print(listStr)
        #prints the INPUTDATA_STORED
        #by ACCESSING_THE_DATABASE
        Label(lb, text="Hello", font=("Courier",20,"bold"),bg=lightBG, fg="#27292b").place(x=500,y=25)
        Label(lb, text=" "+nameVal+"!", font=("Courier",20,"bold"),bg=lightBG).place(x=585,y=25) 
        Label(lb, text="Here are the details you have provided!",font=("Courier",15,"bold"),bg=lightBG).place(x=430,y=80)

        Label(lb, text="Gender: "+ gentext, font=("Courier", 15,"bold"),bg=lightBG).place(x=300,y=140)          
        Label(lb, text="12th Board: "+ boardtext, font=("Courier",15,"bold"),bg=lightBG).place(x=300,y=180)

        Label(lb, text="DOB: "+str(dobVal), font=("Courier", 15,"bold"),bg=lightBG).place(x=300,y=220)
        edit = PhotoImage(file="edit.png")
        Button(lb, bd=0,image=edit,bg=darkBG,activebackground=darkBG,command=goBack).place(x=550,y=550)

       
        Label(lb, text="Stream: "+streamtext, font=("Courier",15,"bold"),bg=lightBG).place(x=300,y=260)
        test = PhotoImage(file="test.png")
        Button(lb, bd=0, image=test, bg=darkBG, activebackground=darkBG,command=take_test ).place(x=850,y=550)


        coc = sqlite3.connect("databaseNK.db")
        cursor = coc.cursor()
        
        cursor.execute("Select * from guide order by std_id desc LIMIT 5")

        Label(lb, text="Sub.",font=("Courier",15,"bold"),bg=lightBG).place(x=780,y=150)
        Label(lb, text="S_ID",font=("Courier",15,"bold"),bg=lightBG).place(x=850,y=150)
        Label(lb, text="Th.",font=("Courier",15,"bold"),bg=lightBG).place(x=915,y=150)
        Label(lb, text="Prc.",font=("Courier",15,"bold"),bg=lightBG).place(x=955,y=150)   
        Label(lb, text="Attd.",font=("Courier",15,"bold"),bg=lightBG).place(x=1015,y=150)
        Label(lb, text="Pro.",font=("Courier",15,"bold"),bg=lightBG).place(x=1060,y=150)
     
        finalData=cursor.fetchall()
        F1=Frame(lb,bg=lightBG)
        F1.place(x=750,y=180)
        for z in range(len(finalData)):
            Label(F1, text="subject "+str(z+1),font=("Comic Sans MS",14), bg=lightBG, fg="#27292b").grid(row=z,column=0,padx=10,pady=10)
            Label(F1, text=finalData[z][0],font=("Comic Sans MS",14), bg=lightBG, fg="#27292b").grid(row=z,column=1,padx=10,pady=10)
            Label(F1, text=finalData[z][1],font=("Comic Sans MS",14), bg=lightBG, fg="#27292b").grid(row=z,column=2,padx=10,pady=10)
            Label(F1, text=finalData[z][2],font=("Comic Sans MS",14), bg=lightBG, fg="#27292b").grid(row=z,column=3,padx=10,pady=10)
            Label(F1, text=finalData[z][3],font=("Comic Sans MS",14), bg=lightBG, fg="#27292b").grid(row=z,column=4,padx=10,pady=10)
            Label(F1, text=finalData[z][4],font=("Comic Sans MS",14), bg=lightBG, fg="#27292b").grid(row=z,column=5,padx=10,pady=10)
                                        
        lb.mainloop()
        return
    def goBack():
        lb.destroy()
        firstUI()
    #EXECUTION_starts_from_here  
    Splash()
    print("came back to main")
 
       
def take_test():
    global v6,v5,v4,v3,v2,v1
    global window,lb
    if(window==1):
        lb.destroy()
    global count1,count2,count3,chai
    global result
    count1=0
    def function1():
        first.destroy()
        sai()

    def function2():
        second.destroy()
        sai()

    def function3():
        third.destroy()
        sai()
        
    def chai1():
        master.destroy()
        satya1()
    def chai2():
        master.destroy()
        satya2()
    def chai3():
        master.destroy()
        satya1()

    def window():
        global v6,v5,v4,v3,v2,v1
        chai=Toplevel()
        count1=0
        temp=0
        chai.title('Result')
        chai.geometry('3000x3000')
        f1=Frame(chai)
        '''
        result=PhotoImage(file='result.png')
        ck=Label(chai,image=result)
        ck.place(x=0,y=0,rewidth=1,relheight=1)
        ck.pack()
        '''
        f1.place()
        A=v6.get()
        B=v5.get()
        C=v4.get()
        D=v3.get()
        E=v2.get()
        F=v1.get()
        if(A==2):
            count1=count1+1
        if(B==4):
            count1=count1+1
        if(C==1):
            count1=count1+1
        if(D==2):
            count1=count1+1
        if(E==4):
            count1=count1+1
        if(F==2):
            count1=count1+1
        print(count1)
        l1=Label(chai,text=count1,borderwidth=10)
        l1.place(x=600,y=50)
        l1.configure(font=("Times New Roman",300,"bold"))
        l1=Label(chai,text="MARKS",borderwidth=10)
        l1.place(x=630,y=450)
        l1.configure(font=("Times New Roman",30,"bold"))
        if A==0:
            temp=temp+1
        if B==0:
            temp=temp+1
        if C==0:
            temp=temp+1
        if D==0:
            temp=temp+1
        if E==0:
            temp=temp+1
        if F==0:
            temp=temp+1
        Attempt=6-temp
        l1=Label(chai,text=temp,borderwidth=10)
        l1.place(x=550,y=600)
        l1.configure(font=("Times New Roman",20,"bold"))
        l2=Label(chai,text=Attempt,borderwidth=10)
        l2.place(x=1100,y=600)
        l2.configure(font=("Times New Roman",20,"bold"))
        l3=Label(chai,text="UNATTEMPTED",borderwidth=10)
        l3.place(x=300,y=600)
        l3.configure(font=("Times New Roman",20,"bold"))
        l4=Label(chai,text="ATTEMPTED",borderwidth=10)
        l4.place(x=900,y=600)
        l4.configure(font=("Times New Roman",20,"bold"))


    def Window1():
        global v6,v5,v4,v3,v2,v1,first,result
        chai=Toplevel()
        count2=0
        temp=0
        chai.title('Result')
        chai.geometry('3000x3000')
        f1=Frame(chai)
        '''
        result=PhotoImage(file='result.png')
        ck=Label(chai,image=result)
        ck.place(x=0,y=0,rewidth=1,relheight=1)
        ck.pack()
        '''
        f1.place()
        A=v6.get()
        B=v5.get()
        C=v4.get()
        D=v3.get()
        E=v2.get()
        F=v1.get()
        if(A==1):
            count2=count2+1
        if(B==3):
            count2=count2+1
        if(C==2):
            count2=count2+1
        if(D==3):
            count2=count2+1
        if(E==4):
            count2=count2+1
        if(F==1):
            count2=count2+1

        print(count2)
        l1=Label(chai,text=count2,borderwidth=10)
        l1.place(x=600,y=50)
        l1.configure(font=("Times New Roman",300,"bold"))
        l1=Label(chai,text="MARKS",borderwidth=10)
        l1.place(x=630,y=450)
        l1.configure(font=("Times New Roman",30,"bold"))
        if A==0:
            temp=temp+1
        if B==0:
            temp=temp+1
        if C==0:
            temp=temp+1
        if D==0:
            temp=temp+1
        if E==0:
            temp=temp+1
        if F==0:
            temp=temp+1
        Attempt=6-temp
        l1=Label(chai,text=temp,borderwidth=10)
        l1.place(x=550,y=600)
        l1.configure(font=("Times New Roman",20,"bold"))
        l2=Label(chai,text=Attempt,borderwidth=10)
        l2.place(x=1100,y=600)
        l2.configure(font=("Times New Roman",20,"bold"))
        l3=Label(chai,text="UNATTEMPTED",borderwidth=10)
        l3.place(x=300,y=600)
        l3.configure(font=("Times New Roman",20,"bold"))
        l4=Label(chai,text="ATTEMPTED",borderwidth=10)
        l4.place(x=900,y=600)
        l4.configure(font=("Times New Roman",20,"bold"))
        

    def Window2():
        global v6,v5,v4,v3,v2,v1,first,result
        chai=Toplevel()
        count3=0
        temp=0
        chai.title('Result')
        chai.geometry('3000x3000')
        f1=Frame(chai)
        '''
        result=PhotoImage(file='result.png')
        ck=Label(chai,image=result)
        ck.place(x=0,y=0,rewidth=1,relheight=1)
        ck.pack()
        '''
        f1.place()
        A=v6.get()
        B=v5.get()
        C=v4.get()
        D=v3.get()
        E=v2.get()
        F=v1.get()
        if(A==2):
            count3=count3+1
        if(B==4):
            count3=count3+1
        if(C==1):
            count3=count3+1
        if(D==2):
            count3=count3+1
        if(E==4):
            count3=count3+1
        if(F==2):
            count3=count3+1

        print(count3)
        l1=Label(chai,text=count3,borderwidth=10)
        l1.place(x=600,y=50)
        l1.configure(font=("Times New Roman",300,"bold"))
        l1=Label(chai,text="MARKS",borderwidth=10)
        l1.place(x=630,y=450)
        l1.configure(font=("Times New Roman",30,"bold"))
        if A==0:
            temp=temp+1
        if B==0:
            temp=temp+1
        if C==0:
            temp=temp+1
        if D==0:
            temp=temp+1
        if E==0:
            temp=temp+1
        if F==0:
            temp=temp+1
        Attempt=6-temp
        l1=Label(chai,text=temp,borderwidth=10)
        l1.place(x=550,y=600)
        l1.configure(font=("Times New Roman",20,"bold"))
        l2=Label(chai,text=Attempt,borderwidth=10)
        l2.place(x=1100,y=600)
        l2.configure(font=("Times New Roman",20,"bold"))
        l3=Label(chai,text="UNATTEMPTED",borderwidth=10)
        l3.place(x=300,y=600)
        l3.configure(font=("Times New Roman",20,"bold"))
        l4=Label(chai,text="ATTEMPTED",borderwidth=10)
        l4.place(x=900,y=600)
        l4.configure(font=("Times New Roman",20,"bold"))


            

    def satya1():
        global v6,v5,v4,v3,v2,v1,first,result
        first=Toplevel()
        first.wm_attributes('-fullscreen','true')
        first.title('MATHS QUIZ')
        back=PhotoImage(file="back6.png")
        bk=Label(first,image=back)
        bk.place(x=0,y=0,relwidth=1,relheight=1)


        v6=IntVar()
        q6=Label(first,text='1.While catching a ball, a player pulls down his hands to lower the' ,bg="#f15922")
        q6.place(x=10,y=0)
        q6.configure(font=("Times New Roman",15,"bold"))
        r21=Radiobutton(first,text='a) force',variable=v6,value=1,bg="#f15922")
        r21.place(x=10,y=30)
        r21.configure(font=("Times New Roman",15,"bold"))
        r22=Radiobutton(first,text='b) moment',variable=v6,value=2,bg="#f15922")   ### answer
        r22.place(x=10,y=60)
        r22.configure(font=("Times New Roman",15,"bold"))
        r23=Radiobutton(first,text='c) impulse',variable=v6,value=3,bg="#f15922")
        r23.place(x=10,y=90)
        r23.configure(font=("Times New Roman",15,"bold"))
        r24=Radiobutton(first,text='d) catching time',variable=v6,value=4,bg="#f15922")
        r24.place(x=10,y=120)
        r24.configure(font=("Times New Roman",15,"bold"))

        
        v5=IntVar()
        q5=Label(first,text='2.The different colors of different starts are due to the variation of',bg="#f15922")
        q5.place(x=10,y=180)
        q5.configure(font=("Times New Roman",15,"bold"))
        r17=Radiobutton(first,text='a) temperature',variable=v5,value=1,bg="#f15922")
        r17.place(x=10,y=210)
        r17.configure(font=("Times New Roman",15,"bold"))
        r18=Radiobutton(first,text='b) pressure',variable=v5,value=2,bg="#f15922")
        r18.place(x=10,y=240)
        r18.configure(font=("Times New Roman",15,"bold"))
        r19=Radiobutton(first,text='c) density',variable=v5,value=3,bg="#f15922")
        r19.place(x=10,y=270)
        r19.configure(font=("Times New Roman",15,"bold"))
        r20=Radiobutton(first,text='d) radiation ',variable=v5,value=4,bg="#f15922") ### answer
        r20.place(x=10,y=300)
        r20.configure(font=("Times New Roman",15,"bold"))


        v4=IntVar()
        q4=Label(first,text='3.Woolen clothes keep the body warm because ?',bg="#f15922")
        q4.place(x=10,y=360)
        q4.configure(font=("Times New Roman",15,"bold"))
        #q4=Label(first,text='interest .What is the rate of interest?',bg="#f15922")
        #q4.place(x=10,y=390)
        #q4.configure(font=("Times New Roman",15,"bold"))
        r13=Radiobutton(first,text='a) Wool increases the temperature of the body ',variable=v4,value=1,bg="#f15922") ### answer
        r13.place(x=10,y=390)
        r13.configure(font=("Times New Roman",15,"bold"))
        r14=Radiobutton(first,text='b) Wool is a bad conductor',variable=v4,value=2,bg="#f15922")
        r14.place(x=10,y=420)
        r14.configure(font=("Times New Roman",15,"bold"))
        r15=Radiobutton(first,text='c) Wool absorbs radiant heat from outer objects',variable=v4,value=3,bg="#f15922")
        r15.place(x=10,y=450)
        r15.configure(font=("Times New Roman",15,"bold"))
        r16=Radiobutton(first,text='d) none of the above',variable=v4,value=4,bg="#f15922")
        r16.place(x=10,y=480)
        r16.configure(font=("Times New Roman",15,"bold"))

        exit = Button(first, justify=LEFT,bg="#005367",activebackground="#005367")
        ex = PhotoImage(file="icon.png")
        exit.config(image=ex, width="30", height="30", bd=0, command=first.destroy)
        exit.place(x=1300,y=30)


        v3=IntVar()
        q3=Label(first,text='4.The shape of our milky way galaxy is ?',bg="#005367")
        q3.place(x=700,y=0)
        q3.configure(font=("Times New Roman",15,"bold"),foreground="white")
        r9=Radiobutton(first,text='a) circular',variable=v3,value=1,bg="#005367")
        r9.place(x=700,y=30)
        r9.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r10 = Radiobutton(first, text='b) ellipitical ', variable=v3, value=2,bg="#005367")   ###answer
        r10.place(x=700,y=60)
        r10.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r11 = Radiobutton(first, text="c) sprial", variable=v3, value=3,bg="#005367")
        r11.place(x=700,y=90)
        r11.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r12 = Radiobutton(first, text="d) none of the above ", variable=v3, value=4,bg="#005367")
        r12.place(x=700,y=120)
        r12.configure(font=("Times New Roman",15,"bold"),foreground="orange")

        b=Button(first,justify = LEFT)
        photo=PhotoImage(file="sub2.png")
        b.config(image=photo,width="200",height="40",bd=0,activebackground="#f15922",command=window)
        b.place(x=400,y=600)

        b1=Button(first,justify = LEFT)
        photo1=PhotoImage(file="backbutton.png")
        b1.config(image=photo1,width="200",height="55",activebackground="#f15922",bg="#005367",bd=0,command=function1)
        b1.place(x=900,y=600)

        v2=IntVar()
        q2=Label(first,text='5. If the length of a simple pendulum is halved then its period of oscillation is ',bg="#005367")
        q2.place(x=700,y=180)
        q2.configure(font=("Times New Roman",15,"bold"),foreground="white")
        r5 = Radiobutton(first, text="a) doubled", variable=v2, value=1,bg="#005367")
        r5.place(x=700,y=210)
        r5.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r6 = Radiobutton(first, text="b) halved", variable=v2, value=2,bg="#005367")
        r6.place(x=700,y=240)
        r6.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r7 = Radiobutton(first, text="c)increased by a factor", variable=v2, value=3,bg="#005367")
        r7.place(x=700,y=270)
        r7.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r8 = Radiobutton(first, text="d) decreased by a factor", variable=v2, value=4,bg="#005367")  ##answer
        r8.place(x=700,y=300)
        r8.configure(font=("Times New Roman",15,"bold"),foreground="orange")


        v1=IntVar()
        q=Label(first,text='6.Instrument used to measure the force and velocity  ?',bg="#005367")
        q.place(x=700,y=360)
        q.configure(font=("Times New Roman",15,"bold"),foreground="white")
        r1=Radiobutton(first,text='a) Ammeter',variable=v1,value=1,bg="#005367")
        r1.place(x=700,y=390)
        r1.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r2=Radiobutton(first,text='b) Anemometer ',variable=v1,value=2,bg="#005367")  ##answer
        r2.place(x=700,y=420)
        r2.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r3=Radiobutton(first,text='c) Altimeter',variable=v1,value=3,bg="#005367")
        r3.place(x=700,y=450)
        r3.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r4=Radiobutton(first,text='d) Audiometer',variable=v1,value=4,bg="#005367")
        r4.place(x=700,y=480)
        r4.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        first.mainloop()



        
    def satya2():
        global v6,v5,v4,v3,v2,v1,second,result
        second=Toplevel()
        second.wm_attributes('-fullscreen','true')
        second.title('MATHS QUIZ')
        back=PhotoImage(file="back6.png")
        bk=Label(second,image=back)
        bk.place(x=0,y=0,relwidth=1,relheight=1)

        v6=IntVar()
        q6=Label(second,text='1.Slope of the line ax+by+c=0 is ',bg="#f15922")
        q6.place(x=10,y=0)
        q6.configure(font=("Times New Roman",15,"bold"))
        r21=Radiobutton(second,text='a) -b/a',variable=v6,value=1,bg="#f15922")
        r21.place(x=10,y=30)
        r21.configure(font=("Times New Roman",15,"bold"))
        r22=Radiobutton(second,text='b) -c/a',variable=v6,value=2,bg="#f15922")
        r22.place(x=10,y=60)
        r22.configure(font=("Times New Roman",15,"bold"))
        r23=Radiobutton(second,text='c) -a/b',variable=v6,value=3,bg="#f15922")
        r23.place(x=10,y=90)
        r23.configure(font=("Times New Roman",15,"bold"))
        r24=Radiobutton(second,text='d) none of the above',variable=v6,value=4,bg="#f15922")
        r24.place(x=10,y=120)
        r24.configure(font=("Times New Roman",15,"bold"))


        v5=IntVar()
        q5=Label(second,text='2.What is the probabiity of getting a sum of 9 from two trows of dies ?',bg="#f15922")
        q5.place(x=10,y=180)
        q5.configure(font=("Times New Roman",15,"bold"))
        r17=Radiobutton(second,text='a) 1/6 ',variable=v5,value=1,bg="#f15922")
        r17.place(x=10,y=210)
        r17.configure(font=("Times New Roman",15,"bold"))
        r18=Radiobutton(second,text='b) 1/8',variable=v5,value=2,bg="#f15922")
        r18.place(x=10,y=240)
        r18.configure(font=("Times New Roman",15,"bold"))
        r19=Radiobutton(second,text='c) 1/9',variable=v5,value=3,bg="#f15922")
        r19.place(x=10,y=270)
        r19.configure(font=("Times New Roman",15,"bold"))
        r20=Radiobutton(second,text='d) 1/12',variable=v5,value=4,bg="#f15922")
        r20.place(x=10,y=300)
        r20.configure(font=("Times New Roman",15,"bold"))


        v4=IntVar()
        q4=Label(second,text='3.A sum of Rs. 12,500 amounts to Rs. 15,500 in 4 years at the rate of simple',bg="#f15922")
        q4.place(x=10,y=360)
        q4.configure(font=("Times New Roman",15,"bold"))
        q4=Label(second,text='interest .What is the rate of interest?',bg="#f15922")
        q4.place(x=10,y=390)
        q4.configure(font=("Times New Roman",15,"bold"))
        r13=Radiobutton(second,text='a) 650',variable=v4,value=1,bg="#f15922")
        r13.place(x=10,y=420)
        r13.configure(font=("Times New Roman",15,"bold"))
        r14=Radiobutton(second,text='b) 690',variable=v4,value=2,bg="#f15922")
        r14.place(x=10,y=450)
        r14.configure(font=("Times New Roman",15,"bold"))
        r15=Radiobutton(second,text='c) 698',variable=v4,value=3,bg="#f15922")
        r15.place(x=10,y=480)
        r15.configure(font=("Times New Roman",15,"bold"))
        r16=Radiobutton(second,text='d) 770',variable=v4,value=4,bg="#f15922")
        r16.place(x=10,y=510)
        r16.configure(font=("Times New Roman",15,"bold"))

        exit = Button(second, justify=LEFT,bg="#005367",activebackground="#005367")
        ex = PhotoImage(file="icon.png")
        exit.config(image=ex, width="30", height="30", bd=0, command=second.destroy)
        exit.place(x=1300,y=30)

        v3=IntVar()
        q3=Label(second,text='4.In how many ways can the etters of the world LEADER can be arranged ?',bg="#005367")
        q3.place(x=700,y=0)
        q3.configure(font=("Times New Roman",15,"bold"),foreground="white")
        r9=Radiobutton(second,text='a) 72',variable=v3,value=1,bg="#005367")
        r9.place(x=700,y=30)
        r9.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r10 = Radiobutton(second, text='b) 144 ', variable=v3, value=2,bg="#005367")
        r10.place(x=700,y=60)
        r10.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r11 = Radiobutton(second, text="c) 360", variable=v3, value=3,bg="#005367")
        r11.place(x=700,y=90)
        r11.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r12 = Radiobutton(second, text="d) 720 ", variable=v3, value=4,bg="#005367")
        r12.place(x=700,y=120)
        r12.configure(font=("Times New Roman",15,"bold"),foreground="orange")

        b=Button(second,justify = LEFT)
        photo=PhotoImage(file="sub2.png")
        b.config(image=photo,width="200",height="40",bd=0,activebackground="#f15922",command=Window1)
        b.place(x=400,y=600)

        b2=Button(second,justify = LEFT)
        photo2=PhotoImage(file="backbutton.png")
        b2.config(image=photo2,width="200",height="55",activebackground="#f15922",bg="#005367",bd=0,command=function2)
        b2.place(x=900,y=600)


        v2=IntVar()
        q2=Label(second,text='5.A sum fetched a total simple interest of Rs. 4016.25 at the rate',bg="#005367")
        q2.place(x=700,y=180)
        q2.configure(font=("Times New Roman",15,"bold"),foreground="white")
        q18=Label(second,text=' of 9 p.c.p.a. in 5 years. What is the sum?',bg="#005367")
        q18.place(x=700,y=210)
        q18.configure(font=("Times New Roman",15,"bold"),foreground="white")
        r5 = Radiobutton(second, text="a)4462.50", variable=v2, value=1,bg="#005367")
        r5.place(x=700,y=240)
        r5.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r6 = Radiobutton(second, text="b)8032.50", variable=v2, value=2,bg="#005367")
        r6.place(x=700,y=270)
        r6.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r7 = Radiobutton(second, text="c)8900", variable=v2, value=3,bg="#005367")
        r7.place(x=700,y=300)
        r7.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r8 = Radiobutton(second, text="d)8925", variable=v2, value=4,bg="#005367")
        r8.place(x=700,y=330)
        r8.configure(font=("Times New Roman",15,"bold"),foreground="orange")


        v1=IntVar()
        q=Label(second,text='6.Log(1/8) to the base x =-3/2',bg="#005367")
        q.place(x=700,y=390)
        q.configure(font=("Times New Roman",15,"bold"),foreground="white")
        r1=Radiobutton(second,text='a)-4',variable=v1,value=1,bg="#005367")
        r1.place(x=700,y=420)
        r1.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r2=Radiobutton(second,text='b)4',variable=v1,value=2,bg="#005367")
        r2.place(x=700,y=450)
        r2.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r3=Radiobutton(second,text='c)1/4',variable=v1,value=3,bg="#005367")
        r3.place(x=700,y=480)
        r3.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r4=Radiobutton(second,text='d)10',variable=v1,value=4,bg="#005367")
        r4.place(x=700,y=510)
        r4.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        second.mainloop()

            
    def satya3():
        global v6,v5,v4,v3,v2,v1,third,result
        third=Toplevel()
        third.wm_attributes('-fullscreen','true')
        third.title('MATHS QUIZ')
        back=PhotoImage(file="back6.png")
        bk=Label(third,image=back)
        bk.place(x=0,y=0,relwidth=1,relheight=1)
        
        v6=IntVar()
        q6=Label(third,text='1.The green color seen in firework displays is due to the chloride salt of ',bg="#f15922")
        q6.place(x=10,y=0)
        q6.configure(font=("Times New Roman",15,"bold"))
        r21=Radiobutton(third,text='a) strontium',variable=v6,value=1,bg="#f15922")
        r21.place(x=10,y=30)
        r21.configure(font=("Times New Roman",15,"bold"))
        r22=Radiobutton(third,text='b) batrium',variable=v6,value=2,bg="#f15922")   ### answer
        r22.place(x=10,y=60)
        r22.configure(font=("Times New Roman",15,"bold"))
        r23=Radiobutton(third,text='c) sodium',variable=v6,value=3,bg="#f15922")
        r23.place(x=10,y=90)
        r23.configure(font=("Times New Roman",15,"bold"))
        r24=Radiobutton(third,text='d) calcium',variable=v6,value=4,bg="#f15922")
        r24.place(x=10,y=120)
        r24.configure(font=("Times New Roman",15,"bold"))


        v5=IntVar()
        q5=Label(third,text='2.The purest form of Iron',bg="#f15922")
        q5.place(x=10,y=180)
        q5.configure(font=("Times New Roman",15,"bold"))
        r17=Radiobutton(third,text='a) Cast iron',variable=v5,value=1,bg="#f15922")
        r17.place(x=10,y=210)
        r17.configure(font=("Times New Roman",15,"bold"))
        r18=Radiobutton(third,text='b) steel',variable=v5,value=2,bg="#f15922")
        r18.place(x=10,y=240)
        r18.configure(font=("Times New Roman",15,"bold"))
        r19=Radiobutton(third,text='c) pig iron',variable=v5,value=3,bg="#f15922")
        r19.place(x=10,y=270)
        r19.configure(font=("Times New Roman",15,"bold"))
        r20=Radiobutton(third,text='d) wrought iron',variable=v5,value=4,bg="#f15922") ### answer
        r20.place(x=10,y=300)
        r20.configure(font=("Times New Roman",15,"bold"))


        v4=IntVar()
        q4=Label(third,text='3.Peroxyacetly nitrate is a ',bg="#f15922")
        q4.place(x=10,y=360)
        q4.configure(font=("Times New Roman",15,"bold"))
        #q4=Label(third,text='interest .What is the rate of interest?',bg="#f15922")
        #q4.place(x=10,y=390)
        #q4.configure(font=("Times New Roman",15,"bold"))
        r13=Radiobutton(third,text='a) Secondary pollutant',variable=v4,value=1,bg="#f15922") ### answer
        r13.place(x=10,y=390)
        r13.configure(font=("Times New Roman",15,"bold"))
        r14=Radiobutton(third,text='b) acidic dye',variable=v4,value=2,bg="#f15922")
        r14.place(x=10,y=420)
        r14.configure(font=("Times New Roman",15,"bold"))
        r15=Radiobutton(third,text='c) plant hormone',variable=v4,value=3,bg="#f15922")
        r15.place(x=10,y=450)
        r15.configure(font=("Times New Roman",15,"bold"))
        r16=Radiobutton(third,text='d) vitamin',variable=v4,value=4,bg="#f15922")
        r16.place(x=10,y=480)
        r16.configure(font=("Times New Roman",15,"bold"))

        exit = Button(third, justify=LEFT,bg="#005367",activebackground="#005367")
        ex = PhotoImage(file="icon.png")
        exit.config(image=ex, width="30", height="30", bd=0, command=third.destroy)
        exit.place(x=1300,y=30)

        v3=IntVar()
        q3=Label(third,text='4.Most commonly used bleaching agent ?',bg="#005367")
        q3.place(x=700,y=0)
        q3.configure(font=("Times New Roman",15,"bold"),foreground="white")
        r9=Radiobutton(third,text='a) alcohol',variable=v3,value=1,bg="#005367")
        r9.place(x=700,y=30)
        r9.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r10 = Radiobutton(third, text='b) chlorine ', variable=v3, value=2,bg="#005367")   ###answer
        r10.place(x=700,y=60)
        r10.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r11 = Radiobutton(third, text="c) sodium chorine", variable=v3, value=3,bg="#005367")
        r11.place(x=700,y=90)
        r11.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r12 = Radiobutton(third, text="d) cardon dioxide ", variable=v3, value=4,bg="#005367")
        r12.place(x=700,y=120)
        r12.configure(font=("Times New Roman",15,"bold"),foreground="orange")

        b=Button(third,justify = LEFT)
        photo=PhotoImage(file="sub2.png")
        b.config(image=photo,width="200",height="40",bd=0,activebackground="#f15922",command=Window2)
        b.place(x=400,y=600)

        b3=Button(third,justify = LEFT)
        photo3=PhotoImage(file="backbutton.png")
        b3.config(image=photo3,width="200",height="55",activebackground="#f15922",bg="#005367",bd=0,command=function3)
        b3.place(x=900,y=600)



        v2=IntVar()
        q2=Label(third,text='5.Combustion is a ',bg="#005367")
        q2.place(x=700,y=180)
        q2.configure(font=("Times New Roman",15,"bold"),foreground="white")
        #q18=Label(third,text=' of 9 p.c.p.a. in 5 years. What is the sum?',bg="#005367")
        #q18.place(x=700,y=210)
        #q18.configure(font=("Times New Roman",15,"bold"),foreground="white")
        r5 = Radiobutton(third, text="a)Physical and chemical process", variable=v2, value=1,bg="#005367")
        r5.place(x=700,y=210)
        r5.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r6 = Radiobutton(third, text="b)bioogical process", variable=v2, value=2,bg="#005367")
        r6.place(x=700,y=240)
        r6.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r7 = Radiobutton(third, text="c)physical process", variable=v2, value=3,bg="#005367")
        r7.place(x=700,y=270)
        r7.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r8 = Radiobutton(third, text="d)chemical process", variable=v2, value=4,bg="#005367")  ##answer
        r8.place(x=700,y=300)
        r8.configure(font=("Times New Roman",15,"bold"),foreground="orange")


        v1=IntVar()
        q=Label(third,text='6.Which of the following is not a form of carbon ?',bg="#005367")
        q.place(x=700,y=360)
        q.configure(font=("Times New Roman",15,"bold"),foreground="white")
        r1=Radiobutton(third,text='a) soot ',variable=v1,value=1,bg="#005367")
        r1.place(x=700,y=390)
        r1.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r2=Radiobutton(third,text='b)hematite',variable=v1,value=2,bg="#005367")  ##answer
        r2.place(x=700,y=420)
        r2.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r3=Radiobutton(third,text='c) graphite',variable=v1,value=3,bg="#005367")
        r3.place(x=700,y=450)
        r3.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        r4=Radiobutton(third,text='d) charcoal',variable=v1,value=4,bg="#005367")
        r4.place(x=700,y=480)
        r4.configure(font=("Times New Roman",15,"bold"),foreground="orange")
        third.mainloop()

    def sai():
        global master
        master=Toplevel()
        master.wm_attributes('-fullscreen','true')
        master.title('MAIN')
        back1=PhotoImage(file="education1.png")
        bk=Label(master,image=back1)
        bk.place(x=0,y=0,relwidth=1,relheight=1)
        l1=Label(master,text='WELCOME TO THE QUIZ')
        l1.place(x=540,y=100)
        l1.configure(font=("Impact",25,"bold italic"),background='red',foreground='white')

        exit = Button(master, justify=LEFT,bg="#005367",activebackground="#005367")
        ex = PhotoImage(file="icon.png")
        exit.config(image=ex, width="30", height="30", bd=0, command=master.destroy)
        exit.place(x=1300,y=30)

        l2=Button(master,text="Click here to enter PHYSICS QUIZ",command=chai3)
        l2.place(x=30,y=250)
        l2.configure(font=("Times New Roman",15,"bold"))

      
        
        '''    
        exit1 = Button(master, justify=LEFT)
        ex1 = PhotoImage(file="run.png")
        exit1.config(image=ex1, width="30", height="30", bd=0, command=chai1)
        exit1.place(x=370,y=240)
        '''
        
        l4=Button(master,text="Click here to enter MATHS QUIZ",command=chai2)
        l4.place(x=30,y=350)
        l4.configure(font=("Times New Roman",15,"bold"))    
        '''
        exit2 = Button(master, justify=LEFT,activebackground="#005367")
        ex2 = PhotoImage(file="run.png")
        exit2.config(image=ex2, width="30", height="30", bd=0, command=chai2)
        exit2.place(x=370,y=340)
        '''
        
        l3=Button(master,text="Click here to enter CHEMISTRY QUIZ",command=chai3)
        l3.place(x=30,y=450)
        l3.configure(font=("Times New Roman",15,"bold"))
        '''
        exit3 = Button(master, justify=LEFT,activebackground="#005367")
        ex3 = PhotoImage(file="run.png")
        exit3.config(image=ex3, width="30", height="30", bd=0, command=chai3)
        exit3.place(x=390,y=440)
        '''
        back2=PhotoImage(file="images143.png")
        bk=Label(master,image=back2)
        bk.place(x=1000,y=350)

        l10=Button(master,text="Recomendation",command=Recommendation_system)
        l10.place(x=360,y=550)
        l10.configure(font=("Times New Roman",15,"bold"))
        master.mainloop()
        
    sai()

    

    
def fuzzy_calculator(inputs):
    
    
    theory= ctrl.Antecedent(np.arange(0,71,1),'theory')
    practical=ctrl.Antecedent(np.arange(0,31,1,),'practical')
    attendance= ctrl.Antecedent(np.arange(0,101,1),'attendance')
    project= ctrl.Antecedent(np.arange(0,31,1),'project')
    grade=ctrl.Consequent(np.arange(0,101,1),'grade')



    practical['l']=fuzz.trimf(practical.universe,[0,10,15])
    practical['m']=fuzz.trimf(practical.universe,[12,15,24])
    practical['h']=fuzz.trimf(practical.universe,[22,26,31])

    theory['l']=fuzz.trimf(theory.universe,[0,24,36])
    theory['m']=fuzz.trimf(theory.universe,[24,36,48])
    theory['h']=fuzz.trimf(theory.universe,[40,60,71])

    attendance['l']=fuzz.trimf(attendance.universe,[0,40,50])
    attendance['m']=fuzz.trimf(attendance.universe,[45,65,80])
    attendance['h']=fuzz.trimf(attendance.universe,[75,85,101])

    project['l']=fuzz.trimf(project.universe,[0,10,15])
    project['m']=fuzz.trimf(project.universe,[13,15,24])
    project['h']=fuzz.trimf(project.universe,[22,26,31])

    grade['l']=fuzz.trimf(grade.universe,[0,40,50])
    grade['m']=fuzz.trimf(grade.universe,[45,65,80])
    grade['h']=fuzz.trimf(grade.universe,[75,85,101])

   

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

    rule55= ctrl.Rule( theory['h'] & practical['l'] & attendance['l'] & project['l'] , grade['m'])
    rule56= ctrl.Rule( theory['h'] & practical['l'] & attendance['l'] & project['m'] , grade['m'])
    rule57= ctrl.Rule( theory['h'] & practical['l'] & attendance['l'] & project['h'] , grade['m'])
    rule58= ctrl.Rule( theory['h'] & practical['l'] & attendance['m'] & project['l'] , grade['m'])
    rule59= ctrl.Rule( theory['h'] & practical['l'] & attendance['m'] & project['m'] , grade['m'])
    rule60= ctrl.Rule( theory['h'] & practical['l'] & attendance['m'] & project['h'] , grade['m'])
    rule61= ctrl.Rule( theory['h'] & practical['l'] & attendance['h'] & project['l'] , grade['m'])
    rule62= ctrl.Rule( theory['h'] & practical['l'] & attendance['h'] & project['m'] , grade['m'])
    rule63= ctrl.Rule( theory['h'] & practical['l'] & attendance['h'] & project['h'] , grade['m'])
    rule64= ctrl.Rule( theory['h'] & practical['m'] & attendance['l'] & project['l'] , grade['m'])
    rule65= ctrl.Rule( theory['h'] & practical['m'] & attendance['l'] & project['m'] , grade['m'])
    rule66= ctrl.Rule( theory['h'] & practical['m'] & attendance['l'] & project['h'] , grade['m'])
    rule67= ctrl.Rule( theory['h'] & practical['m'] & attendance['m'] & project['l'] , grade['m'])
    rule68= ctrl.Rule( theory['h'] & practical['m'] & attendance['m'] & project['m'] , grade['m'])
    rule69= ctrl.Rule( theory['h'] & practical['m'] & attendance['m'] & project['h'] , grade['h'])
    rule70= ctrl.Rule( theory['h'] & practical['m'] & attendance['h'] & project['l'] , grade['h'])
    rule71= ctrl.Rule( theory['h'] & practical['m'] & attendance['h'] & project['m'] , grade['h'])
    rule72= ctrl.Rule( theory['h'] & practical['m'] & attendance['h'] & project['h'] , grade['h'])
    rule73= ctrl.Rule( theory['h'] & practical['h'] & attendance['l'] & project['l'] , grade['m'])
    rule74= ctrl.Rule( theory['h'] & practical['h'] & attendance['l'] & project['m'] , grade['h'])
    rule75= ctrl.Rule( theory['h'] & practical['h'] & attendance['l'] & project['h'] , grade['h'])
    rule76= ctrl.Rule( theory['h'] & practical['h'] & attendance['m'] & project['l'] , grade['h'])
    rule77= ctrl.Rule( theory['h'] & practical['h'] & attendance['m'] & project['m'] , grade['h'])
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
    wm.input['attendance']=inputs[2]
    wm.input['project']=inputs[3]

    wm.compute()
    out=wm.output['grade']
    print(out)
    
    return out

def Recommendation_system():
    global recommendation,lb
    subjects_science=['physics','chemistry','biology','mathematics','English']
    subjects_commerce=['Bussiness','Accounts','Economics','Mathematics','English']
    subjects_Humanities=['History','Geography','Political Science','Physical Education','English']
    test_scores=[9,9,9,9,9]
    lists1=[int(i) for i in listS1]
    lists2=[int(i) for i in listS2]
    lists3=[int(i) for i in listS3]
    lists4=[int(i) for i in listS4]
    lists5=[int(i) for i in listS5]
    final_marks=[lists1[0]+lists1[1],lists2[0]+lists2[1],lists3[0]+lists3[1],lists4[0]+lists4[1],lists5[0]+lists5[1]]
    
    sub1=fuzzy_calculator(lists1)
    sub2=fuzzy_calculator(lists2)
    sub3=fuzzy_calculator(lists3)
    sub4=fuzzy_calculator(lists4)
    sub5=fuzzy_calculator(lists5)
    lb.destroy()
    recommendation=dict()
    eligibility=sum(final_marks)/5
    
    if(streamVal==1):
        #test for Engineering

        if(eligibility>60 and final_marks[0]>60 and final_marks[1]>60 and final_marks[3]>60):
            fuzz_score=(sub1+sub2+sub3)/3
            recommendation['Engineering']=fuzz_score
        #test for Medical
        if(eligibility>60 and final_marks[2]>60):
            fuzz_score=(sub2+sub3)/2
            recommendation['Medical']=fuzz_score
        #test for Bsc
        if(eligibility>60 and final_marks[0]>60):
            recommendation['Bsc physics']=sub1
        if(eligibility>60 and final_marks[1]>60):
            recommendation['Bsc chemistry']=sub2
        if(eligibility>60 and final_marks[2]>60):
            recommendation['Bsc biology']=sub3
        if(eligibility>60 and final_marks[3]>60):
            recommendation['Bsc mathematics']=sub4
        if(eligibility>60 and final_marks[4]>60):
            recommendation['Bsc Computer Science']=sub4
    elif (streamVal==2):
         #test for BA

        if(eligibility>60 ):
            fuzz_score=(sub1+sub2+sub3+sub4)/4
            recommendation['BA']=fuzz_score
        #test for Journalism and Mass Communication
        if(eligibility>60 and final_marks[2]>60 ):
            recommendation['Journalism and Mass Communication']=sub3
        if(eligibility>60 ):
            recommendation['Fashion Design']=sub5

       
    else:
         #test for Bcom

        if(eligibility>60 ):
            fuzz_score=(sub1+sub2+sub3+sub4)/4
            recommendation['Bcom']=fuzz_score
        #test for BBA
        if(eligibility>60 and final_marks[0]>60):
            fuzz_score=(sub1+sub2)/2
            recommendation['BBA']=fuzz_score
        #test for Bachelor of Economics
        if(eligibility>60 and final_marks[2]>60):
            recommendation['Bachelor of Economics']=sub3
        #test for LLB
        if(eligibility>60 and final_marks[4]>60):
            fuzz_score=(sub3+sub5)/2
            recommendation['LLB']=fuzz_score
        #test for CA
        if(eligibility>60 and final_marks[1]>60):
            fuzz_score=(sub2+sub3)/2
            recommendation['CA']=fuzz_score
       

    if(eligibility>50 and (sum(test_scores)/5) > 5):
        fuzz_score=sub5
        recommendation['Animation and Graphics Design']=sub5


    if(eligibility>60 and (sum(test_scores)/5) > 5 and final_marks[0]>60 and final_marks[1]>60 and final_marks[3]>60 and final_marks[4]>60):
        fuzz_score=(sub1+sub2+sub3+sub4+sub5)/4
        recommendation['B.Ed']=sub5
       
    for i in recommendation:
       print(i,": ",recommendation[i])
    
    path_selection()
def path_selection():
    global recommendation,lb,top
    print(listS1)
    print(listS2)
    print(listS3)
    print(listS4)
    print(listS5)
    global top,window,variable
    
    if window==1:
        top.withdraw()
    top=Toplevel()
    top.geometry("1400x700+0+0")
    top.title("Pathway Selection")
    image1 =PhotoImage(file="path.png")
    top.wm_attributes('-fullscreen', 'true')
    Form = Label(top, image=image1)
    Form.pack(side='top', fill='both', expand='yes')
    close = PhotoImage(master=top, file="close.png")
    Button(top, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=top.destroy).place(x=1320,y=10)
    OptionList=["Animation/Graphics","BA","Bachelor of Education","Bachelor of Economics","BBA","B.Com","BSc Physics","BSc chemistry","BSc biology","BSc mathematics"
                              ,"BSc Computer","CA","Journalism and Communication",
                              "Engineering ",
                              "LLB",
                              "Medical"]
    variable = StringVar(top)
    variable.set(OptionList[0])

    opt = OptionMenu(top, variable, *OptionList)
    opt.config(width=20, font=('Helvetica', 12))
    opt.place(x=950,y=320)


    labelTest = Label(text="", font=('Helvetica', 12), fg='white')
    labelTest.place(x=920,y=320)

    def callback(*args):
        labelTest.configure(text="The selected item is {}".format(variable.get()))

    variable.trace("w", callback)

    
   
    btn_go = Button(Form, text="GO", width=25, command=show_colleges)
    btn_go.place(x=950, y=400)
    btn_go.bind('<Return>',show_colleges )
    btn_go = Button(Form, text="Finish", width=25, command=Thankyou)
    btn_go.place(x=950, y=700)
    btn_go.bind('<Return>',Thankyou )
    
    lab=[0 for i in range(len(recommendation.values()))]
    k=0
    lab1= Label(Form,text="Recommendations matching your profile", font=('Helvetica', 12))
    lab1.place(x=50,y=540)
    for i in recommendation:
        lab[k]= Label(Form,text=str(i)+": "+str(recommendation[i])+"%", font=('Helvetica', 12))
        lab[k].place(x=50,y=570+k*22)
        k+=1
    top.mainloop()   
      
def show_colleges():
    global top,window,variable
    
    if window==1:
        top.withdraw()
    
    path=variable.get()
    print(path)
    
    j=0
    
    data=pd.read_csv('New Microsoft Excel Worksheet.csv')
    
    def display():
        chai=Toplevel()
        chai.geometry("500x400+0+0")
        chai.wm_attributes('-fullscreen','true')
        Label(chai,text="S.no",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=1)
        Label(chai,text="college id",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=2)
        Label(chai,text="college Name",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=3)
        Label(chai,text="NIRF Ranking",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=4)
        Label(chai,text="Fees",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=100)
        A10=Button(chai,text="Dismiss",width=25,height=3,font="Helvetica 10 bold italic",bg="yellow",command=chai.destroy)
        A10.grid(row=100,column=200)
        i=0
        while i<10:
            Label(chai,text=str(data['S.no'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1+i, column =1)
            Label(chai,text=str(data['college id'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1+i, column =2)
            Label(chai,text=str(data['Name'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1+i, column = 3)
            Label(chai,text=str(data['NIRF Ranking'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column =4)
            Label(chai,text=str(data['Fees(in lakhs)'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column =100)
            i+=1 
    
    def show():
        cha=Toplevel()
        cha.wm_attributes('-fullscreen','true')
        cha.geometry("600x400+0+0")  
        Label(cha,text="S.no",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=0)
        Label(cha,text="college id",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=1)
        Label(cha,text="college Name",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=2)
        Label(cha,text="NIRF Ranking",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=3)
        Label(cha,text="Fees",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=4)
        A9=Button(cha,text="Dismiss",width=25,height=3,font="Helvetica 10 bold italic",bg="yellow",command=cha.destroy)
        A9.grid(row=20,column=14)
        i=11
        while i>10 and i<20:
            Label(cha,text=str(data['S.no'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1+i, column =0)
            Label(cha,text=str(data['college id'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 1)
            Label(cha,text=str(data['Name'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 2)
            Label(cha,text=str(data['NIRF Ranking'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 3)
            Label(cha,text=str(data['Fees(in lakhs)'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 4)
            i+=1
        
        
    def show1():
        cha1=Toplevel()
        cha1.wm_attributes('-fullscreen','true')
        cha1.geometry("900x400+0+0")
        cha1.title("LLB")
        
        Label(cha1,text="S.no",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=0)
    
        Label(cha1,text="college id",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=1)
        Label(cha1,text="college Name",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=2)
        Label(cha1,text="NIRF Ranking",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=3)
        Label(cha1,text="Fees",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=4)
        A8=Button(cha1,text="Dismiss",width=25,height=3,font="Helvetica 10 bold italic",bg="yellow",command=cha1.destroy)
        A8.grid(row=1000,column=100)
    
        
        i=22
        
        while i>20 and i<32:
            Label(cha1,text=str(data['S.no'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1+i, column =0)
            Label(cha1,text=str(data['college id'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 1)
            Label(cha1,text=str(data['Name'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 2)
            Label(cha1,text=str(data['NIRF Ranking'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 3)
            Label(cha1,text=str(data['Fees(in lakhs)'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 4)
            i+=1   
        
    
    def show2() :
        cha2=Toplevel()
        cha2.wm_attributes('-fullscreen','true')
        cha2.geometry("900x400+0+0")
        cha2.title("Arts")
        Label(cha2,text="S.no",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=0)
        Label(cha2,text="college id",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=1)
        Label(cha2,text="college Name",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=2)
        Label(cha2,text="NIRF Ranking",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=3)
        Label(cha2,text="Fees",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=4)
        A7=Button(cha2,text="Dismiss",width=25,height=3,font="Helvetica 10 bold italic",bg="yellow",command=cha2.destroy)
        A7.grid(row=1000,column=100)
    
                    
        i=33
        
        while i>32 and i<43:
            Label(cha2,text=str(data['S.no'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1+i, column =0)
            Label(cha2,text=str(data['college id'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 1)
            Label(cha2,text=str(data['Name'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 2)
            Label(cha2,text=str(data['NIRF Ranking'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 3)
            Label(cha2,text=str(data['Fees(in lakhs)'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 4)
            i+=1   
    
    def show3() :
        cha3=Toplevel()
        cha3.wm_attributes('-fullscreen','true')
        cha3.geometry("900x400+0+0")
        cha3.title("Design")
        Label(cha3,text="S.no",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=0)
        Label(cha3,text="college id",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=1)
        Label(cha3,text="college Name",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=2)
        Label(cha3,text="NIRF Ranking",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=3)
        Label(cha3,text="Fees",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=4)
        A6=Button(cha3,text="Dismiss",width=25,height=3,font="Helvetica 10 bold italic",bg="yellow",command=cha3.destroy)
        A6.grid(row=1000,column=100)
    
                
        i=44
        
        while i>43 and i<53:
            Label(cha3,text=str(data['S.no'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1+i, column =0)
    
            Label(cha3,text=str(data['college id'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 1)
            Label(cha3,text=str(data['Name'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 2)
            Label(cha3,text=str(data['NIRF Ranking'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 3)
            Label(cha3,text=str(data['Fees(in lakhs)'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 4)
            i+=1   
        
    def show4() :
        cha4=Toplevel()
        cha4.geometry("900x400+0+0")
        cha4.wm_attributes('-fullscreen','true')
        cha4.title("Design")
        Label(cha4,text="S.no",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=0)
        Label(cha4,text="college id",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=1)
        Label(cha4,text="college Name",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=2)
        Label(cha4,text="NIRF Ranking",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=3)
        Label(cha4,text="Fees",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=4)
        A5=Button(cha4,text="Dismiss",width=25,height=3,font="Helvetica 16 bold italic",bg="yellow",command=cha4.destroy)
        A5.grid(row=1000,column=100)
    
                
        i=55
        
        while i>54 and i<64:
            Label(cha4,text=str(data['S.no'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1+i, column =0)
    
            Label(cha4,text=str(data['college id'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 1)
            Label(cha4,text=str(data['Name'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 2)
            Label(cha4,text=str(data['NIRF Ranking'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 3)
            Label(cha4,text=str(data['Fees(in lakhs)'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 4)
            i+=1   
    
        
    def show5() :
        cha5=Toplevel()
        cha5.geometry("900x400+0+0")
        cha5.wm_attributes('-fullscreen','true')
    
        
        Label(cha5,text="S.no",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=0)  
        Label(cha5,text="college id",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=1)
        Label(cha5,text="college Name",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=2)
        Label(cha5,text="NIRF Ranking",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=3)
        Label(cha5,text="Fees",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=4)
        A0=Button(cha5,text="Dismiss",width=25,height=3,font="Helvetica 10 bold italic",bg="yellow",command=cha5.destroy)
        A0.grid(row=1000,column=100)
    
                
        i=66
        
        while i>65 and i<76:
            Label(cha5,text=str(data['S.no'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1+i, column =0)
            Label(cha5,text=str(data['college id'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 1)
            Label(cha5,text=str(data['Name'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 2)
            Label(cha5,text=str(data['NIRF Ranking'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 3)
            Label(cha5,text=str(data['Fees(in lakhs)'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 4)
            i+=1   
    
    def show6() :
        cha6=Toplevel()
        cha6.geometry("1000x450+0+0")
        cha6.wm_attributes('-fullscreen','true')
    
        cha6.title("BBA")
        
        Label(cha6,text="S.no",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=0)
        Label(cha6,text="college id",font="Helvetica 16 bold italic",fg="red",bg="blue").grid(row=0,column=1)
        Label(cha6,text="college Name",font="Helvetica 16 bold italic",fg="red",bg="blue").grid(row=0,column=2)
        Label(cha6,text="NIRF Ranking",font="Helvetica 16 bold italic",fg="red",bg="blue").grid(row=0,column=3)
        Label(cha6,text="Fees",font="Helvetica 16 bold italic",fg="red",bg="blue").grid(row=0,column=4)
        A1=Button(cha6,text="Dismiss",width=25,height=3,font="Helvetica 10 bold italic",bg="yellow",command=cha6.destroy)
        A1.grid(row=1000,column=100)
    
        
        i=77
        
        while i>76 and i<87:
            Label(cha6,text=str(data['S.no'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1+i, column =0)
            Label(cha6,text=str(data['college id'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 1)
            Label(cha6,text=str(data['Name'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 2)
            Label(cha6,text=str(data['NIRF Ranking'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 3)
            Label(cha6,text=str(data['Fees(in lakhs)'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 4)
            i+=1   
    def show7() :
        cha7=Toplevel()
        cha7.geometry("1000x450+0+0")
        cha7.wm_attributes('-fullscreen','true')
    
        cha7.title("BSC Chemistry")
        Label(cha7,text="S.no",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=0)
        Label(cha7,text="college id",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=1)
        Label(cha7,text="college Name",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=2)
        Label(cha7,text="NIRF Ranking",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=3)
        Label(cha7,text="Fees",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=4)
        A2=Button(cha7,text="Dismiss",width=25,height=3,font="Helvetica 10 bold italic",bg="yellow",command=cha7.destroy)
        A2.grid(row=1000,column=100)
    
        
        i=88
        
        while i>87 and i<98:
            Label(cha7,text=str(data['S.no'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1+i, column =0)
            Label(cha7,text=str(data['college id'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 1)
            Label(cha7,text=str(data['Name'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 2)
            Label(cha7,text=str(data['NIRF Ranking'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 3)
            Label(cha7,text=str(data['Fees(in lakhs)'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 4)
            i+=1   
    
    def show8() :
        cha8=Toplevel()
        cha8.geometry("1000x450+0+0")
        cha8.wm_attributes('-fullscreen','true')
    
        Label(cha8,text="S.no",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=0)
        Label(cha8,text="college id",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=1)
        Label(cha8,text="college Name",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=2)
        Label(cha8,text="NIRF Ranking",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=3)
        Label(cha8,text="Fees",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=4)
        A2=Button(cha8,text="Dismiss",width=25,height=3,font="Helvetica 10 bold italic",bg="yellow",command=cha8.destroy)
        A2.grid(row=1000,column=100)
    
        
        i=99
        
        while i>98 and i<109:
            Label(cha8,text=str(data['S.no'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1+i, column =0)
            Label(cha8,text=str(data['college id'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 1)
            Label(cha8,text=str(data['Name'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 2)
            Label(cha8,text=str(data['NIRF Ranking'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 3)
            Label(cha8,text=str(data['Fees(in lakhs)'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 4)
            i+=1   
    def show9() :
        cha9=Toplevel()
        cha9.geometry("1000x450+0+0")
        cha9.wm_attributes('-fullscreen','true')
    
        cha9.title("Bsc computer science")
       
        Label(cha9,text="S.no",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=0)
        Label(cha9,text="college id",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=1)
        Label(cha9,text="college Name",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=2)
        Label(cha9,text="NIRF Ranking",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=3)
        Label(cha9,text="Fees",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=4)
        A3=Button(cha9,text="Dismiss",width=25,height=3,font="Helvetica 10 bold italic",bg="yellow",command=cha9.destroy)
        A3.grid(row=1000,column=100)
    
        i=99
        
        while i>98 and i<109:
            Label(cha9,text=str(data['S.no'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1+i, column =0)
            Label(cha9,text=str(data['college id'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 1)
            Label(cha9,text=str(data['Name'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 2)
            Label(cha9,text=str(data['NIRF Ranking'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 3)
            Label(cha9,text=str(data['Fees(in lakhs)'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 4)
            i+=1
    def show10() :
        cha10=Toplevel()
        cha10.geometry("1000x450+0+0")
        cha10.wm_attributes('-fullscreen','true')
    
        cha10.title("Bachelor of economic")
        
        Label(cha10,text="S.no",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=0)
        Label(cha10,text="college id",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=1)
        Label(cha10,text="college Name",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=2)
        Label(cha10,text="NIRF Ranking",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=3)
        Label(cha10,text="Fees",font="Helvetica 25 bold italic",fg="red",bg="blue").grid(row=0,column=4)
        A4=Button(cha10,text="Dismiss",width=25,height=3,font="Helvetica 10  bold italic",bg="yellow",command=cha10.destroy)
        A4.grid(row=400,column=10)
    
        i=110
        
        while i>109 and i<120:
            Label(cha10,text=str(data['S.no'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1+i, column =0)
            Label(cha10,text=str(data['college id'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 1)
            Label(cha10,text=str(data['Name'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 2)
            Label(cha10,text=str(data['NIRF Ranking'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 3)
            Label(cha10,text=str(data['Fees(in lakhs)'][i]),font="Helvetica 16 bold italic",fg="red").grid(row = 1 +i, column = 4)
            i+=1   
           
        
                
          #OptionList=[,"
                             
                           
                                 
                              
    if(path=="Engineering"):
        display()
        
    elif(path=="B.Com"):
        show()
    elif(path=="Medical"):
        show1()
    elif(path=="LLB"):
        show2()
    elif(path=="BA"):
        show3()
       
    elif( path=="BSc biology"):
        show5()
    elif(path=="BBA"):
        show6()
        
    elif(path=="BA"):
        show3()
    elif(path=="Animation/Graphics"):
        show4()
    elif(path=="B.Sc Physics"):
        show5()
    elif(path=="B.Sc Chemistry"):
        show7()
    elif(path=="B.Sc Mathematics"):
        show8()
    elif(path=="BSc Computer"):
        show9()
    else:
        show10()
def Thankyou():
    global top,window
    
    if window==1:
        top.withdraw()
    def message():
        messagebox.showinfo("Thankyou","Thankyou for your valuable feedback")
        
    def function():
        top.destroy()
        developers_image()
    
    def function2():
        top.destroy()
        feedback()
    
    def function3():
        image1.destroy()
        back()
    
    def function4():
        feed.destroy()
        back()
    
    def back():
        global top
        top=Toplevel()
        top.wm_attributes("-fullscreen","true")
        back=PhotoImage(file="thankyou.png")
        bk=Label(top,image=back)
        bk.place(x=0,y=0,relwidth=1,relheight=1)
    
        exit = Button(top, justify=LEFT,bg="#005367",activebackground="#005367")
        ex = PhotoImage(file="icon.png")
        exit.config(image=ex, width="30", height="30", bd=0, command=top.destroy)
        exit.place(x=1300,y=30)
    
        back1=Button(top,justify=LEFT)
        developer=PhotoImage(file="develop.png")
        back1.config(image=developer,width="150",height="150",command=function)
        back1.place(x=30,y=463)
    
        back2=Button(top,justify=LEFT)
        feedback=PhotoImage(file="feedback.png")
        back2.config(image=feedback,width="150",height="150",command=function2)
        back2.place(x=1100,y=463)
        top.mainloop()
    
    
    def feedback():
        global feed
        feed=Toplevel()
        feed.wm_attributes("-fullscreen","true")
       # Label(text="",justify=CENTER,relief="flat",width=400,height=100,bg="orange").place(x=0,y=0)
    
        back23=PhotoImage(file="feedbackbackgroundfinal.png")
        bk23=Label(feed,image=back23)
        bk23.place(x=350,y=100,relwidth=1,relheight=1)
    
        b121=Button(feed,justify = LEFT)
        photo12=PhotoImage(file="backbutton.png")
        b121.config(image=photo12,width="200",height="55",activebackground="#f15922",bg="#005367",bd=0,command=function4)
        b121.place(x=300,y=570)
    
    
        b33=Button(feed,justify = LEFT)
        photo2=PhotoImage(file="sub2.png")
        b33.config(image=photo2,width="200",height="40",bd=0,activebackground="#f15922",command=message)
        b33.place(x=510,y=330)
        
        exit1 = Button(feed, justify=LEFT,bg="#005367",activebackground="#005367")
        ex1 = PhotoImage(file="icon.png")
        exit1.config(image=ex1, width="30", height="30", bd=0, command=feed.destroy)
        exit1.place(x=1300,y=30)
        
        Label(feed,text="ENTER YOUR RESPONCE",font=("Times New Roman",25)).place(x=250,y=250)
        e1=Entry(feed,bd=5,width=50).place(x=660,y=260)
        feed.mainloop()
    
    
    
        
    def developers_image():
        global image1
        image1=Toplevel()
        image1.wm_attributes("-fullscreen","true")
        '''
        back1=PhotoImage(file="backgroundplain.png")
        bk2=Label(image1,image=back1)
        bk2.place(x=0,y=0,relwidth=1,relheight=1)
        '''
        Label(text="",justify=CENTER,relief="flat",width=400,height=100,bg="skyblue").place(x=0,y=0)
        b1=Button(image1,justify = LEFT)
        photo1=PhotoImage(file="backbutton.png")
        b1.config(image=photo1,width="200",height="55",activebackground="#f15922",bg="#005367",bd=0,command=function3)
        b1.place(x=900,y=600)
    
        exit = Button(image1, justify=LEFT,bg="#005367",activebackground="#005367")
        ex = PhotoImage(file="icon.png")
        exit.config(image=ex, width="30", height="30", bd=0, command=image1.destroy)
        exit.place(x=1300,y=30)
    
        MOHIT='''    Name:MOHIT SRIKHAKOLLU
                 Email-id:srikakollamohith9@gmail.com
                 Reg no: 11707426
                 Phone No:9182902965 '''
        CHAITANYA='''   Name: Chaitanya Kishore Singaraju
                     Email-id:chaitanya9780@gmail.com
                     Reg no:  11706282
                     Phone No:9603112410'''
        Nikhil='''    Name:Nikhil Raju Kataru
                  Email-id:nikhilkataru07@gmail.com
                  Reg no:  11707830
                  Phone No:7893945033'''
        Sandeep='''    Name:Sandeep Kumar
                   Email-id:sandeep123@gmail.com
                   Reg no  : 11754565
                   Phone No:8621910294'''
    
        
        
        image_mohit=PhotoImage(file='mohith_image.png')
        ck=Label(image1,image=image_mohit)
        ck.place(x=0,y=200)
        Label(image1,justify=CENTER,text=MOHIT,relief="flat",width=34,height=10,font=("Times New Roman",15),bg="skyblue").place(x=130,y=150)
    
        
        image_chaitanya=PhotoImage(file='chaitanya1.png')
        ck1=Label(image1,image=image_chaitanya)
        ck1.place(x=0,y=0)
        Label(image1,justify=CENTER,text=CHAITANYA,relief="flat",width=34,height=10,font=("Times New Roman",15),bg="skyblue").place(x=130,y=-20)
        
        image_nikhil=PhotoImage(file='nikhil_image.png')
        ck2=Label(image1,image=image_nikhil)
        ck2.place(x=0,y=580)
        Label(image1,justify=CENTER,text=Nikhil,relief="flat",width=34,height=10,font=("Times New Roman",15),bg="skyblue").place(x=130,y=505)
        
        image_sandeep=PhotoImage(file='sandeep_image.png')
        ck3=Label(image1,image=image_sandeep)
        ck3.place(x=0,y=380)
        Label(image1,justify=CENTER,text=Sandeep,relief="flat",width=34,height=10,font=("Times New Roman",15),bg="skyblue").place(x=130,y=325)
        
        image1.mainloop()
    
    
    back()

       

   

import pandas as pd
window=0
Home()
   

