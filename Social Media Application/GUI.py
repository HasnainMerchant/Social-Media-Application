from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import MAIN

exec('MAIN')

login_name = ''
class Login:


   def __init__(self,root):
      
      self.root=root
      self.root.title("Login and registration system for Apps")
      self.root.geometry("1366x700+0+0")
      self.root.resizable(False,False)
      self.loginform()  

   
      

   def loginform(self):

      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=1366)

      #self.img=ImageTk.PhotoImage(file="background-2.jpg")
      #img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)

      frame_input=Frame(self.root,bg='white')
      frame_input.place(x=320,y=130,height=450,width=350)

      label1=Label(frame_input,text="Login Here",font=('impact',32,'bold'),fg="black",bg='white')
      label1.place(x=75,y=20)

      label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
      label2.place(x=30,y=95)
      self.username_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
      login_name = self.username_txt.get()
      self.username_txt.place(x=30,y=145,width=270,height=35)
     
      label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
      label3.place(x=30,y=195)
      self.password=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray',show = '*')
      self.password.place(x=30,y=245,width=270,height=35)
 
      btn1=Button(frame_input,command=self.update_pwd,text="forgot password?",cursor='hand2',font=('calibri',10),bg='white',fg='black',bd=0)
      btn1.place(x=125,y=305)

      btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn2.place(x=90,y=340)
        
      btn3=Button(frame_input,command=self.Register,text="Not Registered?register",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
      btn3.place(x=110,y=390)



   def login(self):

      if self.username_txt.get()=="" or self.password.get()=="":

         messagebox.showerror("Error","All fields are required",parent=self.root)

      else:

         try:

            con=pymysql.connect(host='localhost',user='root',password='mArvelisthebest@123.',database='dbms_mini_proj')

            cur=con.cursor()

            cur.execute('select * from users where username=%s and password=%s',(self.username_txt.get(),self.password.get()))

            row=cur.fetchone()

            if row==None:

               messagebox.showerror('Error','Invalid Username And Password',parent=self.root)

               self.loginclear()

               self.username_txt.focus()

            else:

               self.appscreen()

               con.close()

         except Exception as es:

            messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)

            

   def Register(self):



      Frame_login1=Frame(self.root,bg="white")
      Frame_login1.place(x=0,y=0,height=700,width=1366)
      
      #self.img=ImageTk.PhotoImage(file="background-2.jpg")
      #img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=1366,height=700)
     
      frame_input2=Frame(self.root,bg='white')
      frame_input2.place(x=320,y=100,height=500,width=700)

      label1=Label(frame_input2,text="Register Here",font=('impact',20,'bold'),fg="black",bg='white')
      label1.place(x=30,y=15)


      #Username
      label2=Label(frame_input2,text="Username",font=("Goudy old style",14,"bold"),fg='orangered',bg='white')
      label2.place(x=30,y=60)
      self.entry=Entry(frame_input2,font=("times new roman",12,"bold"),bg='lightgray')
      self.entry.place(x=30,y=90,width=100,height=20)

      #Mobile
      label3=Label(frame_input2,text="Mobile",font=("Goudy old style",14,"bold"),fg='orangered',bg='white')
      label3.place(x=30,y=120)
      self.entry2=Entry(frame_input2,font=("times new roman",12,"bold"),bg='lightgray')
      self.entry2.place(x=30,y=150,width=100,height=20)

      #Email
      label4=Label(frame_input2,text="Email",font=("Goudy old style",14,"bold"),fg="orangered",bg="white")
      label4.place(x=30,y=180)
      self.entry3=Entry(frame_input2,font=("times new roman",12,"bold"),bg='lightgray')
      self.entry3.place(x=30,y=210,width=100,height=20)
      
      #Password
      label5=Label(frame_input2,text="Password",font=("Goudy old style",14,"bold"),fg="orangered",bg="white")
      label5.place(x=30,y=240)
      self.entry4=Entry(frame_input2,font=("times new roman",12,"bold"),bg='lightgray',show = '*')
      self.entry4.place(x=30,y=270,width=100,height=20)

      #fname
      label6=Label(frame_input2,text="First Name",font=("Goudy old style",14,"bold"),fg="orangered",bg="white")
      label6.place(x=300,y=60)
      self.entry5=Entry(frame_input2,font=("times new roman",12,"bold"),bg='lightgray')
      self.entry5.place(x=300,y=90,width=100,height=20)

      #lname
      label5=Label(frame_input2,text="Last Name",font=("Goudy old style",14,"bold"),fg="orangered",bg="white")
      label5.place(x=300,y=120)
      self.entry6=Entry(frame_input2,font=("times new roman",12,"bold"),bg='lightgray')
      self.entry6.place(x=300,y=150,width=100,height=20)

      #bdate
      label5=Label(frame_input2,text="Birthdate",font=("Goudy old style",14,"bold"),fg="orangered",bg="white")
      label5.place(x=300,y=180)
      self.entry7=Entry(frame_input2,font=("times new roman",12,"bold"),bg='lightgray')
      self.entry7.place(x=300,y=210,width=100,height=20)

      
      #Register
      btn2=Button(frame_input2,command=self.register,text="Register",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn2.place(x=90,y=370)

      #Login
      btn3=Button(frame_input2,command=self.loginform,text="Already Registered?Login",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
      btn3.place(x=110,y=410)





   def register(self):

      if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()==""or self.entry5.get()==""or self.entry6.get()==""or self.entry7.get()=="":

         messagebox.showerror("Error","All Fields Are Required",parent=self.root)


      else:

         try:

            con=pymysql.connect(host="localhost",user="root",password="mArvelisthebest@123.",database="dbms_mini_proj")

            cur=con.cursor()

            cur.execute("select * from users where email=%s",self.entry3.get())

            row=cur.fetchone()

            if row!=None:

               messagebox.showerror("Error","User already Exist,Please try with another Email",parent=self.root)

               self.regclear()

               self.entry.focus()

            else:

               cur.execute("insert into users(username,mobile,email,password,first_Name,last_Name,birthdate,is_active,created_AT) values(%s,%s,%s,%s,%s,%s,%s,1,now())",(self.entry.get(),self.entry2.get(),self.entry3.get(),self.entry4.get(),self.entry5.get(),
                           self.entry6.get(),
                           self.entry7.get()))

               con.commit()
               con.close()
               messagebox.showinfo("Success","Register Succesfull",parent=self.root)

               self.regclear()

         except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}" ,parent=self.root)


   def update_email(self):
      
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=500,width=500)

      label1=Label(Frame_login,text="Enter Username",font=('times new roman',14,'bold'),fg="black",bg='white')
      label1.place(x=100,y=100)
      self.uname_txt=Entry(Frame_login,font=("times new roman",12,"bold"),bg='lightgray')
      self.uname_txt.place(x=100,y=130,width=100,height=20)


      label2=Label(Frame_login,text="Enter New Email",font=('times new roman',14,'bold'),fg="black",bg='white')
      label2.place(x=100,y=160)
      self.txt_email=Entry(Frame_login,font=("times new roman",12,"bold"),bg='lightgray')
      self.txt_email.place(x=100,y=190,width=200,height=20)

      btn=Button(Frame_login,text="Update",command=self.Email,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn.place(x=100,y=250)

      btn3=Button(Frame_login,command=self.loginform,text="Login",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
      btn3.place(x=100,y=50)

   
   def Email(self):
      try:
         con=pymysql.connect(host="localhost",user="root",password="mArvelisthebest@123.",database="dbms_mini_proj")
         cur=con.cursor()
         cur.execute("update users set email=%s where username=%s",(self.txt_email.get(),self.uname_txt.get()))
         con.commit()
         con.close()
         messagebox.showinfo("Updated","Your Email Has Been Updated")
         self.update_email_clear()
      except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
            self.update_email_clear()


   def update_pwd(self):

      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=700)

      label1=Label(Frame_login,text="Enter Username",font=('times new roman',14,'bold'),fg="black",bg='white')
      label1.place(x=100,y=100)
      self.uname_txt2=Entry(Frame_login,font=("times new roman",12,"bold"),bg='lightgray')
      self.uname_txt2.place(x=100,y=130,width=100,height=20)

      label2=Label(Frame_login,text="Enter New Password",font=('times new roman',14,'bold'),fg="black",bg='white')
      label2.place(x=100,y=160)
      self.txt_pwd=Entry(Frame_login,font=("times new roman",12,"bold"),bg='lightgray')
      self.txt_pwd.place(x=100,y=190,width=200,height=20)

      btn=Button(Frame_login,text="Update",command=self.Password,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn.place(x=100,y=250)

      btn3=Button(Frame_login,command=self.loginform,text="Login",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
      btn3.place(x=100,y=50)

   def Password(self):
      try:
         con=pymysql.connect(host="localhost",user="root",password="mArvelisthebest@123.",database="dbms_mini_proj")
         cur=con.cursor()
         cur.execute("update users set password=%s where username=%s",(self.txt_pwd.get(),self.uname_txt2.get()))
         con.commit()
         con.close()
         messagebox.showinfo("Updated","Your Password Has Been Updated")
         self.update_pwd_clear()
      except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
            self.update_pwd_clear()

      
   def check_posts(self):
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=700)

      btn2=Button(Frame_login,text="Make A Post",command=self.make_a_post,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn2.place(x=250,y=160)

      btn5=Button(Frame_login,text="Show Posts",command=self.show_posts,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn5.place(x=250,y=260)

      btn=Button(Frame_login,text="Go Back",command=self.appscreen,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn.place(x=250,y=360)
   
   def make_a_post(self):

      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=700)

      label1=Label(Frame_login,text="Make A Post",font=('times new roman',16,'bold'),fg="black",bg='white')
      label1.place(x=100,y=160)

      label2=Label(Frame_login,text="Your Post",font=('times new roman',16,'bold'),fg="black",bg='white')
      label2.place(x=100,y=220)
      self.your_post=Entry(Frame_login,font=("times new roman",12,"bold"),bg='lightgray')
      self.your_post.place(x=100,y=250,width=200,height=200)

      label3=Label(Frame_login,text="Your Username",font=('times new roman',16,'bold'),fg="black",bg='white')
      label3.place(x=100,y=100)
      self.post_from=Entry(Frame_login,font=("times new roman",12,"bold"),bg='lightgray')
      self.post_from.place(x=100,y=130,width=100,height=20)

      btn2=Button(Frame_login,text="Post",command=self.SendPost,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn2.place(x=100,y=500)

      btn3=Button(Frame_login,command=self.loginform,text="Login",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
      btn3.place(x=100,y=50)

      btn=Button(Frame_login,command=self.check_posts,text="Go Back",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
      btn.place(x=100,y=650)

   def SendPost(self):
      try:
         con=pymysql.connect(host="localhost",user="root",password="mArvelisthebest@123.",database="dbms_mini_proj")
         cur=con.cursor()
         cur.execute("insert into posts(post_from,post,post_Time) value(%s,%s,now())",(self.post_from.get(),self.your_post.get()))
         con.commit()
         con.close()
         messagebox.showinfo("Successfully Posted")
         #self.send_msg_clear()
      except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
            #self.send_msg_clear()

   def show_posts(self):
      try:
         con=pymysql.connect(host="localhost",user="root",password="mArvelisthebest@123.",database="dbms_mini_proj")
         cur=con.cursor()
         cur.execute("select * from posts where post_from = %s",(self.post_from.get()))
         res=cur.fetchall()
         print("POSTS: ")
         for x2 in res:
            print(x2)
            print()
         con.commit()
         con.close()
         messagebox.showinfo("Successfully Posted")
         #self.send_msg_clear()
      except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
            #self.send_msg_clear()


   
   def check_messages(self):

      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=700)

      btn2=Button(Frame_login,text="Send Message",command=self.send_message,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn2.place(x=250,y=160)

      btn5=Button(Frame_login,text="Show Messages",command=self.show_messages,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn5.place(x=250,y=260)

      btn3=Button(Frame_login,text="Delete Messages",command=self.delete_messages,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn3.place(x=250,y=360)

      btn=Button(Frame_login,text="Go Back",command=self.appscreen,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn.place(x=250,y=460)
      
   def delete_messages(self):
      messagebox.showinfo("test")

   def send_message(self):

      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=700)

      label1=Label(Frame_login,text="Send To(Enter Username)",font=('times new roman',16,'bold'),fg="black",bg='white')
      label1.place(x=100,y=160)
      self.send_to=Entry(Frame_login,font=("times new roman",12,"bold"),bg='lightgray')
      self.send_to.place(x=100,y=190,width=100,height=20)


      label2=Label(Frame_login,text="Your Message",font=('times new roman',16,'bold'),fg="black",bg='white')
      label2.place(x=100,y=220)
      self.your_msg=Entry(Frame_login,font=("times new roman",12,"bold"),bg='lightgray')
      self.your_msg.place(x=100,y=250,width=200,height=200)

      label3=Label(Frame_login,text="Your Username",font=('times new roman',16,'bold'),fg="black",bg='white')
      label3.place(x=100,y=100)
      self.msg_from=Entry(Frame_login,font=("times new roman",12,"bold"),bg='lightgray')
      self.msg_from.place(x=100,y=130,width=100,height=20)

      btn2=Button(Frame_login,text="Send",command=self.SendMessage,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn2.place(x=100,y=500)

      btn3=Button(Frame_login,command=self.loginform,text="Login",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
      btn3.place(x=100,y=50)

      btn=Button(Frame_login,command=self.check_messages,text="Go Back",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
      btn.place(x=100,y=650)

      


   def SendMessage(self):

      try:
         con=pymysql.connect(host="localhost",user="root",password="mArvelisthebest@123.",database="dbms_mini_proj")
         cur=con.cursor()
         cur.execute("insert into messaging(sender_uname,receiver_uname,message,Time_Stamp) value(%s,%s,%s,now())",(self.msg_from.get(),self.send_to.get(),self.your_msg.get()))
         con.commit()
         con.close()
         messagebox.showinfo("Successfully Sent","Your Message has Been Sent")
         self.send_msg_clear()
      except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
            self.send_msg_clear()

   
   
   def show_messages(self):

      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=700)

      label1=Label(Frame_login,text="Your Username",font=('times new roman',16,'bold'),fg="black",bg='white')
      label1.place(x=100,y=160)
      self.show2=Entry(Frame_login,font=("times new roman",12,"bold"),bg='lightgray')
      self.show2.place(x=100,y=190,width=100,height=20)

      btn2=Button(Frame_login,text="Show",command=self.ShowMessages,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn2.place(x=100,y=500)

      btn=Button(Frame_login,text="Go Back",command=self.check_messages,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn.place(x=500,y=500)

   
   def ShowMessages(self):

      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=700)

      label1=Label(Frame_login,text="Your Messages",font=('times new roman',16,'bold'),fg="black",bg='white')
      label1.place(x=100,y=160)
      self.show_here=Listbox(Frame_login,font=("times new roman",12,"bold"),bg='lightgray')
      self.show_here.place(x=100,y=190,width=200,height=200)

      try:
         con=pymysql.connect(host="localhost",user="root",password="mArvelisthebest@123.",database="dbms_mini_proj")
         cur=con.cursor()
         cur.execute("select sender_uname,message,Time_Stamp from messaging where receiver_uname = %s",(self.show2.get()))
         res=cur.fetchall()
         print("MESSAGES: ")
         for x in res:
            print(x)
            print()
         con.commit()
         con.close()
        
      except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
            

      



   def appscreen(self):



      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=700)

      label1=Label(Frame_login,text="Welcome",font=('times new roman',26,'bold'),fg="black",bg='white')
      label1.place(x=250,y=0)

      btn2=Button(Frame_login,text="Update Email",command=self.update_email,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn2.place(x=250,y=160)

      btn5=Button(Frame_login,text="Update Password",command=self.update_pwd,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn5.place(x=250,y=260)

      btn3=Button(Frame_login,text="Check Posts",command=self.check_posts,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn3.place(x=250,y=360)

      btn4=Button(Frame_login,text="Check Messages",command=self.check_messages,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn4.place(x=250,y=460)

      btn5=Button(Frame_login,command=self.loginform,text="Login",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
      btn5.place(x=250,y=560)



   def regclear(self):

      self.entry.delete(0,END)

      self.entry2.delete(0,END)

      self.entry3.delete(0,END)

      self.entry4.delete(0,END)



   def loginclear(self):

      self.username_txt.delete(0,END)

      self.password.delete(0,END)

   def update_email_clear(self):

      self.txt_email.delete(0,END)
      self.uname_txt.delete(0,END)

   def update_pwd_clear(self):
      self.txt_pwd.delete(0,END)
      self.uname_txt2.delete(0,END)

   def send_msg_clear(self):
      self.msg_from.delete(0,END)
      self.send_to.delete(0,END)
      self.your_msg.delete(0,END)



root=Tk()
ob=Login(root)
root.mainloop()