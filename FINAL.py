
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("Student Attendance SYSTEM")
root.geometry("560x550")
root.configure(bg="#ac05f5")

USERNAME=StringVar()
PASSWORD=StringVar()
FIRSTNAME=StringVar()
LASTNAME=StringVar()

STUDENTNAME=StringVar()
REGNO=StringVar()
VAR=IntVar()

#=======================Creating Table for LOGIN and REGISTER============================================ 
def database():
    global conn,cursor
    conn=sqlite3.connect("db_member3.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS member(mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,username TEXT,password TEXT,firstname TEXT,lastname TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS student(std_no INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,studentname TEXT,regno TEXT,var TEXT)")


def Exit():
    result=messagebox.askquestion("SYSTEM","Are you sure you want to exit..?",icon="warning")
    if result=="yes":
        root.destroy()
        exit()

def loginform():

    #=======================CREATING FRAMES===============================
    global loginframe,label_print1
    loginframe=Frame(root,bg="#ac05f5")
    loginframe.grid()

    headframe1=Frame(loginframe,width=1600,height=50,bg="#e7cef2")
    headframe1.pack(side=TOP)
    labeltitle1=Label(headframe1,font=('arial',40,'bold'),text="Attendance SYSTEM",bd=10,bg="#ac05f5",relief=RAISED)
    labeltitle1.grid()

    bodyframe1=Frame(loginframe,bd=2,width=1300,height=500,
                             padx=30,pady=20,bg="#a7b9db",
                             relief=RIDGE)  
    bodyframe1.pack(side=BOTTOM)
    
    #======================Creating Labels and entry boxes===================================

    label_username=Label(bodyframe1,bd=2,text=" Username ",font=("Arial Bold",15),fg="#255b9c",bg="white")
    label_username.grid(row=0,column=0,padx=20,pady=10) 

    label_password=Label(bodyframe1,bd=2,text=" Password ",font=("Arial Bold",15),fg="#255b9c",bg="white")
    label_password.grid(row=1,column=0,padx=20,pady=10) 

    entry_username=Entry(bodyframe1,width=35,textvariable=USERNAME)
    entry_username.grid(column=1,row=0,sticky=W)

    entry_password=Entry(bodyframe1,show="*",width=35,textvariable=PASSWORD)
    entry_password.grid(column=1,row=1,sticky=W)

    label_print1=Label(bodyframe1,bd=2,text="",font=("Arial Bold",15),bg="#a7b9db",fg="BROWN")
    label_print1.grid(row=4,column=1)

    button_login=Button(bodyframe1,text="LOGIN",bg="#00e2ff",width=30,bd=3,padx=5,pady=5,font=("Arial Bold",13),command=log_button)
    button_login.grid(row=3,column=0,padx=30,pady=20,sticky=S,columnspan=2)

    label_register=Label(bodyframe1,bd=2,text=" CREATE ACCOUNT ",font=("Arial Bold",10),fg="RED",bg="white")
    label_register.grid(row=2,column=0,padx=20,pady=20,columnspan=2) 
    label_register.bind('<Button-1>', ToggleToRegister)


