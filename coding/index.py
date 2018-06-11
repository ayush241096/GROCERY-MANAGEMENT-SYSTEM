from tkinter import *
from sqlite3 import dbapi2 as sqlite
from PIL import ImageTk, Image
from tkinter import ttk

login=sqlite.connect("grocery.sqlite")
l=login.cursor()
WinStat = ''


def stock():
    
    application.destroy()
    
    login.close()
    
    import stockdetails
    a = stockdetails.stock()
    
    open_win()

def dailyincome():
    
    application.destroy()
    
    login.close()
    
    import billingdetails
    a = billingdetails.dailyincome()
    
    open_win()    
    
def billingitems():
    
    application.destroy()
    
    login.close()
    
    import billingdetails
    a = billingdetails.billingitems()
    
    open_win()
    
def delstock():
    
    application.destroy()
    login.close()
    
    import stockdetails
    a = stockdetails.deletestock()
    
    open_win()
    
def updatestock():
    
    application.destroy()
    login.close()
    
    import stockdetails
    a = stockdetails.updatestock()
    
    open_win()
    
def expirycheck():
    
    application.destroy()
    login.close()
    
    import expirycheck
    a = expirycheck.expiry()
    
    open_win()


def create_account():
    root.destroy()
    
    ''' Opens Create Window '''
    global create_window, WinStat, un, pwd, question_var, ans
    WinStat='create_window'
    create_window=Tk()
    create_window.configure(background="#a1dbcd")
    img = ImageTk.PhotoImage(Image.open('front.jpg'))
    panel = Label(create_window, image = img).grid(row=0, column=0,columnspan=5)
   
    Label(create_window,text='Enter Details to Create New Account',background="#a1dbcd").grid(row=1,column=0,columnspan=5)
    Label(create_window,text='--------------------------------------------------------------',background="#a1dbcd").grid(row=3,column=0,columnspan=5)
    Label(create_window, text='Username',background="#a1dbcd").grid(row=4, column=1)
    un=Entry(create_window,width=10)
    un.grid(row=4, column=2)
    Label(create_window, text='Password',background="#a1dbcd").grid(row=5, column=1)
    pwd=Entry(create_window,width=10, show="*")
    pwd.grid(row=5, column=2)
    
    question_var = StringVar()
    choices = {'Who is your fav. teacher ?','Who is your first crush ?','Where is your birth mark ?','What is her name ?'}
    question_var.set('Who is your fav. teacher ?') # set the default option 
    question = OptionMenu(create_window, question_var, *choices)
    Label(create_window, text="Choose a dish", background="#a1dbcd").grid(row = 6, column = 1)
    question.grid(row = 6, column =2)
    
	
    Label(create_window, text='Answer',background="#a1dbcd").grid(row=8, column=1)
    ans=Entry(create_window,width=10)
    ans.grid(row=8, column=2)
    Label(create_window,text='',background="#a1dbcd").grid(row=9,column=0,columnspan=5)
    Button(create_window,text='Create Account',command=signup).grid(row=10, column=1)
    Button(create_window,width=6,text='Close',command=create_window.destroy).grid(row=10, column=2)
    Label(create_window,text='--------------------------------------------------------------',background="#a1dbcd").grid(row=11,column=0,columnspan=5)
    Label(create_window,text='Have Account',background="#a1dbcd").grid(row=12,column=0,columnspan=2)
    Button(create_window,text=' Login Here',command=again).grid(row=12,column=2)
    Label(create_window,text='--------------------------------------------------------------',background="#a1dbcd").grid(row=13,column=0,columnspan=5)
    
        
    create_window.mainloop()

def signup():
    u=un.get()
    p=pwd.get()
    q=question_var.get()
    a=ans.get()
    result = False
    if u=="" or p=="" or q=="" or a=="":
        top=Tk()
        Label(top,width=30, text='Please Fill All Deatils').grid(row=0, column=0)
        top.mainloop()
    else:
        try:
            sql="insert into user values('%s','%s','%s','%s')" % (u,p,q,a)
            l.execute(sql)
            login.commit()
            result = True
        except:
            result = False

    if result:
        top=Tk()
        Label(top,width=30, text='ACCOUNT CREATED').grid(row=0, column=0)
        top.mainloop()
    else:
        top=Tk()
        Label(top,width=30, text='ACCOUNT CANN\'T CREATED\n Username already exist').grid(row=0, column=0)
        top.mainloop()

