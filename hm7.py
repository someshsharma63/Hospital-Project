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


frame1=Frame(bg="salmon")
frame1.pack(side=TOP,fill=BOTH,expand=True)

frame2=Frame(frame1,bg="salmon",height="900",width="900")
frame2.pack(side=TOP)


image1=PhotoImage(file="person.png")
label=Label(frame2,image=image1,width=150,height=150)
label.pack(side=TOP)

label1=Label(frame2,text="Add New Ward:",bg="thistle",font=("calibri",25,"bold"))
label1.pack(anchor="nw",padx=150)

label1=Label(frame2,text="Building:",bg="thistle",font=("calibri",15,"bold"))
label1.pack(anchor="nw")

data=["A","B","C","D","E"]
stringVar=StringVar(root)
stringVar.set("A")
dropdownlist=OptionMenu(frame2,stringVar,*data)
dropdownlist.pack()

label1=Label(frame2,text="Floor:",bg="thistle",font=("calibri",15,"bold"))
label1.pack(anchor="nw")

data=["Ground floor","First floor","Second floor","Third floor","Fourth floor"]
stringVar=StringVar(root)
stringVar.set("First floor")
dropdownlist=OptionMenu(frame2,stringVar,*data)
dropdownlist.pack()

label1=Label(frame2,text="Room No:",bg="thistle",font=("calibri",15,"bold"))
label1.pack(anchor="nw")

userEntry=Entry(frame2,width="10",font=("calibri",15,"bold"))
userEntry.pack()

label1=Label(frame2,text="Room Type:",bg="thistle",font=("calibri",15,"bold"))
label1.pack(anchor="nw")

data=["Normal","Medium","VIP"]
stringVar=StringVar(root)
stringVar.set("VIP")
dropdownlist=OptionMenu(frame2,stringVar,*data)
dropdownlist.pack()

label1=Label(frame2,text="No of Bed:",bg="thistle",font=("calibri",15,"bold"))
label1.pack(anchor="nw")

userEntry=Entry(frame2,width="10",font=("calibri",15,"bold"))
userEntry.pack()

label1=Label(frame2,text="Unit Price:",bg="thistle",font=("calibri",15,"bold"))
label1.pack(anchor="nw")

button1=Button(frame2,text="Add",fg="red",bd=10,font=("calibri",14,"bold"))
button1.pack(side="left",padx=10)

button2=Button(frame2,text="close",fg="red",bd=10,font=("calibri",14,"bold"))
button2.pack(side="right",pady=50,padx=10)




userEntry=Entry(frame2,width="10",font=("calibri",15,"bold"))
userEntry.pack()



root.mainloop()