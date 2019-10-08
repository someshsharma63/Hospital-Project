from tkinter import *
root=Tk()
root.title("somesh sharma")
root.geometry("1000x700")

frame1=Frame(bg="pink")
frame1.pack(side=TOP,fill=BOTH,expand=True)

frame2=Frame(frame1,height="400",width="400")
frame2.pack(side=RIGHT,padx="200")

frame3=Frame(frame2,height="50")
frame3.pack(side=TOP)

image1=PhotoImage(file="person.png")
label=Label(frame2,image=image1,width=150,height=150)
label.pack(side=LEFT,padx="10")

label1=Label(frame2,text="Username:",font=("calibri",18,"bold"))
label1.pack(anchor="nw",padx=10)

userEntry=Entry(frame2,font=("calibri",14,"bold"))
userEntry.pack(anchor="nw",padx=10)

label1=Label(frame2,text="Password:",font=("calibri",18,"bold"))
label1.pack(anchor="nw",padx=10)

userEntry=Entry(frame2,show='*',font=("calibri",14,"bold"))
userEntry.pack(anchor="nw",padx=10)

buttonok=Button(frame2,text="OK",bg="orange",height=2,width=6,bd=2)
buttonok.pack(side=LEFT,padx="10",pady="10")

buttonexit=Button(frame2,text="EXIT",bg="orange",height=2,width=6,bd=2)
buttonexit.pack(side=RIGHT,padx="10",pady="10")













root.mainloop()