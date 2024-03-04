from tkinter import * 
import mysql.connector
from tkinter import messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
import time
from tkinter import BOTH, END, LEFT
import random


current_balance=0.00

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data={'Balance':tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        ################## INITIALIZING PAGES IN CONTAINER #################################
        for F in (StartPage, MenuPage, WithdrawPage,DepositPage,BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

################## START PAGE #################################
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#800020')
        self.controller = controller
        self.controller.title('PESPAY')
        self.controller.state('zoomed')
        #self.controller.iconphoto(False,tk.PhotoImage(file='login_register_screen.png'))

        heading=tk.Label(self,text='PESPAY',font=('orbitron',45,'bold'),foreground='white',background='#800020')
        heading.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#800020').pack()

        password_label=tk.Label(self,text=(f'Welcome {user_display_name} to PESPAY Banking SERVICES'),font=('BatmanForeverAlternate',17),
        bg='#800020',fg='white').pack(pady=10)
        def next_page():
            controller.show_frame('MenuPage')

        entry_button = tk.Button(self,text='Enter',font=('orbitron',12),command=next_page,relief='raised',borderwidth=3,
        width=23,height=3).pack(pady=10)

        def Quit():
            self.controller.destroy()
            main_screen()

        def popup():
            response=messagebox.askyesno('Exit','Do you want to Quit?')

            if response == 1:
                return Quit()
            else:
                return


        quit1 = tk.Button(self,text='Quit',font=('orbitron',12),command=popup,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10)
        
        
        dualtone_label=tk.Label(self, text='',font=('orbitron',13),fg='white',bg='#800020',anchor='n')
        dualtone_label.pack(fill='both',expand='True')

        def changescreen():
            self.controller.destroy()
            main_screen()

        def popup2():
            response=messagebox.askyesno('Exit','Do you want to use another account?')

            if response == 1:
                return changescreen()
            else:
                return

        register_login_screen = tk.Button(dualtone_label,text='Use another account',font=('orbitron',12),command=popup2,relief='raised',
        borderwidth=3,width=23,height=3).pack(pady=10,padx=10,side='bottom',anchor='e')

        ################## BOTTOM FRAME #################################
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3).pack(fill='x',side='bottom')


        def tick():
            current_time=time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)


        time_label=tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        tick()

        credits=tk.Label(bottom_frame,text='Created and Developed by GOKUL M AND TEAM',font=('orbitron',15)).pack()



################## MENU PAGE #################################
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#800020')
        self.controller = controller

        heading=tk.Label(self,text='PESPAY BANKING SERVICES',font=('orbitron',45,'bold'),foreground='white',background='#800020')
        heading.pack(pady=25)
        main_menu_label=tk.Label(self,text='Main Menu',font=('orbitron',13),fg='white',bg='#800020')
        main_menu_label.pack(pady=5)
        slection_label=tk.Label(self,text='WHAT DO YOU WANT TO DO?',font=('orbitron',13),fg='white',bg='#800020')
        slection_label.pack(fill='x',pady=5)

        button_frame=tk.Frame(self,bg='#800020')
        button_frame.pack(fill='both',expand='True')

        def withdraw():
            controller.show_frame('WithdrawPage')

        withdraw_button=tk.Button(button_frame,text='Withdraw',font=('orbitron',13),command=withdraw,relief='raised',borderwidth=3,
        width=30,height=4)
        withdraw_button.grid(row=0,column=0,pady=7)

        def deposit():
            controller.show_frame('DepositPage')

        deposit_button=tk.Button(button_frame,text='Deposit',font=('orbitron',13),command=deposit,relief='raised',borderwidth=3,width=30,height=4)
        deposit_button.grid(row=1,column=0,pady=5)

        def balance():
            controller.show_frame('BalancePage')

        balance_button=tk.Button(button_frame,text='Balance',font=('orbitron',13),command=balance,relief='raised',borderwidth=3,width=30,height=4)
        balance_button.grid(row=0,column=1,pady=7,padx=794)

        def exit():
            controller.show_frame('StartPage')

        exit_button=tk.Button(button_frame,text='Exit',font=('orbitron',13),command=exit,relief='raised',borderwidth=3,width=30,height=4)
        exit_button.grid(row=1,column=1,pady=5)

