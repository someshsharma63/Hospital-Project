from tkinter import *

root=Tk()
root.geometry("1800x800")
root.title("Project Pack")

frame100=Frame(root,height="190",bg="White")
frame100.pack(side=TOP,fill=X);
frame200=Label(frame100,text="Hospital Name",bg="Pink",fg="blue",width="35",font=("calibri",18,"bold"))
frame200.pack(anchor="center",fill=X)

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

button5=Button(frame300,text="Finance Management",bd=10,font=("calibri",14,"bold"))
button5.pack(side="top",fill=X)

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


label=Label(frame1,text="Finance Management",font=("calibri",25,"bold"))
label.pack(side=TOP)

label=Label(frame2,text="Select Department",bg="aqua",font=("calibri",20,"bold"))
label.pack(anchor="nw",padx="80",pady="30")

data=["Manager","IT","Cleaner","Nurse","Doctor"]

stringVar=StringVar(root)
stringVar.set("Doctor")
dropdownlist=OptionMenu(frame2,stringVar,*data)
dropdownlist.pack()


label=Label(frame4,text="Select Name",bg="tan",font=("calibri",20,"bold"))
label.pack(pady="10")

label=Label(frame3,text="ID",bg="skyblue",font=("calibri",20,"bold"))
label.pack(side=TOP,pady="10",padx="100")

userEntry=Entry(frame3,font=("calibri",14,"bold"))
userEntry.pack()

label=Label(frame3,text="Name",bg="skyblue",font=("calibri",20,"bold"))
label.pack(side=TOP,pady="10")

userEntry=Entry(frame3,font=("calibri",14,"bold"))
userEntry.pack()

label=Label(frame3,text="Sex",bg="skyblue",font=("calibri",20,"bold"))
label.pack(side=TOP,pady="10")

data=["Male","Female","Other"]

stringVar=StringVar(root)
stringVar.set("Doctor")
dropdownlist=OptionMenu(frame3,stringVar,*data)
dropdownlist.pack()

label=Label(frame3,text="Position",bg="skyblue",font=("calibri",20,"bold"))
label.pack(side=TOP,pady="10")

userEntry=Entry(frame3,font=("calibri",14,"bold"))
userEntry.pack()

label=Label(frame3,text="Salary",bg="skyblue",font=("calibri",20,"bold"))
label.pack(side=TOP,pady="10")

userEntry=Entry(frame3,font=("calibri",14,"bold"))
userEntry.pack()


label=Label(frame3,text="Phone",bg="skyblue",font=("calibri",20,"bold"))
label.pack(side=TOP,pady="10")

userEntry=Entry(frame3,font=("calibri",14,"bold"))
userEntry.pack()


label=Label(frame3,text="Address",bg="skyblue",font=("calibri",20,"bold"))
label.pack(side=TOP,pady="10")

userEntry=Entry(frame3,font=("calibri",14,"bold"))
userEntry.pack()


button=Button(frame5,text="Close",bg="yellow",width="8",bd=9,font=("calibri",14,"bold"))
button.pack(side=RIGHT,padx="18",pady="10");

button=Button(frame5,text="Update",bg="yellow",width="20",bd=9,font=("calibri",14,"bold"))
button.pack(side=RIGHT,padx="18",pady="10");




root.mainloop()