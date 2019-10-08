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


frame1=Frame(root,bg="red")
frame1.pack(fill=BOTH,expand=True)

frame2=Frame(frame1,bg="thistle",height="950",width="950")
frame2.pack(side=RIGHT,fill=BOTH,expand=True)


image1=PhotoImage(file="person.png")
label=Label(frame2,image=image1,bg="teal",width=900,height=100)
label.pack(side=TOP,)

label1=Label(frame2,text="Add New User:",bg="cyan",font=("calibri",25,"bold"))
label1.pack(side=TOP,pady="30")

label1=Label(frame2,text="User ID:",bg="gray",font=("calibri",20,"bold"))
label1.pack(anchor="nw",padx=150)

userEntry=Entry(frame2,width="20",font=("calibri",15,"bold"))
userEntry.pack()

label2=Label(frame2,text="User Name:",bg="gray",font=("calibri",20,"bold"))
label2.pack(anchor="nw",padx=150)

userEntry=Entry(frame2,width="20",font=("calibri",15,"bold"))
userEntry.pack()

label3=Label(frame2,text="Password:",bg="gray",font=("calibri",20,"bold"))
label3.pack(anchor="nw",padx=150)

userEntry=Entry(frame2,show='*',width="20",font=("calibri",15,"bold"))
userEntry.pack()

label4=Label(frame2,text="Confirm:",bg="gray",font=("calibri",20,"bold"))
label4.pack(anchor="nw",padx=150)


userEntry=Entry(frame2,show='*',width="20",font=("calibri",15,"bold"))
userEntry.pack()


label5=Label(frame2,text="Position:",bg="gray",font=("calibri",20,"bold"))
label5.pack(anchor="nw",padx=150)

userEntry=Entry(frame2,width="20",font=("calibri",15,"bold"))
userEntry.pack()


button1=Button(frame2,text="Add",fg="red",bd=10,font=("calibri",14,"bold"))
button1.pack(side="left",padx=200)

button2=Button(frame2,text="close",fg="red",bd=10,font=("calibri",14,"bold"))
button2.pack(anchor="ne",padx=100,pady=20)


root.mainloop()