def forgot_pass():
    root.destroy()
    
    ''' Opens Create Window '''
    global forgot_window, WinStat, un, question_var, ans
    WinStat='forgot_window'
    forgot_window=Tk()
    forgot_window.configure(background="#a1dbcd")
    img = ImageTk.PhotoImage(Image.open('front.jpg'))
    panel = Label(forgot_window, image = img).grid(row=0, column=0,columnspan=5)
   
    Label(forgot_window,text='Enter Details to Get Your Password',background="#a1dbcd").grid(row=1,column=0,columnspan=5)
    Label(forgot_window,text='--------------------------------------------------------------',background="#a1dbcd").grid(row=3,column=0,columnspan=5)
    Label(forgot_window, text='Username',background="#a1dbcd").grid(row=4, column=1)
    un=Entry(forgot_window,width=10)
    un.grid(row=4, column=2)
    
    question_var = StringVar()
    choices = {'Who is your fav. teacher ?','Who is your first crush ?','Where is your birth mark ?','What is her name ?'}
    question_var.set('Who is your fav. teacher ?') # set the default option 
    question = OptionMenu(forgot_window, question_var, *choices)
    Label(forgot_window, text="Choose a dish", background="#a1dbcd").grid(row = 6, column = 1)
    question.grid(row = 6, column =2)
    
	
    Label(forgot_window, text='Answer',background="#a1dbcd").grid(row=8, column=1)
    ans=Entry(forgot_window,width=10)
    ans.grid(row=8, column=2)
    Label(forgot_window,text='',background="#a1dbcd").grid(row=9,column=0,columnspan=5)
    Button(forgot_window,text='Recover Password',command=get_pass).grid(row=10, column=1)
    Button(forgot_window,width=6,text='Close',command=forgot_window.destroy).grid(row=10, column=2)
    Label(forgot_window,text='--------------------------------------------------------------',background="#a1dbcd").grid(row=11,column=0,columnspan=5)
    Label(forgot_window,text='Have Account',background="#a1dbcd").grid(row=12,column=0,columnspan=2)
    Button(forgot_window,text=' Login Here',command=again).grid(row=12,column=2)
    Label(forgot_window,text='--------------------------------------------------------------',background="#a1dbcd").grid(row=13,column=0,columnspan=5)
    
        
    forgot_window.mainloop()

def get_pass():
    global un, pwd, root,question_var, ans
    u=un.get()
    q=question_var.get()
    a=ans.get()
    password = ""
    if u=="" or  q=="" or a=="":
        top=Tk()
        Label(top,width=30, text='Please Fill All Deatils').grid(row=0, column=0)
        top.mainloop()
    else:
        try:
            sql="select * from user where username='%s' and question='%s' and answer='%s'" % (u,q,a)
            l.execute(sql)
        except:
            print("")
        count = 0	
        for i in l:  
            password = i[1]		
        if password!="":
            top=Tk()
            Label(top,width=30, text="Your password is "+password).grid(row=0, column=0)
            top.mainloop()
        else:
            top=Tk()
            Label(top,width=30, text='Wrong Information').grid(row=0, column=0)
            top.mainloop()

	
def again():   
    ''' Main Login Window'''
    global un, pwd, WinStat, root, application,create_window,forgot_window
    if WinStat=='application':
        application.destroy()
    elif WinStat=='create_window':
        create_window.destroy()
    elif WinStat=='forgot_window':
        forgot_window.destroy()
    root=Tk()
    root.title('GROCERY MANAGEMENT SYSTEM')
    #root.wm_iconbitmap('favicon.ico')
    root.configure(background="#a1dbcd")
    img = ImageTk.PhotoImage(Image.open('front.jpg'))
    panel = Label(root, image = img).grid(row=0, column=0,columnspan=5)
   
    Label(root,text='Enter Details to Login',background="#a1dbcd").grid(row=1,column=0,columnspan=5)
    Label(root,text='--------------------------------------------------------------',background="#a1dbcd").grid(row=3,column=0,columnspan=5)
    Label(root, text='Username',background="#a1dbcd").grid(row=4, column=1)
    un=Entry(root,width=10)
    un.grid(row=4, column=2)
    Label(root, text='Password',background="#a1dbcd").grid(row=5, column=1)
    pwd=Entry(root,width=10, show="*")
    pwd.grid(row=5, column=2)
    Label(root,text='',background="#a1dbcd").grid(row=6,column=0,columnspan=5)
    Button(root,width=6,text='Login',command=check).grid(row=7, column=1)
    Button(root,width=6,text='Close',command=root.destroy).grid(row=7, column=2)
    Label(root,text='--------------------------------------------------------------',background="#a1dbcd").grid(row=8,column=0,columnspan=5)
    Button(root,text='Forgot Password',command=forgot_pass).grid(row=9,column=0,columnspan=4)
    Label(root,text='--------------------------------------------------------------',background="#a1dbcd").grid(row=10,column=0,columnspan=5)
    Button(root,text='Create New Account',command=create_account).grid(row=11,column=0,columnspan=4)
    Label(root,text='--------------------------------------------------------------',background="#a1dbcd").grid(row=12,column=0,columnspan=5)
    
    root.mainloop()
    
