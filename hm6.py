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


frame1=Frame(root,height="150",relief="solid",borderwidth=2)
frame1.pack(side=TOP,fill=X);

frame2=Frame(root,height="160",width="150",bg="aqua",relief="solid",borderwidth=2)
frame2.pack(side=LEFT,fill=Y);

frame3=Frame(root,height="160",width="150",bg="skyblue",relief="solid",borderwidth=2)
frame3.pack(side=RIGHT,fill=Y);

frame4=Frame(root,height="160",width="130",bg="tan",relief="solid",borderwidth=2)
frame4.pack(anchor="center",fill=BOTH,expand=True);

frame5=Frame(root,height="90",bg="mediumpurple",relief="solid",borderwidth=2)
frame5.pack(side=BOTTOM,fill=X);

image1=PhotoImage(file="person.png")
label=Label(frame1,image=image1,width=125,height=125)
label.pack(side=TOP)




label=Label(frame1,text="Room Information",bg="peru",font=("calibri",25,"bold"))
label.pack(side=TOP)

label=Label(frame2,text="Building",font=("bold",20))
label.pack(anchor="nw",padx="80")

data=["A","B","C"]

stringVar=StringVar(root)
stringVar.set("A")
dropdownlist=OptionMenu(frame2,stringVar,*data)
dropdownlist.pack(pady="10")

label1=Label(frame2,text="Room Type",font=("bold",17))
label1.pack(side=TOP,pady="20")
checkButton1=Checkbutton(frame2,text="VryIMP",font=("bold",15))
checkButton2=Checkbutton(frame2,text="Normal",font=("bold",15))
checkButton3=Checkbutton(frame2,text="Medium",font=("bold",15))
checkButton1.pack()
checkButton2.pack()
checkButton3.pack()

label=Label(frame4,text="Room No.",font=("bold",17))
label.pack(pady="10")

label=Label(frame3,text="Building",font=("bold",17))
label.pack(side=TOP,pady="10")

userEntry=Entry(frame3)
userEntry.pack()

label=Label(frame3,text="Room No.",font=("bold",17))
label.pack(side=TOP,pady="10",padx="80")

userEntry=Entry(frame3)
userEntry.pack()

label=Label(frame3,text="Room Type",font=("bold",17))
label.pack(side=TOP,pady="10")

userEntry=Entry(frame3)
userEntry.pack()

label=Label(frame3,text="Number of Bed",font=("bold",17))
label.pack(side=TOP,pady="10")

userEntry=Entry(frame3)
userEntry.pack()

label=Label(frame3,text="Price",font=("bold",17))
label.pack(side=TOP,pady="10")

userEntry=Entry(frame3)
userEntry.pack()

label=Label(frame3,text="Statue",font=("bold",17))
label.pack(side=TOP,pady="10")

userEntry=Entry(frame3)
userEntry.pack()


button=Button(frame5,text="New",bg="red",width="11",bd=9,font=("calibri",14,"bold"))
button.pack(side=RIGHT,padx="18",pady="10");

button=Button(frame5,text="Update",bg="red",width="16",bd=9,font=("calibri",14,"bold"))
button.pack(side=RIGHT,padx="18",pady="10");


root.mainloop()