def registerform():
    #=======================CREATING FRAMES===============================

    global registerframe,label_print2
    registerframe=Frame(root,bg="#ac05f5")
    registerframe.grid()

    headframe2=Frame(registerframe,width=1600,height=50,bg="#e7cef2")
    headframe2.grid()
    labeltitle2=Label(headframe2,font=('arial',40,'bold'),text="Attendance SYSTEM",bd=10,bg="#ac05f5",relief=RAISED)
    labeltitle2.grid()

    bodyframe2=Frame(registerframe,bd=2,width=1300,height=500,
                             padx=30,pady=20,bg="#a7b9db",
                             relief=RIDGE)  
    bodyframe2.grid(sticky=S)
    #======================Creating Labels and entry boxes===================================

    label_username=Label(bodyframe2,bd=2,text=" Username ",font=("Arial Bold",15),fg="#255b9c",bg="white")
    label_username.grid(row=2,column=0,padx=20,pady=10) 

    entry_username=Entry(bodyframe2,width=35,textvariable=USERNAME)
    entry_username.grid(column=1,row=2,sticky=W)
    
    label_password=Label(bodyframe2,bd=2,text=" Password ",font=("Arial Bold",15),fg="#255b9c",bg="white")
    label_password.grid(row=3,column=0,padx=20,pady=10) 

    entry_password=Entry(bodyframe2,show="*",width=35,textvariable=PASSWORD)
    entry_password.grid(column=1,row=3,sticky=W)

    label_firstname=Label(bodyframe2,bd=2,text=" Firstname ",font=("Arial Bold",15),fg="#255b9c",bg="white")
    label_firstname.grid(row=0,column=0,padx=20,pady=10) 
    
    entry_firstname=Entry(bodyframe2,width=35,textvariable=FIRSTNAME)
    entry_firstname.grid(column=1,row=0,sticky=W)
     
    label_lastname=Label(bodyframe2,bd=2,text=" Lastname ",font=("Arial Bold",15),fg="#255b9c",bg="white")
    label_lastname.grid(row=1,column=0,padx=20,pady=10) 

    entry_lastname=Entry(bodyframe2,width=35,textvariable=LASTNAME)
    entry_lastname.grid(column=1,row=1,sticky=W)    
    
    label_print2=Label(bodyframe2,bd=2,text="",font=("Arial Bold",15),fg="BROWN",bg="#a7b9db")
    label_print2.grid(row=6,column=1)
    
    button_login=Button(bodyframe2,text="CREATE ACCOUNT",bg="#00e2ff",width=30,bd=3,padx=5,pady=5,font=("Arial Bold",13),command=reg_button)
    button_login.grid(row=4,column=0,padx=10,pady=10,sticky=S,columnspan=2)

    label_login=Label(bodyframe2,bd=2,text=" Go Back to LOGIN FORM ",font=("Arial Bold",10),fg="RED",bg="white")
    label_login.grid(row=5,column=0,padx=20,pady=20,columnspan=2) 
    label_login.bind('<Button-1>', ToggleToLogin)


#==========================Function to travel between LOGIN and REGISTER Forms================================================
def ToggleToLogin(event=None):
    registerframe.destroy()
    loginform()

def ToggleToRegister(event=None):
    loginframe.destroy()
    registerform()


def reg_button():
    database()
    if USERNAME.get=="" or PASSWORD.get==" " or FIRSTNAME.get=="" or LASTNAME.get=="":
        label_print2.config(text="Please complete the required fields!")
    else:
        cursor.execute("SELECT * FROM member WHERE username = ?",(USERNAME.get(),))
        if cursor.fetchone() is not None:
            label_print2.config(text=" USERNAME already Taken !")
        else:
            cursor.execute("INSERT INTO member (username,password,firstname,lastname) VALUES(?, ?, ?, ?)",(str(USERNAME.get()),str(PASSWORD.get()),str(FIRSTNAME.get()),str(LASTNAME.get())))
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            FIRSTNAME.set("")
            LASTNAME.set("") 
            label_print2.config(text="Successfully Created")
            cursor.close()
            conn.close()

def log_button():
    database()
    if USERNAME.get=="" or PASSWORD.get=="":
        label_print1.config(text="Please COMPLETE the required field")
    else:
        cursor.execute("SELECT * FROM member WHERE username = ? and password = ?",(USERNAME.get(),PASSWORD.get()))
        if cursor.fetchone() is not None:
            messagebox.askokcancel("LOGIN","Successfully LOGGED IN, Now you may close the Whole WIndow")

        else:
            label_print1.config(text="Wrong Credential")    
    
    USERNAME.set("")
    PASSWORD.set("")
loginform()

#if __name__=='__main__':
root.mainloop()

#=====================================CLASS for Front End UI======================================================

