from tkinter import *

root=Tk()
root.geometry("1200x700")
root.title("Project Pack")

frame101=Frame(root,height="190",bg="White")
frame101.pack(side=TOP,fill=X);
frame201=Label(frame101,text="Hospital Name",bg="White",fg="blue",width="35",font=("calibri",18,"bold"))
frame201.pack(anchor="center")

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





frame1=Frame(root,height="200",relief="solid",borderwidth=2,bg="powderblue")
frame1.pack(side=TOP,fill=X);


image6=PhotoImage(file="person.png")
label=Label(frame1,image=image6,width=110,height=110)
label.pack(anchor="center")
label=Label(frame1,text="PATIENT INFORMATION",bg="lightgreen",font=("calibri",23,"bold"))
label.pack(anchor="center")


frame2=Frame(root,height="60",width="300",relief="solid",borderwidth=2)
frame2.pack(side=LEFT,fill=Y);

label1=Label(frame2,text="Input Patient's Name",font=("calibri",17,"bold"))
label1.pack(anchor=CENTER,pady=20)
userEntry=Entry(frame2,width="20",font=("calibri",15,"bold"))
userEntry.pack()


frame3=Frame(root,height="60",width="300",relief="solid",borderwidth=2)
frame3.pack(side=RIGHT,fill=Y);

label1=Label(frame3,text="Status of Disease",font=("calibri",17,"bold"))
label1.pack(padx=80,pady=10)
userEntry=Entry(frame3,width="20",font=("calibri",15,"bold"))
userEntry.pack()

label1=Label(frame3,text="Check IN",font=("calibri",17,"bold"))
label1.pack(pady=10)
userEntry=Entry(frame3,width="20",font=("calibri",15,"bold"))
userEntry.pack()

label1=Label(frame3,text="Room No.",font=("calibri",17,"bold"))
label1.pack(pady=10)
userEntry=Entry(frame3,width="20",font=("calibri",15,"bold"))
userEntry.pack()

label1=Label(frame3,text="Room Type",font=("calibri",17,"bold"))
label1.pack(pady=10)
userEntry=Entry(frame3,width="20",font=("calibri",15,"bold"))
userEntry.pack()

label1=Label(frame3,text="Building",font=("calibri",17,"bold"))
label1.pack(pady=10)
userEntry=Entry(frame3,width="20",font=("calibri",15,"bold"))
userEntry.pack()



button=Button(frame3,text="Update",bg="yellow",bd=7,font=("calibri",15,"bold"))
button.pack(side=LEFT,padx=35);


button=Button(frame3,text="Close",bg="yellow",bd=7,font=("calibri",15,"bold"))
button.pack(side=LEFT,padx=35);



frame4=Frame(root,height="60",width="130",relief="solid",borderwidth=2)
frame4.pack(anchor="center",fill=BOTH,expand=True);

label1=Label(frame4,text="Patient ID",font=("calibri",18,"bold"))
label1.pack(side=TOP)

userEntry=Entry(frame4,width="20",font=("calibri",15,"bold"))
userEntry.pack()

label2=Label(frame4,text="Name",font=("calibri",18,"bold"))
label2.pack(side=TOP)

userEntry=Entry(frame4,width="20",font=("calibri",15,"bold"))
userEntry.pack()

label3=Label(frame4,text="Gender",font=("calibri",18,"bold"))
label3.pack(side=TOP)

data=["MALE","FEMALE","OTHER"]

stringVar=StringVar(root)
stringVar.set("MALE")
dropdownlist=OptionMenu(frame4,stringVar,*data)
dropdownlist.pack()

label4=Label(frame4,text="Age",font=("calibri",18,"bold"))
label4.pack(side=TOP)

userEntry=Entry(frame4,width="20",font=("calibri",15,"bold"))
userEntry.pack()

label5=Label(frame4,text="Phone",font=("calibri",18,"bold"))
label5.pack(side=TOP)

userEntry=Entry(frame4,width="20",font=("calibri",15,"bold"))
userEntry.pack()

label6=Label(frame4,text="Address",font=("calibri",18,"bold"))
label6.pack(side=TOP)

userEntry=Entry(frame4,width="20",font=("calibri",15,"bold"))
userEntry.pack()

label7=Label(frame4,text="Disease",font=("calibri",18,"bold"))
label7.pack(side=TOP) 

userEntry=Entry(frame4,width="20",font=("calibri",15,"bold"))
userEntry.pack()



root.mainloop()