def check():   
    ''' Check Button for Login Window '''
    global un, pwd, root
    u=un.get()
    p=pwd.get()
    
    if u=="" or p=="":
        top=Tk()
        Label(top,width=30, text='Please Fill All Deatils').grid(row=0, column=0)
        top.mainloop()
    else:
        try:
            sql="select * from user where username='%s' and password='%s'" % (u,p)
            l.execute(sql)
        except:
            print("")
        count = 0
        for i in l:
            count+=1		
        if count>0:
            root.destroy()
            open_win()
        else:
            top=Tk()
            Label(top,width=30, text='Wrong username and password').grid(row=0, column=0)
            top.mainloop()
	
	
	
def check_db():
    
    try:
        table1 = l.execute('CREATE TABLE IF NOT EXISTS "bill" ("cusname" TEXT,"cusaddress" TEXT,"items" TEXT,"totalcost" TEXT,"billingdate" TEXT,"billno" TEXT,"bill" TEXT)')
        table2 = l.execute('CREATE TABLE IF NOT EXISTS "customer" ("name" TEXT,"address" TEXT);')
        table3 = l.execute('CREATE TABLE IF NOT EXISTS grocerylist ("Item_No" MEDIUMINT,"Item_Name" VARCHAR(255) DEFAULT "NULL","Item_Type" VARCHAR(255) DEFAULT "NULL","Quantity_Remain" TEXT DEFAULT "NULL","Item_Cost" VARCHAR(100) DEFAULT "NULL","Expiry_Date" VARCHAR(255),"Manufactured_By" VARCHAR(255) DEFAULT "NULL");')
        table4 = l.execute('CREATE TABLE IF NOT EXISTS user(username varchar(50) not null primary key,password varchar(50) not null,question varchar(50) not null,answer varchar(50) not null);')
        print("Database created successfully or already exist")
        login.commit()
        
    except:
        print("Cann able to create database")	
        
   
    
        
    

def open_win(): 
    ''' Opens Main Window '''
    global application, WinStat
    WinStat='application'
    application=Tk()
    #application.wm_iconbitmap('favicon.ico')
    
  
    application.title("Grocery Management System")
    application.geometry("800x400")
    
    ''' Main Window Picture '''
    img = ImageTk.PhotoImage(Image.open('collage.jpg'))
    panel = Label(application, image = img).grid(row=0, column=0,columnspan=5)
    
   

    
    menu_bar = Menu(application)
    stock_menu = Menu(menu_bar,tearoff=0)
    expiry_menu = Menu(menu_bar,tearoff=0)
    billing_menu = Menu(menu_bar,tearoff=0)
    '''Stock Maintainance'''
    stock_menu.add_command(label="Add Items", command=stock)
    stock_menu.add_command(label="Delete Items", command=delstock)
    stock_menu.add_command(label="Update Items", command=updatestock)
    '''Expiry Check'''
    expiry_menu.add_command(label="Check Expiry", command=expirycheck)
    '''Billing'''
    billing_menu.add_command(label="Billing", command=billingitems)
    billing_menu.add_command(label="Check Today's Income", command=dailyincome)
    
    
    menu_bar.add_cascade(label="Stock", menu=stock_menu)
    menu_bar.add_cascade(label="Expiry", menu=expiry_menu)
    menu_bar.add_cascade(label="Billing", menu=billing_menu)
    menu_bar.add_cascade(label="Logout",command=again)
    application.config(menu=menu_bar)
    
    
    
        
    application.mainloop()

    

    
    
    
check_db()  
again()