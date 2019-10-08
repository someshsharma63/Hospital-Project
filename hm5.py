from tkinter import *

root=Tk()
root.geometry("1200x700")
root.title("Project Pack")

frame1000=Frame(root,height="190",bg="White")
frame1000.pack(side=TOP,fill=X);
frame2000=Label(frame1000,text="Hospital Name",bg="White",fg="blue",width="35",font=("calibri",18,"bold"))
frame2000.pack(anchor="center")

frame3000=Frame(root,borderwidth="10",bg="powderblue",height="60",width="230")
frame3000.pack(side=LEFT,fill=Y);
frame4000=Label(frame3000,text="Menu",fg="White",bg="red",width="35",font=("calibri",18,"bold"))
frame4000.pack(anchor="nw")

button1=Button(frame3000,text="Patient Registration",bd=10,font=("calibri",14,"bold"))
button1.pack(side="top",fill=X)

button2=Button(frame3000,text="Patient Information",bd=10,font=("calibri",14,"bold"))
button2.pack(side="top",fill=X)

button3=Button(frame3000,text="Patient CheckOut",bd=10,font=("calibri",14,"bold"))
button3.pack(side="top",fill=X)

button4=Button(frame3000,text="Room Information",bd=10,font=("calibri",14,"bold"))
button4.pack(side="top",fill=X)

button5=Button(frame3000,text="Add New Ward",bd=10,font=("calibri",14,"bold"))
button5.pack(side="top",fill=X)

button6=Button(frame3000,text="Staff Information",bd=10,font=("calibri",14,"bold"))
button6.pack(side="top",fill=X)

button7=Button(frame3000,text="User Information",bd=10,font=("calibri",14,"bold"))
button7.pack(side="top",fill=X)

button8=Button(frame3000,text="Add New User",bd=10,font=("calibri",14,"bold"))
button8.pack(side="top",fill=X)

button9=Button(frame3000,text="Close",bd=10,font=("calibri",14,"bold"))
button9.pack(side="left",padx=5)

button10=Button(frame3000,text="LogOut",bd=10,font=("calibri",14,"bold"))
button10.pack(side="right",pady=50)


frame1=Frame(root,height="150",relief="solid",borderwidth=2)
frame1.pack(side=TOP,fill=X);

frame2=Frame(root,height="160",width="150",relief="solid",borderwidth=2)
frame2.pack(side=LEFT,fill=Y);

frame3=Frame(root,height="160",width="150",relief="solid",borderwidth=2)
frame3.pack(side=RIGHT,fill=Y);

frame4=Frame(root,height="160",width="130",relief="solid",borderwidth=2)
frame4.pack(anchor="center",fill=BOTH,expand=True);

frame5=Frame(root,height="90",relief="solid",borderwidth=2)
frame5.pack(side=BOTTOM,fill=X);

image1=PhotoImage(file="hospital1.png")
label=Label(frame1,image=image1,width=125,height=125)
label.pack(side=TOP)

label=Label(frame1,text="Patient Checkout",font=("calibri",25,"bold"))
label.pack(side=TOP)

label=Label(frame2,text="Input Patient Name",font=("calibri",16,"bold"))
label.pack(side=TOP,padx=50)

userEntry=Entry(frame2)
userEntry.pack()

label=Label(frame4,text="Patient ID",font=("calibri",16,"bold"))
label.pack(side=TOP)
userEntry=Entry(frame4)
userEntry.pack()

label=Label(frame4,text="Name",font=("calibri",16,"bold"))
label.pack(side=TOP)
userEntry=Entry(frame4)
userEntry.pack()

label=Label(frame4,text="Gender",font=("calibri",16,"bold"))
label.pack(side=TOP)
userEntry=Entry(frame4)
userEntry.pack()

label=Label(frame4,text="Age",font=("calibri",16,"bold"))
label.pack(side=TOP)
userEntry=Entry(frame4)
userEntry.pack()

label=Label(frame4,text="Phone",font=("calibri",16,"bold"))
label.pack(side=TOP)
userEntry=Entry(frame4)
userEntry.pack()

label=Label(frame4,text="Address",font=("calibri",16,"bold"))
label.pack(side=TOP)
userEntry=Entry(frame4)
userEntry.pack()

label=Label(frame4,text="Disease",font=("calibri",16,"bold"))
label.pack(side=TOP)
userEntry=Entry(frame4)
userEntry.pack()

label=Label(frame4,text="Status",font=("calibri",15,"bold"))
label.pack(side=TOP)

data=["Well","Better","Death"]

stringVar=StringVar(root)
stringVar.set("Better")
dropdownlist=OptionMenu(frame4,stringVar,*data)
dropdownlist.pack()

label=Label(frame3,text="Date In",font=("calibri",15,"bold"))
label.pack(side=TOP,padx=70)
userEntry=Entry(frame3)
userEntry.pack()

label=Label(frame3,text="Date Out",font=("calibri",15,"bold"))
label.pack(side=TOP)
userEntry=Entry(frame3)
userEntry.pack()

label=Label(frame3,text="Room No.",font=("calibri",15,"bold"))
label.pack(side=TOP)
userEntry=Entry(frame3)
userEntry.pack()

label=Label(frame3,text="Room Type",font=("calibri",15,"bold"))
label.pack(side=TOP)
userEntry=Entry(frame3)
userEntry.pack()



label=Label(frame3,text="Unit Price",font=("calibri",15,"bold"))
label.pack(side=TOP)
userEntry=Entry(frame3)
userEntry.pack()

label=Label(frame3,text="Building",font=("calibri",15,"bold"))
label.pack(side=TOP)
userEntry=Entry(frame3)
userEntry.pack()



label=Label(frame3,text="Medicine & Service Price",font=("calibri",16,"bold"))
label.pack(side=TOP)
userEntry=Entry(frame3)
userEntry.pack()


label=Label(frame3,text="Price",font=("calibri",16,"bold"))
label.pack(side=TOP)
userEntry=Entry(frame3)
userEntry.pack()

button=Button(frame5,text="OK",bg="yellow",width="10",bd=9,font=("calibri",14,"bold"))
button.pack(side=RIGHT,padx="25",pady="10");

button=Button(frame5,text="Delete",bg="yellow",width="16",bd=9,font=("calibri",14,"bold"))
button.pack(side=RIGHT,padx="25",pady="10");




root.mainloop()