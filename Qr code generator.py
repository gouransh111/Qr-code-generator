from tkinter import*
from tkinter import messagebox#,Toplevel#Toplevel shows us a small screen
import pyqrcode
import os
#Functions===================================
def Generate_Enter(e):
    Generate_btn["bg"] = "purple2"
def Generate_leave(e):
    Generate_btn["bg"] = "light green"

def Clear_Enter(e):
    Clear_btn["bg"] = "purple2"
def Clear_leave(e):
    Clear_btn["bg"] = "light green"

def Exit_Enter(e):
    Exit_btn["bg"] = "purple2"
def Exit_leave(e):
    Exit_btn["bg"] = "light green"

def Quit_root():
     res = messagebox.askokcancel("Notification","Are you sure you want to exit?")
     if res==True:
         root.destroy()
def Clear():
    Qr_id_txt.delete(0,END)
    Qr_message_txt.delete(0,END)
    Qr_name_txt.delete(0,END)
    Qr_notificationmessage_l.config(text="")

def Generate_Qr():
    Qr_id = Qr_id_txt.get()
    Qr_message=Qr_message_txt.get()
    Qr_name= Qr_name_txt.get()
    Group = f"Name : {Qr_name} \nId : {Qr_id} \nMessage : {Qr_message} "
    #print(Qr_name,Qr_id,Qr_message)
    #print(Group)
    pp = 'E:\Qr codes'
    cc = f"{pp}\{Qr_id}{Qr_name}.svg"
    ll = os.listdir(pp)
    if(f"{Qr_id}{Qr_name}.svg" in ll):
            messagebox.showinfo("Notification","Please enetr an other id or name")
    else:
          url = pyqrcode.create(Group)
          url.svg(cc,scale=10)
          mm = f"Qr Code saved as :{cc}"
          Qr_notificationmessage_l.config(text=mm)
          #rr = messagebox.askyesno("Notification","Qr code is generated do you want to see it")
          #if rr==True:
           #   top = Toplevel()
            #  top.geometry("400x400")
             # root.title("Qr code")
              #3top.config(bg="white")
              #i3mg = PhotoImage(file=cc)
              #label1 = Label(top,image=img,bg="white")
              #label1.place(x=10,y=10)
              #top.mainloop()

root = Tk()
root.geometry("570x400+270+100")
root.title("Qr code generator")
root.wm_iconbitmap("E:\Qr code generator\Qr code ico.ico")
root.config(bg="cyan")
##LAbels-=====================================
Qr_id_l = Label(root,text="Enter your Id :",bg="yellow",fg="red",width = 20,height=2,font=("times","12","italic bold"))
Qr_id_l.place(x=10,y=20)

Qr_name_l = Label(root,text="Enter your Name :",bg="yellow",fg="red",width = 20,height=2,font=("times","12","italic bold"))
Qr_name_l.place(x=10,y=80)

Qr_message_l = Label(root,text="Enter your Message :",bg="yellow",fg="red",width = 20,height=2,font=("times","12","italic bold"))
Qr_message_l.place(x=10,y=140)

Qr_notification_l = Label(root,text="Notification:",bg="red",fg="blue",width = 15,height="2",font=("times","15","underline bold"))
Qr_notification_l.place(x=10,y=350,height="40",width="160")


Qr_notificationmessage_l = Label(root,text="",bg="red",fg="blue",width = 30,height="2",font=("times","15","bold"))
Qr_notificationmessage_l.place(x=200,y=350,height="40")

##Entries============================================
Qr_id_txt = Entry(root,bd= "5",relief=GROOVE,bg="pink",font=("times","15","italic bold"),width=30)
Qr_id_txt.place(x=250,y=23)

Qr_name_txt = Entry(root,bd= "5",relief=GROOVE,bg="pink",font=("times","15","italic bold"),width=30)
Qr_name_txt.place(x=250,y=83)

Qr_message_txt = Entry(root,bd= "5",relief=GROOVE,bg="pink",font=("times","15","italic bold"),width=30)
Qr_message_txt.place(x=250,y=143)

#Button logos ==============================================================
Generate_image = PhotoImage(file="E:\Qr code generator\qr-code.png")
Generate_image = Generate_image.subsample(18,18)

Clear_image = PhotoImage(file="E:\Qr code generator\eraser.png")
Clear_image = Clear_image.subsample(18,18)

Exit_image = PhotoImage(file="E:\Qr code generator\cancel.png")
Exit_image = Exit_image.subsample(18,18)

##Buttons-=================================
Generate_btn = Button(root,text="Generate",width="100",bd="10",bg="light green",image=Generate_image,font=("times","12"," bold"),compound=RIGHT,activebackground="green3",command=Generate_Qr)
Generate_btn.place(x=10,y=250)

Clear_btn = Button(root,text="Clear",width="100",bd="10",bg="light green",image=Clear_image,font=("times","12"," bold"),compound=RIGHT,activebackground="green3",command=Clear)
Clear_btn.place(x=210,y=250)

Exit_btn = Button(root,text="Exit",width="100",bd="10",bg="light green",image=Exit_image,font=("times","12"," bold"),compound=RIGHT,activebackground="green3",command=Quit_root)
Exit_btn.place(x=410,y=250)

#HOver effects==============================================
Generate_btn.bind("<Enter>",Generate_Enter)
Generate_btn.bind('<Leave>',Generate_leave)

Clear_btn.bind("<Enter>",Clear_Enter)
Clear_btn.bind('<Leave>',Clear_leave)

Exit_btn.bind("<Enter>",Exit_Enter)
Exit_btn.bind('<Leave>',Exit_leave)
root.mainloop()