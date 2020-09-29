from tkinter import*
root = Tk()
root.geometry("570x400+270+100")
root.title("Qr code generator")
root.wm_iconbitmap("E:/Qr code ico.ico")
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


Qr_notificationmessage_l = Label(root,text="Notification:",bg="red",fg="blue",width = 15,height="2",font=("times","15","underline bold"))
Qr_notificationmessage_l.place(x=200,y=350,height="40",width="350")
##Entries============================================
Qr_id_txt = Entry(root,bd= "5",relief=GROOVE,bg="pink",font=("times","15","italic bold"),width=30)
Qr_id_txt.place(x=250,y=23)

Qr_name_txt = Entry(root,bd= "5",relief=GROOVE,bg="pink",font=("times","15","italic bold"),width=30)
Qr_name_txt.place(x=250,y=83)

Qr_message_txt = Entry(root,bd= "5",relief=GROOVE,bg="pink",font=("times","15","italic bold"),width=30)
Qr_message_txt.place(x=250,y=143)
##Buttons-=================================
Generate_btn = Button(root,text="Generate",width="10",bd="10",bg="light green",font=("times","12"," bold"),activebackground="blue")
Generate_btn.place(x=10,y=250)

Clear_btn = Button(root,text="Clear",width="10",bd="10",bg="light green",font=("times","12"," bold"),activebackground="blue")
Clear_btn.place(x=210,y=250)

Exit_btn = Button(root,text="Exit",width="10",bd="10",bg="light green",font=("times","12"," bold"),activebackground="blue")
Exit_btn.place(x=410,y=250)
root.mainloop()