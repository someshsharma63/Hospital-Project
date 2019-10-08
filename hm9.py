from tkinter import *

root=Tk()
root.geometry("1200x700")
root.title("Project Pack")

frame100=Frame(root,height="190",bg="White")
frame100.pack(side=TOP,fill=X);
frame200=Label(frame100,text="Hospital Name",bg="White",fg="blue",width="35",font=("calibri",18,"bold"))
frame200.pack(anchor="center")

frame300=Frame(root,borderwidth="10",bg="powderblue",height="60",width="230")
frame300.pack(side=LEFT,fill=Y);
frame400=Label(frame300,text="Menu",fg="White",bg="red",width="35",font=("calibri",18,"bold"))
frame400.pack(anchor="nw")

button1=Button(frame300,text="Patient Registration",bd=10,font=("calibri",14,"bold"))
button1.pack(side="top",fill=X)

button2=Button(frame300,text="Patient Information",bd=10,font=("calibri",14,"bold"))
button2.pack(side="top",fill=X)

button3=Button(frame300,text="Patient CheckOut",bd=10,font=("calibri",14,"bold"))
button3.pack(side="top",fill=X)

button4=Button(frame300,text="Room Information",bd=10,font=("calibri",14,"bold"))
button4.pack(side="top",fill=X)

button5=Button(frame300,text="Add New Ward",bd=10,font=("calibri",14,"bold"))
button5.pack(side="top",fill=X)

button6=Button(frame300,text="Staff Information",bd=10,font=("calibri",14,"bold"))
button6.pack(side="top",fill=X)

button7=Button(frame300,text="User Information",bd=10,font=("calibri",14,"bold"))
button7.pack(side="top",fill=X)

button8=Button(frame300,text="Add New User",bd=10,font=("calibri",14,"bold"))
button8.pack(side="top",fill=X)

button9=Button(frame300,text="Close",bd=10,font=("calibri",14,"bold"))
button9.pack(side="left",padx=5)

button10=Button(frame300,text="LogOut",bd=10,font=("calibri",14,"bold"))
button10.pack(side="right",pady=50)

frame1=Frame(root,bg="white")
frame1.pack(fill=BOTH,expand=True)

frame2=Frame(frame1,bg="powderblue",height="110")
frame2.pack(side=TOP,fill=X)

image6=PhotoImage(file="person.png")
label=Label(frame2,image=image6,width=125,height=125)
label.pack(anchor="center")
label=Label(frame2,text="USER INFORMATION",bg="yellow",font=("bold",20))
label.pack(anchor="center")

frame3=Frame(frame1,bg="pink",width="200")
frame3.pack(side=RIGHT,fill=Y)

button=Button(frame3,text="New",bg="yellow",bd=7,font=("bold",20))
button.pack(side=TOP,padx="10",pady="20");

button=Button(frame3,text="Delete",bg="yellow",bd=7,font=("bold",20))
button.pack(side=TOP,padx="10",pady="20");

button=Button(frame3,text="Close",bg="yellow",bd=7,font=("bold",20))
button.pack(side=TOP,padx="10",pady="20");

button=Button(frame3,text="Refresh",bg="yellow",bd=7,font=("bold",19))
button.pack(side=TOP,padx="10",pady="20");

button=Button(frame3,text="Change Password",bg="yellow",bd=7,font=("bold",20))
button.pack(side=TOP,padx="10",pady="20");

frame4=Frame(frame1,bg="pink",bd=2)
frame4.pack(anchor=CENTER,fill=BOTH,expand=True)



frame5=Frame(frame4)
frame5.pack(fill=BOTH,expand=True)
frame51=Frame(frame5,bg="white")
frame51.grid(row=0,column=0,sticky="news")
label1=Label(frame51,text="User ID",font=("calibri",17,"bold"))
label1.pack(side=LEFT,fill=BOTH,expand=True)
frame52=Frame(frame5,bg="white")
frame52.grid(row=0,column=1,sticky="news")
label1=Label(frame52,text="User Name",font=("calibri",17,"bold"))
label1.pack(side=LEFT,fill=BOTH,expand=True)
frame53=Frame(frame5,bg="white")
frame53.grid(row=0,column=2,sticky="news")
label1=Label(frame53,text="Position",font=("calibri",17,"bold"))
label1.pack(side=LEFT,fill=BOTH,expand=True)
frame5.grid_rowconfigure(0,weight=1)
frame5.grid_columnconfigure(0,weight=1)
frame5.grid_columnconfigure(1,weight=1)
frame5.grid_columnconfigure(2,weight=1)

frame6=Frame(frame4)
frame6.pack(fill=BOTH,expand=True)
frame61=Frame(frame6,bg="red")
frame61.grid(row=0,column=0,sticky="news")
label1=Label(frame61,text="1",font=("calibri",17,"bold"))
label1.pack(side=LEFT,fill=BOTH,expand=True)
frame62=Frame(frame6,bg="yellow")
frame62.grid(row=0,column=1,sticky="news")
label1=Label(frame62,text="admin",font=("calibri",17,"bold"))
label1.pack(side=LEFT,fill=BOTH,expand=True)
frame63=Frame(frame6,bg="purple")
frame63.grid(row=0,column=2,sticky="news")
label1=Label(frame63,text="Admin",font=("calibri",17,"bold"))
label1.pack(side=LEFT,fill=BOTH,expand=True)
frame6.grid_rowconfigure(0,weight=1)
frame6.grid_columnconfigure(0,weight=1)
frame6.grid_columnconfigure(1,weight=1)
frame6.grid_columnconfigure(2,weight=1)

frame7=Frame(frame4)
frame7.pack(fill=BOTH,expand=True)
frame71=Frame(frame7,bg="red")
frame71.grid(row=0,column=0,sticky="news")
label1=Label(frame71,text="2",font=("calibri",17,"bold"))
label1.pack(side=LEFT,fill=BOTH,expand=True)
frame72=Frame(frame7,bg="yellow")
frame72.grid(row=0,column=1,sticky="news")
label1=Label(frame72,text="manager",font=("calibri",17,"bold"))
label1.pack(side=LEFT,fill=BOTH,expand=True)
frame73=Frame(frame7,bg="purple")
frame73.grid(row=0,column=2,sticky="news")
label1=Label(frame73,text="Manager",font=("calibri",17,"bold"))
label1.pack(side=LEFT,fill=BOTH,expand=True)
frame7.grid_rowconfigure(0,weight=1)
frame7.grid_columnconfigure(0,weight=1)
frame7.grid_columnconfigure(1,weight=1)
frame7.grid_columnconfigure(2,weight=1)

frame8=Frame(frame4)
frame8.pack(fill=BOTH,expand=True)
frame81=Frame(frame8,bg="red")
frame81.grid(row=0,column=0,sticky="news")
label1=Label(frame81,text="3",font=("calibri",17,"bold"))
label1.pack(side=LEFT,fill=BOTH,expand=True)
frame82=Frame(frame8,bg="yellow")
frame82.grid(row=0,column=1,sticky="news")
label1=Label(frame82,text="cashier",font=("calibri",17,"bold"))
label1.pack(side=LEFT,fill=BOTH,expand=True)
frame83=Frame(frame8,bg="purple")
frame83.grid(row=0,column=2,sticky="news")
label1=Label(frame83,text="Cashier",font=("calibri",17,"bold"))
label1.pack(side=LEFT,fill=BOTH,expand=True)
frame8.grid_rowconfigure(0,weight=1)
frame8.grid_columnconfigure(0,weight=1)
frame8.grid_columnconfigure(1,weight=1)
frame8.grid_columnconfigure(2,weight=1)


root.mainloop()