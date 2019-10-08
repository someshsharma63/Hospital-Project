from tkinter import *
from tkinter import messagebox
	
global framepatientregistration
global framepatientinformation
global framepatientcheckout
global frameroominfo
global frameaddnewward
global framestaffinfo
global frameuserinfo
global frameaddnewuser
global counterpreg
global counterpinfo
global counterpcheck
global counterrinfo
global counteraward
global countersinfo
global counteruinfo
global counterauser


counterpreg=0
counterpinfo=0
counterpcheck=0
counterrinfo=0
counteraward=0
countersinfo=0
counteruinfo=0
counterauser=0

root=Tk()
root.geometry("1200x700")
root.title("Hospital Management")

def onWindowClose():
	if messagebox.askyesno("Confirm","Are you Sure,you want to exit"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",onWindowClose)


def auser():
	global framemenurightimage
	global framepatientregistration
	global framepatientinformation
	global framepatientcheckout 
	global frameroominfo
	global frameaddnewward
	global framestaffinfo
	global frameuserinfo
	global frameaddnewuser
	global counterpreg
	global counterpinfo
	global counterpcheck
	global counterrinfo
	global counteraward
	global countersinfo
	global counteruinfo
	global counterauser

	counterauser+=1
	counterpreg=0
	counterpinfo=0
	counterpcheck=0
	counterrinfo=0
	counteraward=0
	countersinfo=0
	counteruinfo=0
	try:
		framemenurightimage.destroy()
	except:
		pass
	try:
		framepatientregistration.destroy()
	except:
		pass
	try:
		framepatientinformation.destroy()
	except:
		pass
	try:
		framepatientcheckout.destroy()
	except:
		pass
	try:
		frameroominfo.destroy()
	except:
		pass
	try:
		frameaddnewward.destroy()
	except:
		pass
	try:
		framestaffinfo.destroy()
	except:
		pass
	try:
		frameuserinfo.destroy()
	except:
		pass
	if counterauser==1:
		frameaddnewuser=Frame(root,bg="pink")
		frameaddnewuser.pack(side="right",fill=BOTH,expand=True)

		frameaddnewusertop=Frame(frameaddnewuser,height="200",bg="powderblue",relief="solid",borderwidth=2)
		frameaddnewusertop.pack(side=TOP,fill=X);


		labeladdnewuser=Label(frameaddnewusertop,text="Add New User",bg="powderblue",font=("calibri",23,"bold"))
		labeladdnewuser.pack(anchor="center")


		frameaddnewuserlabels=Frame(frameaddnewuser,height="900",width="900",bg="pink")
		frameaddnewuserlabels.pack(side=TOP)

		labelUserID=Label(frameaddnewuserlabels,text="User ID:     ",bg="pink",font=("calibri",20,"bold"))
		labelUserID.grid(row=0,column=0,padx=110,pady=15)

		entryfname=Entry(frameaddnewuserlabels,font=("calibri",20,"bold"))
		entryfname.grid(row=0,column=1)




		labelFloor=Label(frameaddnewuserlabels,text="User Name:",bg="pink",font=("calibri",20,"bold"))
		labelFloor.grid(row=1,column=0,padx=110,pady=15)
		entryfname=Entry(frameaddnewuserlabels,font=("calibri",20,"bold"))
		entryfname.grid(row=1,column=1)


		labelPassword=Label(frameaddnewuserlabels,text="Password:  ",bg="pink",font=("calibri",20,"bold"))
		labelPassword.grid(row=2,column=0,padx=150,pady=15)
		passwordEntry=Entry(frameaddnewuserlabels)
		passwordentry=Entry(frameaddnewuserlabels,show="*",font=("calibri",20,"bold"))
		passwordentry.grid(row=2,column=1)





		labelPassword=Label(frameaddnewuserlabels,text="Confirm:    ",bg="pink",font=("calibri",20,"bold"))
		labelPassword.grid(row=3,column=0,padx=110,pady=15)
		confirmEntry=Entry(frameaddnewuserlabels)
		confirmentry=Entry(frameaddnewuserlabels,show="*",font=("calibri",20,"bold"))
		confirmentry.grid(row=3,column=1)

		labelNoofBed=Label(frameaddnewuserlabels,text="Position:   ",bg="pink",font=("calibri",20,"bold"))
		labelNoofBed.grid(row=4,column=0,padx=110,pady=15)
		entryfname=Entry(frameaddnewuserlabels,font=("calibri",20,"bold"))
		entryfname.grid(row=4,column=1)



		root.grid_rowconfigure(0,weight=1)
		root.grid_rowconfigure(1,weight=1)
		root.grid_rowconfigure(2,weight=1)
		root.grid_rowconfigure(3,weight=1)
		root.grid_rowconfigure(4,weight=1)
		root.grid_columnconfigure(0,weight=1)
		root.grid_columnconfigure(1,weight=1)


		frameaddnewuserbottom=Frame(frameaddnewuser,height="900",width="900",bg="pink")
		frameaddnewuserbottom.pack(side=TOP)

		buttonAdd=Button(frameaddnewuserbottom,text="Add",fg="red",width=10,bd=8,font=("calibri",16,"bold"))
		buttonAdd.pack(side="left",padx=10,pady=10)

		buttonClose=Button(frameaddnewuserbottom,text="close",fg="red",width=10,bd=8,font=("calibri",16,"bold"))
		buttonClose.pack(side="right",padx=10,pady=10)			




def uinfo():
	global framemenurightimage
	global framepatientregistration
	global framepatientinformation
	global framepatientcheckout 
	global frameroominfo
	global frameaddnewward
	global framestaffinfo
	global frameuserinfo
	global frameaddnewuser
	global counterpreg
	global counterpinfo
	global counterpcheck
	global counterrinfo
	global counteraward
	global countersinfo
	global counteruinfo
	global counterauser

	counteruinfo+=1
	counterpreg=0
	counterpinfo=0
	counterpcheck=0
	counterrinfo=0
	counteraward=0
	countersinfo=0
	counterauser=0
	try:
		framemenurightimage.destroy()
	except:
		pass
	try:
		framepatientregistration.destroy()
	except:
		pass
	try:
		framepatientinformation.destroy()
	except:
		pass
	try:
		framepatientcheckout.destroy()
	except:
		pass
	try:
		frameroominfo.destroy()
	except:
		pass
	try:
		frameaddnewward.destroy()
	except:
		pass
	try:
		framestaffinfo.destroy()
	except:
		pass
	try:
		frameaddnewuser.destroy()
	except:
		pass
	if counteruinfo==1:
		frameuserinfo=Frame(root,bg="white")
		frameuserinfo.pack(side="right",fill=BOTH,expand=True)

		frameuserinfotop=Frame(frameuserinfo,bg="powderblue",height="110")
		frameuserinfotop.pack(side=TOP,fill=X)

		labeluserinformation=Label(frameuserinfotop,text="USER INFORMATION",bg="powderblue",font=("calibri",23,"bold"))
		labeluserinformation.pack(anchor="center")

		frameuserinforight=Frame(frameuserinfo,bg="pink",width="200")
		frameuserinforight.pack(side=RIGHT,fill=Y)

		buttonNew=Button(frameuserinforight,text="New",bg="yellow",width=14,bd=7,font=("bold",20))
		buttonNew.pack(side=TOP,padx="10",pady="20");

		buttonDelete=Button(frameuserinforight,text="Delete",bg="yellow",width=14,bd=7,font=("bold",20))
		buttonDelete.pack(side=TOP,padx="10",pady="20");

		buttonClose=Button(frameuserinforight,text="Close",bg="yellow",width=14,bd=7,font=("bold",20))
		buttonClose.pack(side=TOP,padx="10",pady="20");

		buttonRefresh=Button(frameuserinforight,text="Refresh",bg="yellow",width=14,bd=7,font=("bold",19))
		buttonRefresh.pack(side=TOP,padx="10",pady="20");

		buttonChangepassword=Button(frameuserinforight,text="Change Password",bg="yellow",bd=7,font=("bold",20))
		buttonChangepassword.pack(side=TOP,padx="10",pady="20");

		frameuserinfocenter=Frame(frameuserinfo,bg="pink",bd=2)
		frameuserinfocenter.pack(anchor=CENTER,fill=BOTH,expand=True)



		frame5=Frame(frameuserinfocenter)
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

		frameuserinfocenter6=Frame(frameuserinfocenter)
		frameuserinfocenter6.pack(fill=BOTH,expand=True)
		frameuserinfocenter61=Frame(frameuserinfocenter6,bg="red")
		frameuserinfocenter61.grid(row=0,column=0,sticky="news")
		label1=Label(frameuserinfocenter61,text="1",font=("calibri",17,"bold"))
		label1.pack(side=LEFT,fill=BOTH,expand=True)
		frameuserinfocenter62=Frame(frameuserinfocenter6,bg="yellow")
		frameuserinfocenter62.grid(row=0,column=1,sticky="news")
		label1=Label(frameuserinfocenter62,text="admin",font=("calibri",17,"bold"))
		label1.pack(side=LEFT,fill=BOTH,expand=True)
		frameuserinfocenter63=Frame(frameuserinfocenter6,bg="purple")
		frameuserinfocenter63.grid(row=0,column=2,sticky="news")
		label1=Label(frameuserinfocenter63,text="Admin",font=("calibri",17,"bold"))
		label1.pack(side=LEFT,fill=BOTH,expand=True)
		frameuserinfocenter6.grid_rowconfigure(0,weight=1)
		frameuserinfocenter6.grid_columnconfigure(0,weight=1)
		frameuserinfocenter6.grid_columnconfigure(1,weight=1)
		frameuserinfocenter6.grid_columnconfigure(2,weight=1)

		frameuserinfocenter7=Frame(frameuserinfocenter)
		frameuserinfocenter7.pack(fill=BOTH,expand=True)
		frameuserinfocenter71=Frame(frameuserinfocenter7,bg="red")
		frameuserinfocenter71.grid(row=0,column=0,sticky="news")
		label1=Label(frameuserinfocenter71,text="2",font=("calibri",17,"bold"))
		label1.pack(side=LEFT,fill=BOTH,expand=True)
		frameuserinfocenter72=Frame(frameuserinfocenter7,bg="yellow")
		frameuserinfocenter72.grid(row=0,column=1,sticky="news")
		label1=Label(frameuserinfocenter72,text="manager",font=("calibri",17,"bold"))
		label1.pack(side=LEFT,fill=BOTH,expand=True)
		frameuserinfocenter73=Frame(frameuserinfocenter7,bg="purple")
		frameuserinfocenter73.grid(row=0,column=2,sticky="news")
		label1=Label(frameuserinfocenter73,text="Manager",font=("calibri",17,"bold"))
		label1.pack(side=LEFT,fill=BOTH,expand=True)
		frameuserinfocenter7.grid_rowconfigure(0,weight=1)
		frameuserinfocenter7.grid_columnconfigure(0,weight=1)
		frameuserinfocenter7.grid_columnconfigure(1,weight=1)
		frameuserinfocenter7.grid_columnconfigure(2,weight=1)

		frameuserinfocenter8=Frame(frameuserinfocenter)
		frameuserinfocenter8.pack(fill=BOTH,expand=True)
		frameuserinfocenter81=Frame(frameuserinfocenter8,bg="red")
		frameuserinfocenter81.grid(row=0,column=0,sticky="news")
		label1=Label(frameuserinfocenter81,text="3",font=("calibri",17,"bold"))
		label1.pack(side=LEFT,fill=BOTH,expand=True)
		frameuserinfocenter82=Frame(frameuserinfocenter8,bg="yellow")
		frameuserinfocenter82.grid(row=0,column=1,sticky="news")
		label1=Label(frameuserinfocenter82,text="cashier",font=("calibri",17,"bold"))
		label1.pack(side=LEFT,fill=BOTH,expand=True)
		frameuserinfocenter83=Frame(frameuserinfocenter8,bg="purple")
		frameuserinfocenter83.grid(row=0,column=2,sticky="news")
		label1=Label(frameuserinfocenter83,text="Cashier",font=("calibri",17,"bold"))
		label1.pack(side=LEFT,fill=BOTH,expand=True)
		frameuserinfocenter8.grid_rowconfigure(0,weight=1)
		frameuserinfocenter8.grid_columnconfigure(0,weight=1)
		frameuserinfocenter8.grid_columnconfigure(1,weight=1)
		frameuserinfocenter8.grid_columnconfigure(2,weight=1)







def sinfo():
	global framemenurightimage
	global framepatientregistration
	global framepatientinformation
	global framepatientcheckout 
	global frameroominfo
	global frameaddnewward
	global framestaffinfo
	global frameuserinfo
	global frameaddnewuser
	global counterpreg
	global counterpinfo
	global counterpcheck
	global counterrinfo
	global counteraward
	global countersinfo
	global counteruinfo
	global counterauser

	countersinfo+=1
	counterpreg=0
	counterpinfo=0
	counterpcheck=0
	counterrinfo=0
	counteraward=0
	counteruinfo=0
	counterauser=0
	try:
		framemenurightimage.destroy()
	except:
		pass
	try:
		framepatientregistration.destroy()
	except:
		pass
	try:
		framepatientinformation.destroy()
	except:
		pass
	try:
		framepatientcheckout.destroy()
	except:
		pass
	try:
		frameroominfo.destroy()
	except:
		pass
	try:
		frameaddnewward.destroy()
	except:
		pass
	try:
		frameuserinfo.destroy()
	except:
		pass
	try:
		frameaddnewuser.destroy()
	except:
		pass
	if countersinfo==1:
		framestaffinfo=Frame(root)
		framestaffinfo.pack(side="right",fill=BOTH,expand=True)


		framestaffinfotop=Frame(framestaffinfo,height="200",relief="solid",borderwidth=2,bg="powderblue")
		framestaffinfotop.pack(side=TOP,fill=X);

		labelstaffinformation=Label(framestaffinfotop,text="STAFF INFORMATION",bg="powderblue",font=("calibri",23,"bold"))
		labelstaffinformation.pack(anchor="center")


		framestaffinformationleft=Frame(framestaffinfo,height="60",width="300",relief="solid",borderwidth=2)
		framestaffinformationleft.pack(side=LEFT,fill=Y);

		labelUsername=Label(framestaffinformationleft,text="User Name",font=("calibri",20,"bold"))
		labelUsername.pack(anchor=CENTER,pady=20)
		UsernameEntry=Entry(framestaffinformationleft,width="20",font=("calibri",15,"bold"))
		UsernameEntry.pack()


		framestaffinformationright=Frame(framestaffinfo,height="60",width="300",relief="solid",borderwidth=2)
		framestaffinformationright.pack(side=RIGHT,fill=Y);

		buttonAdd=Button(framestaffinformationright,text="Add",bg="yellow",width=10,bd=7,font=("calibri",15,"bold"))
		buttonAdd.pack(side=TOP,padx="70",pady="40");

		buttonNew=Button(framestaffinformationright,text="New",bg="yellow",bd=7,width=10,font=("calibri",15,"bold"))
		buttonNew.pack(side=TOP,padx="70",pady="40");

		buttonUpdate=Button(framestaffinformationright,text="Update",bg="yellow",bd=7,width=10,font=("calibri",15,"bold"))
		buttonUpdate.pack(side=TOP,padx="70",pady="40");

		buttonClose=Button(framestaffinformationright,text="Close",bg="yellow",bd=7,width=10,font=("calibri",15,"bold"))
		buttonClose.pack(side=TOP,padx="50",pady="20");


		framestaffinformationcenter=Frame(framestaffinfo,height="60",width="130",relief="solid",borderwidth=2)
		framestaffinformationcenter.pack(anchor="center",fill=BOTH,expand=True);



		labelid=Label(framestaffinformationcenter,text="ID:                 ",font=("calibri",20,"bold"))
		labelid.grid(row=0,column=0,padx=10,pady=20)
		IDentry=Entry(framestaffinformationcenter,font=("calibri",20,"bold"))
		IDentry.grid(row=0,column=1,padx=0)

		labelName=Label(framestaffinformationcenter,text="Name:            ",font=("calibri",20,"bold"))
		labelName.grid(row=1,column=0,padx=10,pady=20)
		Nameentry=Entry(framestaffinformationcenter,font=("calibri",20,"bold"))
		Nameentry.grid(row=1,column=1,padx=0)




		labelGender=Label(framestaffinformationcenter,text="Sex:                ",font=("calibri",20,"bold"))
		labelGender.grid(row=2,column=0)
		checkButton1=Checkbutton(framestaffinformationcenter,text="Male",font=("calibri",18,"bold"))
		checkButton2=Checkbutton(framestaffinformationcenter,text="Female",font=("calibri",18,"bold"))
		checkButton1.grid(row=2,column=1,sticky="w",)
		checkButton2.grid(row=2,column=1,sticky="e",padx=90)


		labelPosition=Label(framestaffinformationcenter,text="Position:         ",font=("calibri",20,"bold"))
		labelPosition.grid(row=3,column=0,padx=10,pady=20)
		Positionentry=Entry(framestaffinformationcenter,font=("calibri",20,"bold"))
		Positionentry.grid(row=3,column=1,padx=0)

		labelSalary=Label(framestaffinformationcenter,text="Salary:            ",font=("calibri",20,"bold"))
		labelSalary.grid(row=4,column=0,padx=10,pady=20)
		entryfname=Entry(framestaffinformationcenter,font=("calibri",20,"bold"))
		entryfname.grid(row=4,column=1,padx=0)

		labelPhone=Label(framestaffinformationcenter,text="Phone:           ",font=("calibri",20,"bold"))
		labelPhone.grid(row=5,column=0,padx=10,pady=20)
		Phoneentry=Entry(framestaffinformationcenter,font=("calibri",20,"bold"))
		Phoneentry.grid(row=5,column=1,padx=0)


		labelAddress=Label(framestaffinformationcenter,text="Address:         ",font=("calibri",20,"bold"))
		labelAddress.grid(row=6,column=0,padx=10,pady=20)
		Addressentry=Entry(framestaffinformationcenter,font=("calibri",20,"bold"))
		Addressentry.grid(row=6,column=1,padx=0)


		root.grid_rowconfigure(0,weight=1)
		root.grid_rowconfigure(1,weight=1)
		root.grid_rowconfigure(2,weight=1)
		root.grid_rowconfigure(3,weight=1)
		root.grid_rowconfigure(4,weight=1)
		root.grid_rowconfigure(5,weight=1)
		root.grid_rowconfigure(6,weight=1)
		root.grid_columnconfigure(0,weight=1)
		root.grid_columnconfigure(1,weight=1)





def award():
	global framemenurightimage
	global framepatientregistration
	global framepatientinformation
	global framepatientcheckout 
	global frameroominfo
	global frameaddnewward
	global framestaffinfo
	global frameuserinfo
	global frameaddnewuser
	global counterpreg
	global counterpinfo
	global counterpcheck
	global counterrinfo
	global counteraward
	global countersinfo
	global counteruinfo
	global counterauser

	counteraward+=1
	counterpreg=0
	counterpinfo=0
	counterpcheck=0
	counterrinfo=0
	countersinfo=0
	counteruinfo=0
	counterauser=0
	try:
		framemenurightimage.destroy()
	except:
		pass
	try:
		framepatientregistration.destroy()
	except:
		pass
	try:
		framepatientinformation.destroy()
	except:
		pass
	try:
		framepatientcheckout.destroy()
	except:
		pass
	try:
		frameroominfo.destroy()
	except:
		pass
	try:
		framestaffinfo.destroy()
	except:
		pass
	try:
		frameuserinfo.destroy()
	except:
		pass
	try:
		frameaddnewuser.destroy()
	except:
		pass
	if counteraward==1:
		frameaddnewward=Frame(root)
		frameaddnewward.pack(side="right",fill=BOTH,expand=True)

		frameaddnewwardtop=Frame(frameaddnewward,height="200",bg="powderblue",relief="solid",borderwidth=3)
		frameaddnewwardtop.pack(side=TOP,fill=X);


		labeladdnewward=Label(frameaddnewwardtop,text="Add New Ward",bg="powderblue",font=("calibri",23,"bold"))
		labeladdnewward.pack(anchor="center")


		frameaddnewwardlabels=Frame(frameaddnewward,height="900",width="900")
		frameaddnewwardlabels.pack(side=TOP)

		labelUserID=Label(frameaddnewwardlabels,text="Building:     ",font=("calibri",20,"bold"))
		labelUserID.grid(row=0,column=0,padx=110,pady=15)

		entryfname=Entry(frameaddnewwardlabels,font=("calibri",20,"bold"))
		entryfname.grid(row=0,column=1)




		labelFloor=Label(frameaddnewwardlabels,text="Floor:         ",font=("calibri",20,"bold"))
		labelFloor.grid(row=1,column=0,padx=110,pady=15)
		entryfname=Entry(frameaddnewwardlabels,font=("calibri",20,"bold"))
		entryfname.grid(row=1,column=1)


		labelFloor=Label(frameaddnewwardlabels,text="Room No:    ",font=("calibri",20,"bold"))
		labelFloor.grid(row=2,column=0,padx=110,pady=15)
		entryfname=Entry(frameaddnewwardlabels,font=("calibri",20,"bold"))
		entryfname.grid(row=2,column=1)





		labelFloor=Label(frameaddnewwardlabels,text="Room Type:",font=("calibri",20,"bold"))
		labelFloor.grid(row=3,column=0,padx=110,pady=15)
		entryfname=Entry(frameaddnewwardlabels,font=("calibri",20,"bold"))
		entryfname.grid(row=3,column=1)

		labelNoofBed=Label(frameaddnewwardlabels,text="No of bed:     ",font=("calibri",20,"bold"))
		labelNoofBed.grid(row=4,column=0,padx=110,pady=15)
		entryfname=Entry(frameaddnewwardlabels,font=("calibri",20,"bold"))
		entryfname.grid(row=4,column=1)

		labelUserID=Label(frameaddnewwardlabels,text="Unit Price:     ",font=("calibri",20,"bold"))
		labelUserID.grid(row=5,column=0,padx=110,pady=15)

		entryfname=Entry(frameaddnewwardlabels,font=("calibri",20,"bold"))
		entryfname.grid(row=5,column=1)



		root.grid_rowconfigure(0,weight=1)
		root.grid_rowconfigure(1,weight=1)
		root.grid_rowconfigure(2,weight=1)
		root.grid_rowconfigure(3,weight=1)
		root.grid_rowconfigure(4,weight=1)
		root.grid_rowconfigure(5,weight=1)
		root.grid_columnconfigure(0,weight=1)
		root.grid_columnconfigure(1,weight=1)


		frameaddnewwardbottom=Frame(frameaddnewward,height="900",width="900")
		frameaddnewwardbottom.pack(side=TOP)

		buttonAdd=Button(frameaddnewwardbottom,text="Add",fg="red",width=10,bd=8,font=("calibri",16,"bold"))
		buttonAdd.pack(side="left",padx=10,pady=10)

		buttonClose=Button(frameaddnewwardbottom,text="close",fg="red",width=10,bd=8,font=("calibri",16,"bold"))
		buttonClose.pack(side="right",padx=10,pady=10)			






def rinfo():
	global framemenurightimage
	global framepatientregistration
	global framepatientinformation
	global framepatientcheckout 
	global frameroominfo
	global frameaddnewward
	global framestaffinfo
	global frameuserinfo
	global frameaddnewuser
	global counterpreg
	global counterpinfo
	global counterpcheck
	global counterrinfo
	global counteraward
	global countersinfo
	global counteruinfo
	global counterauser

	counterrinfo+=1

	counterpreg=0
	counterpinfo=0
	counterpcheck=0
	counteraward=0
	countersinfo=0
	counteruinfo=0
	counterauser=0

	try:
		framemenurightimage.destroy()
	except:
		pass			
	try:
		framepatientregistration.destroy()
	except:
		pass
	try:
		framepatientinformation.destroy()
	except:
		pass
	try:
		framepatientcheckout.destroy()
	except:
		pass
	try:
		frameaddnewward.destroy()
	except:
		pass
	try:
		framestaffinfo.destroy()
	except:
		pass
	try:
		frameuserinfo.destroy()
	except:
		pass
	try:
		frameaddnewuser.destroy()
	except:
		pass
		
	if counterrinfo==1:	
		frameroominfo=Frame(root)
		frameroominfo.pack(side="right",fill=BOTH,expand=True)

		frameroominfotop=Frame(frameroominfo,height="150",relief="solid",borderwidth=2)
		frameroominfotop.pack(side=TOP,fill=X);

		frameroominfoleft=Frame(frameroominfo,height="160",width="150",bg="aqua",relief="solid",borderwidth=2)
		frameroominfoleft.pack(side=LEFT,fill=Y);

		frameroominforight=Frame(frameroominfo,height="160",width="150",bg="skyblue",relief="solid",borderwidth=2)
		frameroominforight.pack(side=RIGHT,fill=Y);

		frameroominfocenter=Frame(frameroominfo,height="160",width="130",bg="tan",relief="solid",borderwidth=2)
		frameroominfocenter.pack(anchor="center",fill=BOTH,expand=True);

		frameroominfobottom=Frame(frameroominfo,height="90",bg="mediumpurple",relief="solid",borderwidth=2)
		frameroominfobottom.pack(side=BOTTOM,fill=X);


		labelRoominformation=Label(frameroominfotop,text="Room Information",font=("calibri",20,"bold"))
		labelRoominformation.pack(side=TOP)


		labelBuilding=Label(frameroominfoleft,text="Building",bg="aqua",font=("calibri",20,"bold"))
		labelBuilding.pack(anchor="nw",padx="80")

		data=["A","B","C"]

		stringVar=StringVar(frameroominfo)
		stringVar.set("A")
		dropdownlist=OptionMenu(frameroominfoleft,stringVar,*data)
		dropdownlist.pack(pady="10")

		labelRoomtype=Label(frameroominfoleft,text="Room Type:-",bg="aqua",font=("calibri",20,"bold"))
		labelRoomtype.pack(side=TOP,pady="20")
		checkButton1=Checkbutton(frameroominfoleft,text="VryIMP",bg="aqua",font=("calibri",15,"bold"))
		checkButton2=Checkbutton(frameroominfoleft,text="Normal",bg="aqua",font=("calibri",15,"bold"))
		checkButton3=Checkbutton(frameroominfoleft,text="Medium",bg="aqua",font=("calibri",15,"bold"))
		checkButton1.pack()
		checkButton2.pack()
		checkButton3.pack()

		labelRoomno=Label(frameroominfocenter,text="Room No.",bg="tan",font=("calibri",20,"bold"))
		labelRoomno.pack(pady="10")

		RoomNoEntry=Entry(frameroominfocenter,width=25,font=("calibri",18,"bold"))
		RoomNoEntry.pack()

		labelBuilding=Label(frameroominforight,text="Building",bg="skyblue",font=("calibri",20,"bold"))
		labelBuilding.pack(side=TOP,pady="10")

		BuildingEntry=Entry(frameroominforight,font=("calibri",15,"bold"))
		BuildingEntry.pack()

		labelRoomno=Label(frameroominforight,text="Room No.",bg="skyblue",font=("calibri",20,"bold"))
		labelRoomno.pack(side=TOP,pady="10",padx="80")

		RoomnoEntry=Entry(frameroominforight,font=("calibri",15,"bold"))
		RoomnoEntry.pack()

		labelRoomtype=Label(frameroominforight,text="Room Type",bg="skyblue",font=("calibri",20,"bold"))
		labelRoomtype.pack(side=TOP,pady="10")

		RoomtypeEntry=Entry(frameroominforight,font=("calibri",15,"bold"))
		RoomtypeEntry.pack()

		labelnoofbed=Label(frameroominforight,text="Number of Bed",bg="skyblue",font=("calibri",20,"bold"))
		labelnoofbed.pack(side=TOP,pady="10")

		noofbedEntry=Entry(frameroominforight,font=("calibri",15,"bold"))
		noofbedEntry.pack()

		labelPrice=Label(frameroominforight,text="Price",bg="skyblue",font=("calibri",20,"bold"))
		labelPrice.pack(side=TOP,pady="10")

		PriceEntry=Entry(frameroominforight,font=("calibri",15,"bold"))
		PriceEntry.pack()

		labelStatue=Label(frameroominforight,text="Statue",bg="skyblue",font=("calibri",20,"bold"))
		labelStatue.pack(side=TOP,pady="10")

		StatueEntry=Entry(frameroominforight,font=("calibri",15,"bold"))
		StatueEntry.pack()


		ButtonClose=Button(frameroominfobottom,text="Close",bg="yellow",width="9",bd=4,font=("calibri",16,"bold"))
		ButtonClose.pack(side=RIGHT,padx="5",pady="10");

		ButtonDelete=Button(frameroominfobottom,text="Delete",bg="yellow",width="9",bd=4,font=("calibri",16,"bold"))
		ButtonDelete.pack(side=RIGHT,padx="5",pady="10");

		ButtonUpdate=Button(frameroominfobottom,text="Update",bg="yellow",width="9",bd=4,font=("calibri",16,"bold"))
		ButtonUpdate.pack(side=RIGHT,padx="5",pady="10");

		ButtonNew=Button(frameroominfobottom,text="New",bg="yellow",width="9",bd=4,font=("calibri",16,"bold"))
		ButtonNew.pack(side=RIGHT,padx="5",pady="10");







def pcheck():
	global framemenurightimage
	global framepatientregistration
	global framepatientinformation
	global framepatientcheckout
	global frameroominfo
	global frameaddnewward
	global framestaffinfo
	global frameuserinfo
	global frameaddnewuser
	global counterpreg
	global counterpinfo
	global counterpcheck
	global counterrinfo
	global counteraward
	global countersinfo
	global counteruinfo
	global counterauser

	counterpcheck+=1	

	counterpreg=0
	counterpinfo=0
	counterrinfo=0
	counteraward=0
	countersinfo=0
	counteruinfo=0
	counterauser=0
	try:
		framemenurightimage.destroy()
	except:
		pass	
	try:	
		framepatientregistration.destroy()
	except:
		pass	
	try:
		framepatientinformation.destroy()
	except:
		pass
	try:
		frameroominfo.destroy()
	except:
		pass
	try:
		frameaddnewward.destroy()
	except:
		pass
	try:
		framestaffinfo.destroy()
	except:
		pass
	try:
		frameuserinfo.destroy()
	except:
		pass
	try:
		frameaddnewuser.destroy()
	except:
		pass

	if counterpcheck==1:	
		framepatientcheckout=Frame(root)
		framepatientcheckout.pack(side="right",fill=BOTH,expand=True)

		framepatientcheckouttop=Frame(framepatientcheckout,height="150",bg="powderblue",relief="solid",borderwidth=2)
		framepatientcheckouttop.pack(side=TOP,fill=X);

		framepatientcheckoutleft=Frame(framepatientcheckout,height="160",width="150",relief="solid",borderwidth=2)
		framepatientcheckoutleft.pack(side=LEFT,fill=Y);

		framepatientcheckoutright=Frame(framepatientcheckout,height="160",width="150",relief="solid",borderwidth=2)
		framepatientcheckoutright.pack(side=RIGHT,fill=Y);


		framepatientcheckoutbottom=Frame(framepatientcheckout,height="90",relief="solid",borderwidth=2)
		framepatientcheckoutbottom.pack(side=BOTTOM,fill=X);


		labelpatientcheckout=Label(framepatientcheckouttop,text="Patient Checkout",bg="powderblue",fg="red",font=("calibri",25,"bold"))
		labelpatientcheckout.pack(side=TOP)

		labelenterpatientname=Label(framepatientcheckoutleft,text="Enter Patient Name",font=("calibri",20,"bold"))
		labelenterpatientname.pack(side=TOP,pady=15)

		enterpatientnameEntry=Entry(framepatientcheckoutleft,font=("calibri",14,"bold"))
		enterpatientnameEntry.pack()


		framepatientcheckoutcenter=Frame(framepatientcheckout,height="160",width="130",relief="solid",borderwidth=2)
		framepatientcheckoutcenter.pack(anchor="center",fill=BOTH,expand=True);

		labelPatientid=Label(framepatientcheckoutcenter,text="Patient ID:",font=("calibri",20,"bold"))
		labelPatientid.grid(row=0,column=0,sticky="w",padx=10)
		Patientidentry=Entry(framepatientcheckoutcenter,font=("calibri",20,"bold"))
		Patientidentry.grid(row=0,column=1,pady=20)

		labelName=Label(framepatientcheckoutcenter,text="Name:       ",font=("calibri",20,"bold"))
		labelName.grid(row=1,column=0,pady=10)
		Nameentry=Entry(framepatientcheckoutcenter,font=("calibri",20,"bold"))
		Nameentry.grid(row=1,column=1)

		Gender=StringVar()


		labelGender=Label(framepatientcheckoutcenter,text="  Gender:    ",font=("calibri",20,"bold"))
		labelGender.grid(row=2,column=0,sticky="w")
		checkButton1=Checkbutton(framepatientcheckoutcenter,text="Male",font=("calibri",18,"bold"))
		checkButton2=Checkbutton(framepatientcheckoutcenter,text="Female",font=("calibri",18,"bold"))
		checkButton1.grid(row=2,column=1,sticky="w",)
		checkButton2.grid(row=2,column=1,sticky="e",padx=90)

		labelAge=Label(framepatientcheckoutcenter,text="Age:         ",font=("calibri",20,"bold"))
		labelAge.grid(row=3,column=0,pady=10)
		Ageentry=Entry(framepatientcheckoutcenter,font=("calibri",20,"bold"))
		Ageentry.grid(row=3,column=1)

		labelPhone=Label(framepatientcheckoutcenter,text="Phone:     ",font=("calibri",20,"bold"))
		labelPhone.grid(row=4,column=0,pady=10)
		Phoneentry=Entry(framepatientcheckoutcenter,font=("calibri",20,"bold"))
		Phoneentry.grid(row=4,column=1)

		labelAddress=Label(framepatientcheckoutcenter,text="Address:  ",font=("calibri",20,"bold"))
		labelAddress.grid(row=5,column=0,pady=10)
		Addressentry=Entry(framepatientcheckoutcenter,font=("calibri",20,"bold"))
		Addressentry.grid(row=5,column=1)


		labelDisease=Label(framepatientcheckoutcenter,text="Disease:   ",font=("calibri",20,"bold"))
		labelDisease.grid(row=6,column=0,pady=10)
		Diseaseentry=Entry(framepatientcheckoutcenter,font=("calibri",20,"bold"))
		Diseaseentry.grid(row=6,column=1)


		labelStatus=Label(framepatientcheckoutcenter,text="Status     ",font=("calibri",20,"bold"))
		labelStatus.grid(row=7,column=0,pady=10)
		StatusEntry=Entry(framepatientcheckoutcenter,font=("calibri",20,"bold"))
		StatusEntry.grid(row=7,column=1)


		root.grid_rowconfigure(0,weight=1)
		root.grid_rowconfigure(1,weight=1)
		root.grid_rowconfigure(2,weight=1)
		root.grid_rowconfigure(3,weight=1)
		root.grid_rowconfigure(4,weight=1)
		root.grid_rowconfigure(5,weight=1)
		root.grid_rowconfigure(6,weight=1)
		root.grid_columnconfigure(0,weight=1)
		root.grid_columnconfigure(1,weight=1)





		labelDateIn=Label(framepatientcheckoutright,text="Date In",font=("calibri",20,"bold"))
		labelDateIn.pack(side=TOP,padx=70)
		DateInEntry=Entry(framepatientcheckoutright,font=("calibri",17,"bold"))
		DateInEntry.pack()

		labelDateOut=Label(framepatientcheckoutright,text="Date Out",font=("calibri",20,"bold"))
		labelDateOut.pack(side=TOP,padx=70)
		DateOutEntry=Entry(framepatientcheckoutright,font=("calibri",17,"bold"))
		DateOutEntry.pack()

		labelRoomNo=Label(framepatientcheckoutright,text="Room No.",font=("calibri",20,"bold"))
		labelRoomNo.pack(side=TOP,padx=70)
		RoomNoEntry=Entry(framepatientcheckoutright,font=("calibri",17,"bold"))
		RoomNoEntry.pack()

		labelRoomtype=Label(framepatientcheckoutright,text="Room Type",font=("calibri",20,"bold"))
		labelRoomtype.pack(side=TOP,padx=70)
		RoomtypeEntry=Entry(framepatientcheckoutright,font=("calibri",17,"bold"))
		RoomtypeEntry.pack()


		labelUnitprice=Label(framepatientcheckoutright,text="Unit Price",font=("calibri",20,"bold"))
		labelUnitprice.pack(side=TOP,padx=70)
		UnitpriceEntry=Entry(framepatientcheckoutright,font=("calibri",17,"bold"))
		UnitpriceEntry.pack()

		labelbuilding=Label(framepatientcheckoutright,text="Building",font=("calibri",20,"bold"))
		labelbuilding.pack(side=TOP,padx=70)
		buildingEntry=Entry(framepatientcheckoutright,font=("calibri",17,"bold"))
		buildingEntry.pack()



		labelMedicine=Label(framepatientcheckoutright,text="Medicine & Service Price",font=("calibri",20,"bold"))
		labelMedicine.pack(side=TOP)
		MedicineEntry=Entry(framepatientcheckoutright,font=("calibri",17,"bold"))
		MedicineEntry.pack()


		labelPrice=Label(framepatientcheckoutright,text="Price:-",font=("calibri",20,"bold"))
		labelPrice.pack(side=TOP)
		PriceEntry=Entry(framepatientcheckoutright,font=("calibri",17,"bold"))
		PriceEntry.pack()



		ButtonClose=Button(framepatientcheckoutbottom,text="Close",bg="yellow",width="10",bd=9,font=("calibri",14,"bold"))
		ButtonClose.pack(side=RIGHT,padx="20",pady="10");

		ButtonDelete=Button(framepatientcheckoutbottom,text="Delete",bg="yellow",width="10",bd=9,font=("calibri",14,"bold"))
		ButtonDelete.pack(side=RIGHT,padx="20",pady="10");


		ButtonOK=Button(framepatientcheckoutbottom,text="OK",bg="yellow",width="10",bd=9,font=("calibri",14,"bold"))
		ButtonOK.pack(side=RIGHT,padx="20",pady="10");






def pinfo():

	global framepatientinformation
	global framepatientregistration
	global framepatientcheckout
	global framemenurightimage
	global frameroominfo
	global frameaddnewward
	global framestaffinfo
	global frameuserinfo
	global frameaddnewuser
	global counterpinfo
	global counterpreg
	global counterpcheck
	global counterrinfo
	global counteraward
	global countersinfo
	global counteruinfo
	global counterauser

	counterpinfo+=1

	counterpreg=0
	counterpcheck=0
	counterrinfo=0
	counteraward=0
	countersinfo=0
	counteruinfo=0
	counterauser=0


	try:
		framemenurightimage.destroy()
	except:
		pass
	try:
		framepatientregistration.destroy()
	except:
		pass
	try:
		framepatientcheckout.destroy()
	except:
		pass
	try:
		frameroominfo.destroy()
	except:
		pass
	try:
		frameaddnewward.destroy()
	except:
		pass
	try:
		framestaffinfo.destroy()
	except:
		pass	
	try:
		frameuserinfo.destroy()
	except:
		pass
	try:
		frameaddnewuser.destroy()
	except:
		pass

	if counterpinfo==1:	
		framepatientinformation=Frame(root,width=100,height=100)
		framepatientinformation.pack(side="right",fill=BOTH,expand=TRUE)

		framepatientinformtop=Frame(framepatientinformation,height="200",relief="solid",borderwidth=2,bg="powderblue")
		framepatientinformtop.pack(side=TOP,fill=X);


		labelpatientinfotext=Label(framepatientinformtop,text="Patient Information",bg="powderblue",font=("calibri",23,"bold"))
		labelpatientinfotext.pack(anchor="center")


		framepatientinformleft=Frame(framepatientinformation,height="60",width="300",relief="solid",borderwidth=2)
		framepatientinformleft.pack(side=LEFT,fill=Y);

		labelinputpatientname=Label(framepatientinformleft,text="Input Patient's Name",font=("calibri",17,"bold"))
		labelinputpatientname.pack(anchor=CENTER,pady=20)
		inputpatientnameEntry=Entry(framepatientinformleft,width="20",font=("calibri",15,"bold"))
		inputpatientnameEntry.pack()


		framepatientinforight=Frame(framepatientinformation,height="60",width="300",relief="solid",borderwidth=2)
		framepatientinforight.pack(side=RIGHT,fill=Y);

		labelstatusofdisease=Label(framepatientinforight,text="Status of Disease",font=("calibri",17,"bold"))
		labelstatusofdisease.pack(padx=80,pady=10)
		statusofdiseaseEntry=Entry(framepatientinforight,width="20",font=("calibri",17,"bold"))
		statusofdiseaseEntry.pack()

		labelCheckIn=Label(framepatientinforight,text="Check IN",font=("calibri",17,"bold"))
		labelCheckIn.pack(pady=10)
		CheckInEntry=Entry(framepatientinforight,width="20",font=("calibri",17,"bold"))
		CheckInEntry.pack()

		labelRoomNo=Label(framepatientinforight,text="Room No.",font=("calibri",17,"bold"))
		labelRoomNo.pack(pady=10)
		RoomNoEntry=Entry(framepatientinforight,width="20",font=("calibri",17,"bold"))
		RoomNoEntry.pack()

		labelRoomType=Label(framepatientinforight,text="Room Type",font=("calibri",17,"bold"))
		labelRoomType.pack(pady=10)
		RoomTypeEntry=Entry(framepatientinforight,width="20",font=("calibri",17,"bold"))
		RoomTypeEntry.pack()

		labelBuilding=Label(framepatientinforight,text="Building",font=("calibri",17,"bold"))
		labelBuilding.pack(pady=10)
		BuildingEntry=Entry(framepatientinforight,width="20",font=("calibri",17,"bold"))
		BuildingEntry.pack()


		Updatebutton=Button(framepatientinforight,text="Update",bg="yellow",bd=7,font=("calibri",15,"bold"))
		Updatebutton.pack(side=LEFT,padx=35);


		Closebutton=Button(framepatientinforight,text="Close",bg="yellow",bd=7,font=("calibri",15,"bold"))
		Closebutton.pack(side=LEFT,padx=35);


		framepatientinformcenter=Frame(framepatientinformation,height="60",width="130",relief="solid",borderwidth=2)
		framepatientinformcenter.pack(anchor="center",fill=BOTH,expand=True);

		labelPatientid=Label(framepatientinformcenter,text="Patient ID:    ",font=("calibri",20,"bold"))
		labelPatientid.grid(row=0,column=0,pady=10,sticky="w")
		Patientidentry=Entry(framepatientinformcenter,font=("calibri",20,"bold"))
		Patientidentry.grid(row=0,column=1,padx=1,pady=17,sticky="w")
		labelPatientid=Label(framepatientinformcenter,text="",font=("calibri",20,"bold"))
		labelPatientid.grid(row=0,column=2,sticky="e")




		labelName=Label(framepatientinformcenter,text="Name:       ",font=("calibri",20,"bold"))
		labelName.grid(row=1,column=0,padx=0,pady=17,sticky="w")
		Nameentry=Entry(framepatientinformcenter,font=("calibri",20,"bold"))
		Nameentry.grid(row=1,column=1)

		Gender=StringVar()


		labelGender=Label(framepatientinformcenter,text="Gender:    ",font=("calibri",20,"bold"))
		labelGender.grid(row=2,column=0,sticky="w")
		checkButton1=Checkbutton(framepatientinformcenter,text="Male",font=("calibri",18,"bold"))
		checkButton2=Checkbutton(framepatientinformcenter,text="Female",font=("calibri",18,"bold"))
		checkButton1.grid(row=2,column=1,sticky="w")
		checkButton2.grid(row=2,column=1,sticky="e",padx=90)


		labelAge=Label(framepatientinformcenter,text="Age:         ",font=("calibri",20,"bold"))
		labelAge.grid(row=3,column=0,sticky="w",padx=0,pady=17)
		Ageentry=Entry(framepatientinformcenter,font=("calibri",20,"bold"))
		Ageentry.grid(row=3,column=1)

		labelPhone=Label(framepatientinformcenter,text="Phone:     ",font=("calibri",20,"bold"))
		labelPhone.grid(row=4,column=0,sticky="w",padx=0,pady=17)
		Phoneentry=Entry(framepatientinformcenter,font=("calibri",20,"bold"))
		Phoneentry.grid(row=4,column=1)

		labelAddress=Label(framepatientinformcenter,text="Address:  ",font=("calibri",20,"bold"))
		labelAddress.grid(row=5,column=0,sticky="w",padx=0,pady=17)
		Addressentry=Entry(framepatientinformcenter,font=("calibri",20,"bold"))
		Addressentry.grid(row=5,column=1)


		labelDisease=Label(framepatientinformcenter,text="Disease:   ",font=("calibri",20,"bold"))
		labelDisease.grid(row=6,column=0,sticky="w",padx=0,pady=17)
		Diseaseentry=Entry(framepatientinformcenter,font=("calibri",20,"bold"))
		Diseaseentry.grid(row=6,column=1)


		root.grid_rowconfigure(0,weight=1)
		root.grid_rowconfigure(1,weight=1)
		root.grid_rowconfigure(2,weight=1)
		root.grid_rowconfigure(3,weight=1)
		root.grid_rowconfigure(4,weight=1)
		root.grid_rowconfigure(5,weight=1)
		root.grid_rowconfigure(6,weight=1)
		root.grid_columnconfigure(0,weight=1)
		root.grid_columnconfigure(1,weight=1)








def preg():
	global framemenurightimage
	global framepatientregistration
	global framepatientinformation
	global framepatientcheckout
	global frameroominfo
	global frameaddnewward
	global framestaffinfo
	global frameuserinfo
	global frameaddnewuser
	global counterpreg
	global counterpinfo
	global counterpcheck
	global counterrinfo
	global counteraward
	global countersinfo
	global counteruinfo
	global counterauser
	

	counterpreg+=1
	counterpinfo=0
	counterpcheck=0
	counterrinfo=0
	counteraward=0
	countersinfo=0
	counteruinfo=0
	counterauser=0
	try:
		framemenurightimage.destroy()
	except:
		pass
	try:
		framepatientinformation.destroy()
	except:
		pass
	try:
		framepatientcheckout.destroy()
	except:
		pass	
	try:
		frameroominfo.destroy()
	except:
		pass
	try:
		frameaddnewward.destroy()
	except:
		pass	
	try:
		framestaffinfo.destroy()
	except:
		pass	
	try:
		frameuserinfo.destroy()
	except:
		pass
	try:
		frameaddnewuser.destroy()
	except:
		pass		
	if counterpreg==1:
		framepatientregistration=Frame(root,width=100,height=100)
		framepatientregistration.pack(side="right",fill=BOTH,expand=TRUE)

		frame1=Frame(framepatientregistration,width=1000,height=1200,bg="pink")
		frame1.pack(side=TOP,fill=X)


		frame2=Frame(frame1,bg="powderblue",relief="solid",borderwidth=2,width=1400,height=50)
		frame2.place(x=0,y=0)

		label=Label(frame2,text="Patient Registration",bg="powderblue",font=("calibri",23,"bold"))
		label.place(x=400,y=0)

		frame3=Frame(frame1,width=400,height=200,relief="solid",borderwidth=2)
		frame3.place(x=20,y=80)

		labelRegID=Label(frame3,text="Registration ID",fg="red",font=("calibri",23,"bold"))
		labelRegID.grid(row=0,column=0)

		labelPatient_id=Label(frame3,text="Reg. No:-",font=("calibri",20,"bold"))
		labelPatient_id.grid(row=1,column=0,sticky="w")
		entryfname=Entry(frame3,font=("calibri",15,"bold"))
		entryfname.grid(row=1,column=1,sticky="n")

		labelPatient_id=Label(frame3,text="Date:-",font=("calibri",20,"bold"))
		labelPatient_id.grid(row=2,column=0,sticky="w")
		entryfname=Entry(frame3,font=("calibri",15,"bold"))
		entryfname.grid(row=2,column=1,sticky="n")


		frame4=Frame(frame1,width=300,height=200,relief="solid",borderwidth=2)
		frame4.place(x=530,y=80)

		
		labelRoomtype=Label(frame4,text="Room Type",fg="red",font=("calibri",23,"bold"))
		labelRoomtype.pack(side=TOP,pady="20")
		checkButton1=Checkbutton(frame4,text="VryIMP",font=("calibri",18,"bold"))
		checkButton2=Checkbutton(frame4,text="Normal",font=("calibri",18,"bold"))
		checkButton3=Checkbutton(frame4,text="Medium",font=("calibri",18,"bold"))
		checkButton1.pack()
		checkButton2.pack()
		checkButton3.pack()


		frame5=Frame(frame1,width=800,height=1000,relief="solid",borderwidth=2)
		frame5.place(x=20,y=250)

		label=Label(frame5,text="Patient's Information",fg="red",font=("calibri",23,"bold"))
		label.grid(row=0,column=0)

		labelPatient_id=Label(frame5,text="Patient ID:-",font=("calibri",20,"bold"))
		labelPatient_id.grid(row=1,column=0,sticky="w")
		entryfname=Entry(frame5,font=("calibri",15,"bold"))
		entryfname.grid(row=1,column=1,sticky="n")

		labelPatient_id=Label(frame5,text="Name:-",font=("calibri",20,"bold"))
		labelPatient_id.grid(row=2,column=0,sticky="w")
		entryfname=Entry(frame5,font=("calibri",15,"bold"))
		entryfname.grid(row=2,column=1,sticky="n")

		labelGender=Label(frame5,text="Gender:-",font=("calibri",20,"bold"))
		labelGender.grid(row=3,column=0,sticky="w")
		checkButton1=Checkbutton(frame5,text="Male",font=("calibri",18,"bold"))
		checkButton2=Checkbutton(frame5,text="Female",font=("calibri",18,"bold"))
		checkButton1.grid(row=3,column=1,sticky="w")
		checkButton2.grid(row=3,column=1,sticky="e",padx=0)


		labelPatient_id=Label(frame5,text="Age:-",font=("calibri",20,"bold"))
		labelPatient_id.grid(row=4,column=0,sticky="w")
		entryfname=Entry(frame5,font=("calibri",15,"bold"))
		entryfname.grid(row=4,column=1,sticky="n")

		labelPatient_id=Label(frame5,text="Phone:-",font=("calibri",20,"bold"))
		labelPatient_id.grid(row=5,column=0,sticky="w")
		entryfname=Entry(frame5,font=("calibri",15,"bold"))
		entryfname.grid(row=5,column=1,sticky="n")

		labelPatient_id=Label(frame5,text="Address:-",font=("calibri",20,"bold"))
		labelPatient_id.grid(row=6,column=0,sticky="w")
		entryfname=Entry(frame5,font=("calibri",15,"bold"))
		entryfname.grid(row=6,column=1,sticky="n")

		labelPatient_id=Label(frame5,text="Disease:-",font=("calibri",20,"bold"))
		labelPatient_id.grid(row=7,column=0,sticky="w")
		entryfname=Entry(frame5,font=("calibri",15,"bold"))
		entryfname.grid(row=7,column=1,sticky="n")

		labelPatient_id=Label(frame5,text="Status of Disease:-",font=("calibri",20,"bold"))
		labelPatient_id.grid(row=8,column=0,sticky="w")
		entryfname=Entry(frame5,font=("calibri",15,"bold"))
		entryfname.grid(row=8,column=1,sticky="n")

		frame6=Frame(frame1,width=500,height=500,relief="solid",borderwidth=2)
		frame6.place(x=750,y=80)

		label=Label(frame6,text="Room Information",fg="red",font=("calibri",23,"bold"))
		label.pack(side=TOP)

		label1=Label(frame6,text="Building:-",font=("calibri",20,"bold"))
		label1.pack(side=TOP)
		data=["A","B","C"]

		stringVar=StringVar(root)
		stringVar.set("A")
		dropdownlist=OptionMenu(frame6,stringVar,*data)
		dropdownlist.pack()


		label1=Label(frame6,text="Room No:-",font=("calibri",20,"bold"))
		label1.pack(side=TOP)
		data=["1","2","3"]

		stringVar=StringVar(root)
		stringVar.set("1")
		dropdownlist=OptionMenu(frame6,stringVar,*data)
		dropdownlist.pack()

		label1=Label(frame6,text="Room Type:-",font=("calibri",20,"bold"))
		label1.pack(side=TOP)

		userEntry=Entry(frame6,font=("calibri",15,"bold"))
		userEntry.pack()

		label1=Label(frame6,text="Price:-",font=("calibri",20,"bold"))
		label1.pack(side=TOP)

		userEntry=Entry(frame6,font=("calibri",15,"bold"))
		userEntry.pack()




		frame7=Frame(frame1,width=500,height=100,relief="solid",borderwidth=2)
		frame7.place(x=700,y=500)


		button=Button(frame7,text="Add",fg="red",bd=7,font=("calibri",15,"bold"))
		button.pack(side=LEFT,padx="10",pady="10");

		button=Button(frame7,text="Room",fg="red",bd=7,font=("calibri",15,"bold"))
		button.pack(side=LEFT,padx="10",pady="10");

		button=Button(frame7,text="Close",fg="red",bd=7,font=("calibri",15,"bold"))
		button.pack(side=LEFT,padx="10",pady="10");







framemenuroot=Frame(root,height="190",bg="White")
framemenuroot.pack(side=TOP,fill=X);
framehospitalname=Label(framemenuroot,text="Hospital Name",bg="White",fg="blue",width="35",font=("calibri",27,"bold"))
framehospitalname.pack(anchor="center")

framemenubackground=Frame(root,bg="powderblue",height="60",width="50")
framemenubackground.pack(side=LEFT,fill=Y);
framemenuheading=Label(framemenubackground,text="Menu",fg="White",bg="red",width="25",font=("calibri",18,"bold"))
framemenuheading.pack(anchor="nw")

Buttonpatientregistration=Button(framemenubackground,text="Patient Registration",command=preg,bd=7,font=("calibri",14,"bold"))
Buttonpatientregistration.pack(side="top",fill=X)

Buttonpatientinformation=Button(framemenubackground,text="Patient Information",command=pinfo,bd=7,font=("calibri",14,"bold"))
Buttonpatientinformation.pack(side="top",fill=X)

Buttonpatientcheckout=Button(framemenubackground,text="Patient CheckOut",command=pcheck,bd=7,font=("calibri",14,"bold"))
Buttonpatientcheckout.pack(side="top",fill=X)

Buttonroominformation=Button(framemenubackground,text="Room Information",command=rinfo,bd=7,font=("calibri",14,"bold"))
Buttonroominformation.pack(side="top",fill=X)

Buttonaddnewward=Button(framemenubackground,text="Add New Ward",command=award,bd=7,font=("calibri",14,"bold"))
Buttonaddnewward.pack(side="top",fill=X)

Buttonstaffinformation=Button(framemenubackground,text="Staff Information",command=sinfo,bd=7,font=("calibri",14,"bold"))
Buttonstaffinformation.pack(side="top",fill=X)

Buttonuserinformation=Button(framemenubackground,text="User Information",command=uinfo,bd=7,font=("calibri",14,"bold"))
Buttonuserinformation.pack(side="top",fill=X)

Buttonaddnewuser=Button(framemenubackground,text="Add New User",command=auser,bd=7,font=("calibri",14,"bold"))
Buttonaddnewuser.pack(side="top",fill=X)

Buttonclose=Button(framemenubackground,text="Close",command=onWindowClose,bd=7,font=("calibri",14,"bold"))
Buttonclose.pack(side="left",padx=5)

Buttonlogout=Button(framemenubackground,text="LogOut",bd=7,font=("calibri",14,"bold"))
Buttonlogout.pack(side="right",pady=50)

framemenurightimage=Frame(root,width="1000",height="70",relief="solid",borderwidth=.4)
framemenurightimage.pack(side=RIGHT,fill=BOTH,expand=True) 
image1=PhotoImage(file="hospital1.png")
label=Label(framemenurightimage,image=image1,width="1000",height="600")
label.pack(side=RIGHT)




root.mainloop()