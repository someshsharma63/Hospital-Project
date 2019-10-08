from tkinter import *
	
root=Tk()
root.geometry("1200x700")
root.title("Project Pack")

frame1=Frame(root,height="190",bg="White")
frame1.pack(side=TOP,fill=X);
frame2=Label(frame1,text="Hospital Name",bg="White",fg="green",width="35",font=('times 24'))
frame2.pack(anchor="center")

frame3=Frame(root,borderwidth="10",bg="powderblue",height="60",width="230")
frame3.pack(side=LEFT,fill=Y);
frame4=Label(frame3,text="Menu",fg="White",bg="red",width="35",font=("calibri",18,"bold"))
frame4.pack(anchor="nw")

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

frame5=Frame(root,width="930",height="70",relief="solid",borderwidth=.4)
frame5.pack(side=RIGHT,fill=BOTH,expand=True) 
image1=PhotoImage(file="hospital1.png")
label=Label(frame5,image=image1,width="930",height="600")
label.pack(side=RIGHT)



root.mainloop()