################## WITHDRAW PAGE #################################
class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#800020')
        self.controller = controller

        heading=tk.Label(self,text='PESPAY BANKING SERVICES',font=('orbitron',45,'bold'),foreground='white',background='#800020')
        heading.pack(pady=25)
        choose_amount_label=tk.Label(self,text='Choose the amount you want to withdraw',font=('orbitron',13),fg='white',bg='#800020')
        choose_amount_label.pack()
        button_frame=tk.Frame(self,bg='#800020')
        button_frame.pack(fill='both',expand='True')

        def withdraw(amount):
            global current_balance
            if amount>current_balance:
                messagebox.showwarning('WARNING','Not sufficient funds!')
                other_amount_entry.delete(0,END)
            else:

                current_balance -= amount
                messagebox.showinfo('TRANSACTION','Done Successfully!')
                other_amount_entry.delete(0,END)
                controller.shared_data['Balance'].set(current_balance)
                mydb=mysql.connector.connect(host="localhost",user="root",password="mysqlXgokul")#connects to db
                mycursor=mydb.cursor()
                mycursor.execute("use payrealx")
                mycursor.execute(f"update payrealbank set balance ={current_balance} where accid = {username1} ")
                mydb.commit()

                controller.show_frame('MenuPage')



        fivehundred_button=tk.Button(button_frame,text='Rs 500',font=('orbitron',12),command=lambda:withdraw(500),relief='raised',
        borderwidth=3,width=30,height=4)
        fivehundred_button.grid(row=2,column=0,pady=5)

        onethousand_button=tk.Button(button_frame,text='Rs 1000',font=('orbitron',12),command=lambda:withdraw(1000),relief='raised',
        borderwidth=3,width=30,height=4)
        onethousand_button.grid(row=2,column=3,pady=5,padx=794)

        cash=tk.StringVar()

        other_amount_entry=tk.Entry(button_frame,font=('orbitron',12),textvariable=cash,width=28,justify="left")
        other_amount_entry.grid(row=4,column=2,pady=4,ipady=30)

        other_amount_heading=tk.Button(button_frame,text='Other amount in RUPEES',font=('orbitron',13),borderwidth=0,relief='sunken',
        activeforeground='white',activebackground='#33334d',bg='#33334d',fg='white')
        other_amount_heading.grid(row=5,column=2)

        def other_amount(_):
            global current_balance
            try:
                val=int(cash.get())

                if int(cash.get())>current_balance:
                    messagebox.showwarning('WARNING','Not sufficient funds!')
                    other_amount_entry.delete(0,END)
                elif int(cash.get())<0:
                    messagebox.showwarning('WARNING','Invalid Input!')
                    other_amount_entry.delete(0,END)
                else:

                    current_balance -= int(cash.get())
                    controller.shared_data['Balance'].set(current_balance)
                    cash.set('')
                    messagebox.showinfo('TRANSACTION','Done Successfully!')
                    controller.show_frame('MenuPage')
                    mydb=mysql.connector.connect(host="localhost",user="root",password="mysqlXgokul")
                    mycursor=mydb.cursor()
                    mycursor.execute("use payrealx")
                    mycursor.execute(f"update payrealbank set balance ={current_balance} where accid = {username1} ")
                    mydb.commit()

            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')

        other_amount_entry.bind('<Return>',other_amount)

        button_frame=tk.Label(self,bg='#800020')
        button_frame.pack(fill='both')


        def menu():
            controller.show_frame('MenuPage')

        menu_button=tk.Button(button_frame,command=menu,text='Menu',font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        menu_button.pack(pady=10)

################## DEPOSIT PAGE #################################
class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#800020')
        self.controller = controller

        heading=tk.Label(self,text='PESPAY BANKING SERVICES',font=('orbitron',45,'bold'),foreground='white',background='#800020')
        heading.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#800020').pack()

        enter_amount_label=tk.Label(self,text='Enter the amount you want to deposit',font=('orbitron',13),bg='#800020',fg='white').pack(pady=10)

        cash=tk.StringVar()
        deposit_entry=tk.Entry(self,textvariable=cash,font=('orbitron',12),width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            try:
                val=int(cash.get())
                if int(val)<0:
                    messagebox.showwarning('WARNING','Improper Amount Entered!')
                    cash.set('')
                else:
                    current_balance += int(val)
                    messagebox.showinfo('DEPOSITION','Done Successfully!')
                    controller.shared_data['Balance'].set(current_balance)
                    controller.show_frame('MenuPage')
                    cash.set('')
                    mydb=mysql.connector.connect(host="localhost",user="root",password="mysqlXgokul")
                    mycursor=mydb.cursor()
                    mycursor.execute("use payrealx")
                    mycursor.execute(f"update payrealbank set balance ={current_balance} where accid = {username1} ")
                    mydb.commit()

            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')


        enter_button=tk.Button(self,text='Enter',font=('orbitron',13),command=deposit_cash,relief='raised',borderwidth=3,width=23,height=3)
        enter_button.pack(pady=10)

        two_tone_label=tk.Label(self,bg='#800020')
        two_tone_label.pack(fill='both',expand=True)

        button_frame=tk.Label(self,bg='#800020')
        button_frame.pack(fill='both')


        def menu():
            controller.show_frame('MenuPage')

        menu_button=tk.Button(button_frame,command=menu,text='Menu',font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        menu_button.pack(pady=10)


################## BALANCE PAGE #################################
class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#800020')
        self.controller = controller

        heading=tk.Label(self,text='PESPAY BANKING SERVICES',font=('orbitron',45,'bold'),foreground='white',background='#800020')
        heading.pack(pady=25)

        upperframe=tk.Frame(self,bg='#800020')
        upperframe.pack(fill='both',expand='True')

        button_frame=tk.Frame(self,bg='#800020')
        button_frame.pack(fill='both')

        mydb=mysql.connector.connect(host="localhost",user="root",password="mysqlXgokul")
        mycursor=mydb.cursor()
        mycursor.execute("create database if not exists payrealx")
        mycursor.execute("use payrealx")
        mycursor.execute(f"select password from payrealbank where accid = {username1} ")
        pass_code=mycursor.fetchone()
        pass_code_read=''
        for i in pass_code:
            pass_code_read+=i

        name_info = tk.Label(upperframe, text=f'Name : {user_display_name}', font=('orbitron',16),fg='white', bg='#800020')
        name_info.pack(pady=5)

        accid_info = tk.Label(upperframe, text=f'Account No. : {username1}', font=('orbitron',16),fg='white', bg='#800020')
        accid_info.pack(pady=5)

        pin_info = tk.Label(upperframe, text=f'Pin : {pass_code_read}', font=('orbitron',16),fg='white', bg='#800020')
        pin_info.pack(pady=5)

        self.balance_var = tk.StringVar()
        controller.shared_data['Balance'].trace('w', self.on_balance_changed)
        controller.shared_data['Balance'].set(current_balance)

        balance_label = tk.Label(self, text='Balance', font=('orbitron',13),fg='white', bg='#800020', anchor='w')
        balance_label.pack()

        upperframe=tk.Frame(self,bg='#800020')
        upperframe.pack(fill='both',expand='True')

        balance_label = tk.Label(upperframe, textvariable=self.balance_var, font=('orbitron',16),fg='white', bg='#800020', anchor='w')
        balance_label.pack(pady=7)

        button_frame=tk.Label(self,bg='#800020')
        button_frame.pack(fill='both')

        def menu():
            controller.show_frame('MenuPage')

        menu_button=tk.Button(button_frame,command=menu,text='Menu',font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        menu_button.pack(pady=10)

        def exit():
            controller.show_frame('StartPage')

        exit_button=tk.Button(button_frame,text='Exit',command=exit,font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=5)

    def on_balance_changed(self, *args):
        self.balance_var.set('Current Balance: Rs'+str(self.controller.shared_data['Balance'].get()))



################## CLASS DEFINE FUNCTION #################################
def abcd():

        app = SampleApp()
        app.mainloop()

def password_not_recognised():
  messagebox.showwarning('WARNING',('Invalid Password!'))
  screen5.destroy()
  screen2.destroy()
  login()

################## ABOUT SCREEN #################################
def about():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("About")
  screen3.geometry("380x90+750+230")
  screen3.configure(bg='#800020')
  screen3.iconphoto(False,tk.PhotoImage(file='abc.png'))
  Label(screen3,bg='#800020', text = "Created and Developed by GOKUL KRISHNA NANDAN AND DURGA \n ATM INTERFACE ",
  font = ("orbitron", 10,'bold')).pack()

################## WARNING_SCREEN #################################
def user_not_found():
  messagebox.showwarning('WARNING',('No AccountID Found !'))
  screen5.destroy()
  screen2.destroy()
  login()


################### REGISTER USER SCREEN #################################
def register_user():
  global username_info
  username_info = str(rand)
  password_info = password.get()
  name_info     = name.get()

  ################## MYSQL DATABASE ##################
  global mycursor
  mydb=mysql.connector.connect(host="localhost",user="root",password="mysqlXgokul")
  mycursor=mydb.cursor()
  mycursor.execute("create database if not exists payrealx")
  mycursor.execute("use payrealx")
  mycursor.execute("create table if not exists payrealbank(accid int(10) primary key,name varchar(30),password char(20),balance char(30))")
  mydb.commit()

  mycursor.execute('select accid from payrealbank')
  values=mycursor.fetchall()

  b=[]
  for i in values:
      b.append(i[0])
  if username_info in b:
    messagebox.showwarning('WARNING',('AccountID already exists!'))

    password_entry.delete(0,END)
    name_entry.delete(0,END)
  elif name_info=='' :
        messagebox.showwarning('WARNING',('No Name Given!'))
        password_entry.delete(0,END)
  elif password_info=='' :
        messagebox.showwarning('WARNING',('No Password Given!'))
  else:
        balance_inti='0.00'
        password_entry.delete(0, END)
        name_entry.delete(0, END)
        screen1.destroy()
        mycursor.execute("insert into payrealbank values('"+username_info+"','"+name_info+"','"+password_info+"','"+balance_inti+"')")
        mydb.commit()
        messagebox.showinfo('Registration',('Done Successfully!'))




def login_verify():
  global current_balance
  global username1
  global name_display
  global user_display_name
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  mydb=mysql.connector.connect(host="localhost",user="root",password="mysqlXgokul")
  mycursor=mydb.cursor()
  #mycursor.execute("create database if not exists payrealx")
  mycursor.execute("use payrealx")

  mycursor.execute("select accid from payrealbank ")
  values=mycursor.fetchall()
  user_acc=[]
  for i in values:
    user_acc.append(i[0])

  if username1.isalpha():
        messagebox.showwarning('WARNING',('Wrong Input!'))
        username_entry1.delete(0, END)
        password_entry1.delete(0,END)

  elif str(username1)=='':
        messagebox.showwarning('WARNING',('No Accound ID Given!'))
        password_entry1.delete(0,END)
  elif str(username1).isspace():
        messagebox.showwarning('WARNING',('No Accound ID Given!'))
        username_entry1.delete(0, END)
        password_entry1.delete(0,END)
  elif username1.isalnum():
      if username1.isdigit():

          if int(username1) in user_acc:

              mycursor.execute(f"select password from payrealbank where accid = {username1} ")
              values=mycursor.fetchall()
              mydb.commit()
              user_pass=[]
              for i in values:
                  user_pass.append(i[0])

              user_pass_1=str(user_pass[0])

              if password1=='':
                  messagebox.showwarning('WARNING',('No Password Given!'))
                  username_entry1.delete(0, END)
                  password_entry1.delete(0,END)
              elif password1 == str(user_pass_1) :
                  mycursor.execute(f"select name from payrealbank where accid={username1}")
                  values=mycursor.fetchall()
                  user_name=[]
                  for i in values:
                    user_name.append(i[0])
                  user_display_name=str(user_name[0])
                  #login_sucess()
                  mydb=mysql.connector.connect(host="localhost",user="root",password="mysqlXgokul")
                  mycursor=mydb.cursor()
                  #mycursor.execute("create database if not exists payrealx")
                  mycursor.execute("use payrealx")

                  mycursor.execute(f'select balance from payrealbank where accid ={username1}')
                  values=mycursor.fetchall()
                  user_balance=[]
                  for i in values:
                    user_balance.append(i[0])
                  user_balance_1=float(user_balance[0])
                  current_balance=user_balance_1

                  screen2.destroy()
                  screen.destroy()
                  abcd()
              elif password1!= str(user_pass_1):
                  password_not_recognised()
          else:
              user_not_found()
              
      else:
          user_not_found()

  else:
        user_not_found()
        

################## REGISTER DISPLAY SCREEN #################################
def register():
  global screen1
  global password_entry
  global username_entry
  global rand
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("380x470+750+230")
  screen1.configure(bg='#800020')
  screen1.iconphoto(False,tk.PhotoImage(file='C:/Users/Gokul/Documents/abc.png'))

  photo = PhotoImage(file="C:/Users/Gokul/Documents/login_person.png")
  label = Label(screen1,image=photo,bg='#800020')
  label.image = photo
  label.pack(pady=5)

  global username
  global password
  global name

  global username_entry
  global password_entry
  global name_entry

  username = StringVar()
  password = StringVar()
  name     = StringVar()

  Label(screen1, text = "Please enter details below to register",bg='#800020',font = ("orbitron", 10)).pack()

  Label(screen1, text = "",bg='#800020').pack()
  Label(screen1, text = "Name",font = ("orbitron", 10),bg='#800020').pack()
  name_entry = Entry(screen1,font = ("orbitron",10), textvariable = name)
  name_entry.pack()

  Label(screen1, text = "Account No.",font = ("orbitron", 10),bg='#800020').pack()
  rand=random.randint(1,100000)
  username=Label(screen1, text = rand,font = ("orbitron", 11),bg='#800020').pack()
  #username_entry = Entry(screen1, textvariable = username)
  #username_entry.pack()

  Label(screen1, text = "Pin",font = ("orbitron", 10),bg='#800020').pack()
  password_entry =  Entry(screen1,font = ("orbitron",10), textvariable = password)
  password_entry.config(fg='black',show='●')
  password_entry.pack()

  Label(screen1, text = "",bg='lightblue').pack()

  img1 = PhotoImage(file="C:/Users/Gokul/Documents/register_final.png")
  photoimage1 = img1.subsample(3, 3)
  img1Btn = Button(screen1,command = register_user,image=photoimage1,bg='#800020',activebackground='#800020',relief=FLAT)
  img1Btn.image = photoimage1
  img1Btn.pack()




def login():
  global screen2
  screen2 = Toplevel(screen) 
  screen2.title("Login")
  screen2.geometry("380x470+750+230")
  screen2.configure(bg='#800020')
  screen2.iconphoto(False,tk.PhotoImage(file='C:/Users/Gokul/Documents/abc.png'))

  photo = PhotoImage(file="C:/Users/Gokul/Documents/login_person_new.png")
  label = Label(screen2,image=photo,bg='#800020')
  label.image = photo
  label.pack(pady=5)

  Label(screen2, text = "Please enter details below to login",bg='#800020',font = ("orbitron", 10)).pack()
  #Label(screen2, text = "",bg='lightblue').pack()

  global username_verify
  #global password_verify

  username_verify = StringVar()
  #password_verify = StringVar()


  global username_entry1
  #global password_entry1

  Label(screen2, text = "Account No.",bg='#800020',font = ("orbitron", 10)).pack()
  username_entry1 = Entry(screen2,font = ("orbitron",10) ,textvariable = username_verify)
  username_entry1.pack()

  Label(screen2, text = "",bg='#800020').pack()

  Label(screen2, text = "",bg='#800020').pack()


  img1 = PhotoImage(file="C:/Users/Gokul/Documents/login_final_new.png")
  photoimage1 = img1.subsample(3, 3)
  img1Btn = Button(screen2,command = login_pass,image=photoimage1,bg='#800020',activebackground='lightblue',relief=FLAT)
  img1Btn.image = photoimage1
  img1Btn.pack()



  return username_entry1


def login_pass():
    global screen5
    global username_entry9
    screen5=Toplevel(screen2)
    screen5.geometry("380x470+750+230")
    screen5.configure(bg='#800020')
    
    photo = PhotoImage(file="C:/Users/Gokul/Documents/login_person_new.png")
    label = Label(screen5,image=photo,bg='#800020')
    label.image = photo
    label.pack(pady=5)

    Label(screen5, text = "Please enter details below to login",bg='#800020',font = ("orbitron", 10)).pack()

    global password_verify
    password_verify = StringVar()

    global password_entry1
    Label(screen5, text = "pin.",bg='#800020',font = ("orbitron", 10)).pack()
    password_entry1 = Entry(screen5,font = ("orbitron",10) ,textvariable = password_verify)
    password_entry1.config(fg='black',show='●')
    password_entry1.pack()

    
    img1 = PhotoImage(file="C:/Users/Gokul/Documents/login_final_new.png")
    photoimage1 = img1.subsample(3, 3)
    img1Btn = Button(screen5,command = login_verify,image=photoimage1,bg='#800020',activebackground='#800020',relief=FLAT)
    img1Btn.image = photoimage1
    img1Btn.pack()


def main_screen():
  global screen
  screen = Tk()
  screen.geometry("530x530+450+120")
  screen.title("PesPay")
  screen.configure(bg='#800020')
  screen.iconphoto(False,tk.PhotoImage(file='C:/Users/Gokul/Documents/pes_logo.png'))


  Label(text = "PESPAY",fg='white', bg = "#800020", width = "300", height = "2", font = ("Droid Sans Mono", 25,)).pack()
  Label(text = "MAKES YOUR BANKING EASIER",fg='white', bg = "navy blue", width = "300", height = "1", font = ("Droid Sans Mono", 15)).pack()

  img = ImageTk.PhotoImage(Image.open("C:/Users/Gokul/Documents/pes_logo.png"))
  panel = Label(screen, image = img,bg='#800020')
  panel.pack()

  photo1 = PhotoImage(file="C:/Users/Gokul/Documents/login_final_new.png")
  photoimage1 = photo1.subsample(2, 2)
  Button(command = login,bg='#800020',activebackground='#800020',relief=FLAT,image=photoimage1).pack(pady=5)


  menu1=Menu(screen)
  menu1.add_command(label="REGISTER",command=register)
  menu1.add_command(label="ABOUT",command=about)
  screen.config(menu=menu1)

  screen.mainloop()

main_screen()