class stddatabase:
    #Self : The self in keyword in Python is used to all the instances in a class. 
    #by using the self keyword, one can easily access all the instances defined within a class, including its methods and attributes.
    def __init__(self,root):
        #__init__ is one of the reserved methods in Python. In object oriented programming, it is known as a constructor. 
        # The __init__ method can be called when an object is created from the class, and access is required to initialize the attributes of the class.
        #==========================Create object rederence instance of database class as p========================
        p=Database()
        p.conn()

        self.root=root
        self.root.title("Student DATABASE")
        self.root.geometry("1220x520")
        self.root.configure(bg="#cce3ed")
        
        std_id=StringVar()
        std_date=StringVar()
        std_name=StringVar()
        std_course=StringVar()
        std_batch=StringVar()
        std_attendance=StringVar() 

        ''' Lets call database methods to perform OPERATIONS'''
        #=====================function to close the frame=====================
        def close():
            print("Student : close method called")
            close=messagebox.askyesno("Student MANAGEMENT System","Are you sure...?")
            if close>0:
                root.destroy()
                print("Student : close method finished")
                return
        #function to clear the entry fields
        def clear():
            print("Student : clear method called")
            self.entry_date.delete(0,END)
            self.entry_id.delete(0,END)
            self.entry_name.delete(0,END)
            self.entry_course.delete(0,END)
            self.entry_batch.delete(0,END)
            self.entry_attendance.delete(0,END)
            stdlist.delete(0,END)
            print("Student : clear method Finished")

        #function to save product details in Database table
        def insert():
            print("Student : insert method called")
            if(len(std_id.get())!=0):
                p.insert(std_id.get(),std_date.get(),std_name.get(),std_course.get(),std_batch.get(),std_attendance.get())
                stdlist.delete(0,END)
                stdlist.insert(END,std_id.get(),std_date.get(),std_name.get(),std_course.get(),std_batch.get(),std_attendance.get())
                Showlist() #called showlist method 
                #after inserting data into the database table
            else:
                messagebox.askyesno("Student Attendance System","Really...ENter Std ID")
            print("Student : insert method Finished \n")
        
        #function responsible to show student table data to scroll student list
        
        def Showlist():
            print("Student : Show method called")
            stdlist.delete(0,END)
            for row in p.show():
                stdlist.insert(END,row,str(""))
            print("Student : Show method Finished \n")

        def stdrec(event): 
            print("Student : StudentRecordSHow method called")
            global pd 

            searchpd=stdlist.curselection()[0]
            pd=stdlist.get(searchpd)
            self.entry_id.delete(0,END)
            self.entry_id.insert(END,pd[0])
            self.entry_date.delete(0,END)
            self.entry_date.insert(END,pd[1])
            self.entry_name.delete(0,END)
            self.entry_name.insert(END,pd[2])
            self.entry_course.delete(0,END)
            self.entry_course.insert(END,pd[3])
            self.entry_batch.delete(0,END)
            self.entry_batch.insert(END,pd[4])
            self.entry_attendance.delete(0,END)
            self.entry_attendance.insert(END,pd[5])
        
            print("Student : StudentRecordSHow method Finished \n")

        #function to delete the record from the database table
        def delete():
            print("Student : delete method called")
            if(len(std_id.get())!=0):
                p.delete(pd[0])
                clear()
                Showlist()
                '''
                p.insert(std_id.get(),std_date.get(),std_name.get(),std_course.get(),std_batch.get(),std_attendance.get())
                stdlist.delete(0,END)
                stdlist.insert(END,std_id.get(),std_date.get(),std_name.get(),std_course.get(),std_batch.get(),std_attendance.get())
                '''
            print("Student : delete method Finished \n")
        
        #Search the record from the database

        def search():
            print("Student : Search method called")
            stdlist.delete(0,END)
            for row in p.search(std_id.get(),std_date.get(),std_name.get(),std_course.get(),std_batch.get(),std_attendance.get()):
                stdlist.insert(END,row,str(""))
            
            print("Student : Search method Finished \n")
    
        ''''CREATE THE FRAMES'''
        
        global mainframe
        mainframe=Frame(self.root,bg="#cce3ed")
        mainframe.grid()

        headframe = Frame(mainframe,bd=2,padx=30,pady=10,
                          bg="#b49de3",relief=RIDGE)
        headframe.pack(side=TOP)
        self.label1=Label(headframe,font=("Arial Bold",40),
                         text=' STUDENT MANAGEMENT ',bg='#96d9d4')
        self.label1.grid() 
        
        #creating Operation frame
        operationframe=Frame(mainframe,bd=3,width=1300,height=120,
                             padx=50,pady=20,bg="#97afdb",
                             relief=RIDGE)   
        operationframe.pack(side=RIGHT) 

        #creating Body Frame      
        bodyframe=Frame(mainframe,bd=2,width=1300,height=500,
                             padx=30,pady=20,bg="#a7b9db",
                             relief=RIDGE)  
        bodyframe.pack(side=BOTTOM)

        leftbodyframe=LabelFrame(bodyframe,bd=3,width=650,height=250,
                             padx=20,pady=10,bg="#a490d6",
                             relief=RIDGE,font=("Arial Bold",15),
                             text="STUDENT DETAILS")
        leftbodyframe.pack(side=LEFT)

        rightbodyframe=LabelFrame(bodyframe,bd=3,width=350,height=250,
                             padx=20,pady=10,bg="#a490d6",
                             relief=RIDGE,font=("Arial Bold",15),
                             text="STUDENT INFORMATION")
        rightbodyframe.pack(side=RIGHT)    

        '''Add WIDGETS to LEFT BODY FRAME'''

        self.label_id=Label(leftbodyframe,bd=2,text="Student ID",
                            font=("Arial Bold",12),padx=2,
                            fg="#255b9c",bg="white")
        self.label_id.grid(row=0,column=0,sticky=W) 

        self.entry_id=Entry(leftbodyframe,width=30,font=("Arial Bold",12),textvariable=std_id)                                                                      
        self.entry_id.grid(column=1,row=0,sticky=W,padx=10)

        self.label_date=Label(leftbodyframe,bd=2,text="DATE",
                            font=("Arial Bold",12),padx=2,
                            fg="#255b9c",bg="white")
        self.label_date.grid(row=1,column=0,pady=10,sticky=W) 

        self.entry_date=Entry(leftbodyframe,width=30,font=("Arial Bold",12),textvariable=std_date)                                                                      
        self.entry_date.grid(column=1,row=1,sticky=W,padx=10)
        
        self.label_name=Label(leftbodyframe,bd=2,text="Student NAME",
                            font=("Arial Bold",12),padx=2,
                            fg="#255b9c",bg="white")
        self.label_name.grid(row=2,column=0,pady=1,sticky=W) 

        self.entry_name=Entry(leftbodyframe,width=30,font=("Arial Bold",12),textvariable=std_name)                                                                      
        self.entry_name.grid(column=1,row=2,sticky=W,padx=10)

        self.label_course=Label(leftbodyframe,bd=2,text=" Course",
                            font=("Arial Bold",12),padx=2,
                            fg="#255b9c",bg="white")
        self.label_course.grid(row=3,column=0,pady=10,sticky=W) 

        self.entry_course=Entry(leftbodyframe,width=30,font=("Arial Bold",12),textvariable=std_course)                                                                      
        self.entry_course.grid(column=1,row=3,sticky=W,padx=10)
        
        self.label_batch=Label(leftbodyframe,bd=2,text="Batch",
                            font=("Arial Bold",12),padx=2,
                            fg="#255b9c",bg="white")
        self.label_batch.grid(row=4,column=0,pady=10,sticky=W) 

        self.entry_batch=Entry(leftbodyframe,width=30,font=("Arial Bold",12),textvariable=std_batch)                                                                      
        self.entry_batch.grid(column=1,row=4,sticky=W,padx=10)

        self.label_attendance=Label(leftbodyframe,bd=2,text="Attendance",
                            font=("Arial Bold",12),padx=2,
                            fg="#255b9c",bg="white")
        self.label_attendance.grid(row=5,column=0,pady=10,sticky=W) 
       
        self.entry_attendance=Entry(leftbodyframe,width=30,font=("Arial Bold",12),textvariable=std_attendance)                                                                      
        self.entry_attendance.grid(column=1,row=5,sticky=W,padx=10)

        '''Adding Widgets in Right Body Frame'''

        scroll=Scrollbar(rightbodyframe)
        scroll.grid(row=0,column=1,sticky=NS)
        stdlist=Listbox(rightbodyframe,width=40,height=16,font=("Arial Bold",12),
                               yscrollcommand=scroll.set)
        stdlist.bind('<<ListboxSelect>>',stdrec)                       
        stdlist.grid(row=0,column=0,padx=8)  
        scroll.config(command=stdlist.yview) 

        '''Add The Buttons to OPERATION FRAME'''  
        
        self.add_button=Button(operationframe,text="ADD",
                                font=("Arial Bold",12),bg="#00e2ff",
                                width=12,bd=3,command=insert)
        self.add_button.grid(row=0,column=0,pady=10) 

        self.show_button=Button(operationframe,text="Show Data",
                                font=("Arial Bold",12),bg="#00e2ff",
                                width=12,bd=3,command=Showlist)
        self.show_button.grid(row=1,column=0,pady=10)

        self.clear_button=Button(operationframe,text="Clear",
                                font=("Arial Bold",12),bg="#00e2ff",
                                width=12,bd=3,command=clear)
        self.clear_button.grid(row=2,column=0,pady=10)

        self.delete_button=Button(operationframe,text="Delete",
                                font=("Arial Bold",12),bg="#00e2ff",
                                width=12,bd=3,command=delete)
        self.delete_button.grid(row=3,column=0,pady=10)

        self.search_button=Button(operationframe,text="Search",
                                font=("Arial Bold",12),bg="#00e2ff",
                                width=12,bd=3,command=search)
        self.search_button.grid(row=4,column=0,pady=10)

        self.close_button=Button(operationframe,text="Close",
                                font=("Arial Bold",12),bg="#00e2ff",
                                width=12,bd=3,command=close)
        self.close_button.grid(row=6,column=0,pady=10)


