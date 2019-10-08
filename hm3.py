from tkinter import *

root=Tk()
root.geometry("1200x700")
root.title("Project Pack")

frame1=Frame(root,height="190",bg="White")
frame1.pack(side=TOP,fill=X);
frame2=Label(frame1,text="Hospital Name",bg="White",fg="blue",width="35",font=("calibri",18,"bold"))
frame2.pack(anchor="center")

frame3=Frame(root,borderwidth="10",bg="powderblue",height="60",width="230")
frame3.pack(side=LEFT,fill=Y);
frame50=Label(frame3,text="Menu",fg="White",bg="red",width="35",font=("calibri",18,"bold"))
frame50.pack(anchor="nw")

button1=Button(frame3,text="Patient Registration",bd=10,font=("calibri",14,"bold"))
button1.pack(side="top",fill=X)

button2=Button(frame3,text="Patient Information",bd=10,font=("calibri",14,"bold"))
button2.pack(side="top",fill=X)

button3=Button(frame3,text="Patient CheckOut",bd=10,font=("calibri",14,"bold"))
button3.pack(side="top",fill=X)

button4=Button(frame3,text="Room Information",bd=10,font=("calibri",14,"bold"))
button4.pack(side="top",fill=X)

button5=Button(frame3,text="Add New Ward",bd=10,font=("calibri",14,"bold"))
button5.pack(side="top",fill=X)

button6=Button(frame3,text="Staff Information",bd=10,font=("calibri",14,"bold"))
button6.pack(side="top",fill=X)

button7=Button(frame3,text="User Information",bd=10,font=("calibri",14,"bold"))
button7.pack(side="top",fill=X)

button8=Button(frame3,text="Add New User",bd=10,font=("calibri",14,"bold"))
button8.pack(side="top",fill=X)

button9=Button(frame3,text="Close",bd=10,font=("calibri",14,"bold"))
button9.pack(side="left",padx=5)

button10=Button(frame3,text="LogOut",bd=10,font=("calibri",14,"bold"))
button10.pack(side="right",pady=50)




frame5=Frame(root,width="10")
frame5.pack(fill=X)
frame11=Frame(frame5)
frame11.grid(row=0,column=0,sticky="news")

frame6=Label(frame11,text="Patient Registration",borderwidth="2",bg="orange",font=("calibri",23,"bold"))
frame6.pack(side=TOP,fill=X)
image1=PhotoImage(file="person.png")
label=Label(frame6,image=image1,width="70",height="70")
label.pack(side=LEFT)



frame5.grid_rowconfigure(0,weight=1)
frame5.grid_columnconfigure(0,weight=1)


frame7=Frame(root)
frame7.pack(fill=BOTH,expand=True)

frame21=Frame(frame7,width=200,height=200)
frame21.grid(row=0,column=0,sticky="news")


frame100=Frame(frame21)
frame100.pack(side=LEFT,fill=BOTH,expand=True);

label1=Label(frame100,text="Registration ID",font=("calibri",23,"bold"))
label1.pack(anchor="nw")

label2=Label(frame100,text="No.",font=("calibri",19))
label2.pack(anchor="nw")

userEntry=Entry(frame100,font=("calibri",18))
userEntry.pack()

label3=Label(frame100,text="Date ",font=("calibri",19))
label3.pack(anchor="nw")

userEntry=Entry(frame100,font=("calibri",18))
userEntry.pack()








frame8=Frame(frame7,width=100)
frame8.grid(row=0,column=1,sticky="news")

frame200=Frame(frame8,height="700",width="700",relief="solid",borderwidth=2)
frame200.pack(side=TOP,fill=BOTH,expand=True);

label1=Label(frame200,text="Room Type",font=("calibri",23,"bold"))
label1.pack(side=TOP)
checkButton1=Checkbutton(frame200,text="VryIMP",font=("calibri",18))
checkButton2=Checkbutton(frame200,text="Normal",font=("calibri",18))
checkButton3=Checkbutton(frame200,text="Medium",font=("calibri",18))
checkButton1.pack()
checkButton2.pack()
checkButton3.pack()








frame23=Frame(frame7,width=180)
frame23.grid(row=0,column=2,sticky="news")

frame102=Frame(frame23,height="700",width="700",relief="solid",borderwidth=2)
frame102.pack(side=TOP,fill=BOTH,expand=True);

label1=Label(frame102,text="Room Information",font=("calibri",23,"bold"))
label1.pack(side=TOP)

label1=Label(frame102,text="Building",font=("calibri",18))
label1.pack(side=TOP)
data=["MALE","FEMALE","OTHERS"]

stringVar=StringVar(root)
stringVar.set("MALE")
dropdownlist=OptionMenu(frame102,stringVar,*data)
dropdownlist.pack()


label1=Label(frame102,text="Room No.",font=("calibri",18))
label1.pack(side=TOP)
data=["1","2","3"]

stringVar=StringVar(root)
stringVar.set("1")
dropdownlist=OptionMenu(frame102,stringVar,*data)
dropdownlist.pack()

label1=Label(frame102,text="Room Type",font=("calibri",18))
label1.pack(side=TOP)

userEntry=Entry(frame102)
userEntry.pack()

label1=Label(frame102,text="Price",font=("calibri",18))
label1.pack(side=TOP)

userEntry=Entry(frame102)
userEntry.pack()




frame7.grid_rowconfigure(0,weight=2)
frame7.grid_columnconfigure(0,weight=2)
frame7.grid_columnconfigure(1,weight=2)
frame7.grid_columnconfigure(2,weight=2)

frame8=Frame(root)
frame8.pack(fill=BOTH,expand=True)

frame9=Frame(frame8)
frame9.grid(row=0,column=0,sticky="news")

frame101=Frame(frame9,height="100",width="900",relief="solid",borderwidth=2)
frame101.pack(anchor="nw",fill=BOTH,expand=True);

label1=Label(frame101,text="Patient's Information",font=("calibri",23,"bold"))
label1.pack(anchor="nw")

label2=Label(frame101,text="PID",font=("calibri",18))
label2.pack(anchor="nw")

userEntry=Entry(frame101)
userEntry.pack()

label3=Label(frame101,text="Name",font=("calibri",18))
label3.pack(anchor="nw")

userEntry=Entry(frame101)
userEntry.pack()

label3=Label(frame101,text="Age",font=("calibri",18))
label3.pack(anchor="nw")

userEntry=Entry(frame101)
userEntry.pack()

label3=Label(frame101,text="Address",font=("calibri",18))
label3.pack(anchor="nw")

userEntry=Entry(frame101)
userEntry.pack()



frame32=Frame(frame8)
frame32.grid(row=0,column=1,sticky="news")

frame200=Frame(frame32,width=100,height=100)
frame200.pack(anchor="nw",fill=BOTH,expand=True);

label3=Label(frame200,text="Disease",font=("calibri",18))
label3.pack(anchor="nw")

userEntry=Entry(frame200)
userEntry.pack()

label3=Label(frame200,text="Status of Disease",font=("calibri",18))
label3.pack(anchor="nw")

userEntry=Entry(frame200)
userEntry.pack()

label3=Label(frame200,text="Phone",font=("calibri",18))
label3.pack(anchor="nw")

userEntry=Entry(frame200)
userEntry.pack()

label3=Label(frame200,text="Gender",font=("calibri",18))
label3.pack(anchor="nw")
data=["MALE","FEMALE","OTHERS"]

stringVar=StringVar(root)
stringVar.set("MALE")
dropdownlist=OptionMenu(frame200,stringVar,*data)
dropdownlist.pack()


button=Button(frame200,text="Add",bd=7,bg="red",font=("calibri",18))
button.pack(side=LEFT,padx="10",pady="10");

button=Button(frame200,text="Room",bd=7,bg="red",font=("calibri",18))
button.pack(side=LEFT,padx="10",pady="10");

button=Button(frame200,text="Close",bg="red",bd=7,font=("calibri",18))
button.pack(side=LEFT,padx="10",pady="10");

frame8.grid_rowconfigure(0,weight=2)
frame8.grid_columnconfigure(0,weight=2)
frame8.grid_columnconfigure(1,weight=2)


root.mainloop()