#BACKEND DATABASE OPERATIONS

class Database:
    def conn(self):
        print("Database: connection method called") 
        con=sqlite3.connect("information.db")
        cur=con.cursor()
        query="create table if not exists stdinfo(sid integer primary key,date text,name text,course text,batch text,attendance text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database: connection method finished \n")

    def insert(self, sid,date,name,course,batch,attendance):
        print("Database: insert method called") 
        con=sqlite3.connect("information.db")
        cur=con.cursor()
        query="insert into stdinfo values(?,?,?,?,?,?)"
        cur.execute(query,(sid,date,name,course,batch,attendance))
        con.commit()
        con.close()
        print("Database: Insert method finished \n")
    
    def show(self):
        print("Database: SHOW method called") 
        con=sqlite3.connect("information.db")
        cur=con.cursor()
        query="select * from stdinfo"
        cur.execute(query)
        rows=cur.fetchall()
        con.close()
        print("Database: ShOW method finished \n")
        return rows

    def delete(self,sid):    
        print("Database: delete method called",sid) 
        con=sqlite3.connect("information.db")
        cur=con.cursor()
        cur.execute("delete from stdinfo where sid=?",(sid,))
        con.commit()
        con.close()
        print(sid,"Database: Delete method finished \n")

    def search(self,sid="",date="",name="",course="",batch="",attendance=""):
        print("Database: Search method called",sid) 
        con=sqlite3.connect("information.db")
        cur=con.cursor()
        cur.execute("select * from stdinfo where sid=? or date=? or name=? or course=? or batch=? or attendance=?",(sid,date,name,course,batch,attendance))
        row=cur.fetchall()
        con.close()
        print(sid,"Database: Search method finished \n")
        return row

#The __name__ is a special built-in variable which evaluates to the name of the current module. However, 
# if a module is being run directly (from command line), then __name__ instead is set to the string “__main__”.
if __name__=='__main__':
    root=Tk()
    application=stddatabase(root)
    root.mainloop()   

