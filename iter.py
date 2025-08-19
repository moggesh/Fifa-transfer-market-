from customtkinter import *
from tkinter import ttk

set_appearance_mode('Dark')
set_default_color_theme('green')

win=CTk()
win.geometry('1920x1080')

nm=""
ag=""
nt=""
ps=""

def win_control():
	for widget in win.winfo_children():
		widget.destroy()
		
def applic():
	win_control()
	
	fr4=CTkFrame(win,height=550,width=950,corner_radius=20)
	fr4.pack(fill='both',expand=True)
	ll=CTkLabel(fr4,text=f'YOU HAVE SENT YOUR APPLICATION ', font=('helvetica', 40 ,'bold'))
	ll.place(relx=0.5,rely=0.2,anchor='center')
	
	cs=CTkButton(fr4,text='close',font=('helvetica',20),corner_radius=20,command=player)
	cs.configure(height=75,width=200,fg_color='red')
	cs.place(relx=0.45,y=200)
	

#application
def applic1():
	win_control()
	global nm,ag,nt,ps
	
	nm='Thomas Parri'
	ag='20'
	nt='Venezuela'
	ps='CM'
	
	fr4=CTkFrame(win,height=550,width=950,corner_radius=20)
	fr4.pack(fill='both',expand=True)
	ll=CTkLabel(fr4,text=f'YOU HAVE SIGNED {nm} \n TO YOUR TEAM', font=('helvetica', 40 ,'bold'))
	ll.place(relx=0.5,rely=0.2,anchor='center')
	
	cd=CTkButton(fr4,text='close',font=('helvetica',20),corner_radius=20,command=manager)
	cd.configure(height=75,width=200,fg_color='red')
	cd.place(relx=0.45,y=200)

def applic2():
	win_control()
	global nm,ag,nt,ps
	
	nm='Andre Onana'
	ag='29'
	nt='Cameroon'
	ps='GK'
	
	fr4=CTkFrame(win,height=550,width=950,corner_radius=20)
	fr4.pack(fill='both',expand=True)
	ll=CTkLabel(fr4,text=f'YOU HAVE SIGNED {nm} \n TO YOUR TEAM', font=('helvetica', 40 ,'bold'))
	ll.place(relx=0.5,rely=0.2,anchor='center')
	
	cf=CTkButton(fr4,text='close',font=('helvetica',20),corner_radius=20,command=manager)
	cf.configure(height=75,width=200,fg_color='red')
	cf.place(relx=0.45,y=200)

def applic3():
	win_control()
	global nm,ag,nt,ps
	
	nm='Aaron Wan Bissaka'
	ag='27'
	nt='DR Congo'
	ps='FB'
	
	fr4=CTkFrame(win,height=550,width=950,corner_radius=20)
	fr4.pack(fill='both',expand=True)
	ll=CTkLabel(fr4,text=f'YOU HAVE SIGNED {nm} \n TO YOUR TEAM', font=('helvetica', 40 ,'bold'))
	ll.place(relx=0.5,rely=0.2,anchor='center')
	
	cg=CTkButton(fr4,text='close',font=('helvetica',20),corner_radius=20,command=manager)
	cg.configure(height=75,width=200,fg_color='red')
	cg.place(relx=0.45,y=200)
	
def applic4():
	win_control()
	global nm,ag,nt,ps
	
	nm='Kevin De Bruyne'
	ag='34'
	nt='Belgium'
	ps='CM'
	
	fr4=CTkFrame(win,height=550,width=950,corner_radius=20)
	fr4.pack(fill='both',expand=True)
	ll=CTkLabel(fr4,text= f'YOU HAVE SIGNED {nm} \n TO YOUR TEAM', font=('helvetica', 40 ,'bold'))
	ll.place(relx=0.5,rely=0.2,anchor='center')
	
	ch=CTkButton(fr4,text='close',font=('helvetica',20),corner_radius=20,command=manager)
	ch.configure(height=75,width=200,fg_color='red')
	ch.place(relx=0.45,y=200)
	
def applic5():
	win_control()
	global nm,ag,nt,ps
	
	nm='Jonathan Tah'
	ag='29'
	nt='Germany'
	ps='CB'
	
	fr4=CTkFrame(win,height=550,width=950,corner_radius=20)
	fr4.pack(fill='both',expand=True)
	ll=CTkLabel(fr4,text=f'YOU HAVE SIGNED {nm} \n TO YOUR TEAM', font=('helvetica', 40 ,'bold'))
	ll.place(relx=0.5,rely=0.2,anchor='center')
	
	cj=CTkButton(fr4,text='close',font=('helvetica',20),corner_radius=20,command=manager)
	cj.configure(height=75,width=200,fg_color='red')
	cj.place(relx=0.45,y=200)
	
def applic6():
	win_control()
	global nm,ag,nt,ps
	
	nm='Leroy Sane'
	ag='29'
	nt='Germany'
	ps='ST'
	
	fr4=CTkFrame(win,height=550,width=950,corner_radius=20)
	fr4.pack(fill='both',expand=True)
	ll=CTkLabel(fr4,text=f'YOU HAVE SIGNED {nm} \n TO YOUR TEAM', font=('helvetica', 40 ,'bold'))
	ll.place(relx=0.5,rely=0.2,anchor='center')
	
	ck=CTkButton(fr4,text='close',font=('helvetica',20),corner_radius=20,command=manager)
	ck.configure(height=75,width=200,fg_color='red')
	ck.place(relx=0.45,rely=200)
	
def applic7():
	win_control()
	global nm,ag,nt,ps
	
	nm='Trent Alexander Arnold'
	ag='26'
	nt='England'
	ps='FB'
	
	fr4=CTkFrame(win,height=550,width=950,corner_radius=20)
	fr4.pack(fill='both',expand=True)
	ll=CTkLabel(fr4,text=f'YOU HAVE SIGNED {nm} \n TO YOUR TEAM', font=('helvetica', 40 ,'bold'))
	ll.place(relx=0.5,rely=0.2,anchor='center')
	
	cl=CTkButton(fr4,text='close',font=('helvetica',20),corner_radius=20,command=manager)
	cl.configure(height=75,width=200,fg_color='red')
	cl.place(relx=0.45,y=200)
			
#player_funtion
def player():
	win_control()
			
#frame for details
	fr1=CTkFrame(win)
	fr1.configure(height=550,width=950,corner_radius=20)
	fr1.place(relx=0.5,rely=0.4,anchor='center')

	
#heading
	app=CTkLabel(fr1,text='ENTER YOUR DETAILS', font=('helvetica', 40 ,'bold'))
	app.place(relx=0.5,rely=0.2,anchor='center')
	

#name
	e1=CTkEntry(fr1,placeholder_text='enter your name')
	e1.configure(height=40,width=300,corner_radius=15)
	e1.place(relx=0.5,rely=0.3,anchor='center')
	
#nationality	
	e2=CTkEntry(fr1,placeholder_text='enter your nationality')
	e2.configure(height=40,width=300,corner_radius=15)
	e2.place(relx=0.5,rely=0.4,anchor='center')

#age
	e3=CTkEntry(fr1,placeholder_text='enter your age')
	e3.configure(height=40,width=300,corner_radius=15)
	e3.place(relx=0.5,rely=0.5,anchor='center')

#combo box function

	def combo(v):
		global ps
		ps=v

		
		
#position
	e4=CTkComboBox(fr1,values=['GK','CB','FB','CM','ST'],command=combo)
	e4.configure(height=40,width=300,corner_radius=15)
	e4.place(relx=0.5,rely=0.6,anchor='center')
	
	
#submit_function
	def submit():
		global nm,ag,nt
		nm=e1.get()
		ag=e2.get()
		nt=e3.get()
		
		win_control()
		
		fr2=CTkFrame(win)
		fr2.configure()
		fr2.configure(height=550,width=950,corner_radius=20)
		fr2.place(relx=0.5,rely=0.5,anchor='center')
		
		lab1=CTkLabel(fr2,text='Welcome',font=('helvetica', 30,'bold'))
		lab1.configure(text=f'Welcome {ag}!')
		lab1.place(relx=0.5,rely=0.1,anchor='center')
		
		vc=CTkButton(fr2,text='view clubs',font=('helvetica',20),corner_radius=20,command=clubs)
		vc.configure(height=75,width=200)
		vc.place(relx=0.5,rely=0.85,anchor='center')
	
#sumbit button
	sub=CTkButton(fr1,text='submit',font=('helvetica',20),corner_radius=20 ,command=submit)
	sub.configure(height=75,width=200)
	sub.place(relx=0.5,rely=0.85,anchor='center')
	
#end of player function


#club_function

def clubs():
	win_control()
	
	ctxt=CTkLabel(win,text='AVAILABLE CLUBS', font=('helvetica', 40 ,'bold'))
	ctxt.place(relx=0.5,rely=0.1,anchor='center')
	
	#scrolling frame
	fr3=CTkScrollableFrame(win)
	fr3.configure(height=550,width=950,corner_radius=20)
	fr3.place(relx=0.5,rely=0.5,anchor='center')
	
	#club frames 
	#1
	clb1=CTkFrame(fr3,height=200,width=850,corner_radius=20)
	clb1.configure(border_width=2)
	clb1.pack(fill='both',expand=True,pady=5)
	
	#2
	
	clb2=CTkFrame(fr3,height=200,width=850,corner_radius=20)
	clb2.configure(border_width=2)
	clb2.pack(fill='both',expand=True,side='bottom',pady=5)
	
	#3
	
	clb3=CTkFrame(fr3,height=200,width=850,corner_radius=20)
	clb3.configure(border_width=2)
	clb3.pack(fill='both',expand=True,side='bottom',pady=5)
	
	#4
	
	clb4=CTkFrame(fr3,height=200,width=850,corner_radius=20)
	clb4.configure(border_width=2)
	clb4.pack(fill='both',expand=True,side='bottom',pady=5)
	
	#5
	
	clb5=CTkFrame(fr3,height=200,width=850,corner_radius=20)
	clb5.configure(border_width=2)
	clb5.pack(fill='both',expand=True,side='bottom',pady=5)
	
	#6
	
	clb6=CTkFrame(fr3,height=200,width=850,corner_radius=20)
	clb6.configure(border_width=2)
	clb6.pack(fill='both',expand=True,side='bottom',pady=5)
	
	#7
	
	clb7=CTkFrame(fr3,height=200,width=850,corner_radius=20)
	clb7.configure(border_width=2)
	clb7.pack(fill='both',expand=True,side='bottom',pady=5)
	
	#8
	
	clb8=CTkFrame(fr3,height=200,width=850,corner_radius=20)
	clb8.configure(border_width=2)
	clb8.pack(fill='both',expand=True,side='bottom',pady=5)
	
	#9
	
	clb9=CTkFrame(fr3,height=200,width=850,corner_radius=20)
	clb9.configure(border_width=2)
	clb9.pack(fill='both',expand=True,side='bottom',pady=5)
	
	
	
	#club 1
	clb_nam1=CTkLabel(clb1,text='NEWCASTLE UNITED FC',font=('Arial',35,'bold'),compound='left')
	clb_nam1.place(x=30,y=20)
	dsc1=CTkLabel(clb1,text='Preimer League',font=('Arial',18),compound='bottom')
	dsc1.place(x=30,y=60)
	sb1=CTkButton(clb1,text='APPLY',font=('helvetica',20),corner_radius=20,command=applic)
	sb1.configure(height=55,width=150)
	sb1.pack(side='right',padx=15,pady=25)
	
	#club2
	clb_nam2=CTkLabel(clb2,text='SPORTING CP',font=('Arial',35,'bold'),compound='left')
	clb_nam2.place(x=30,y=20)
	dsc2=CTkLabel(clb2,text='Liga Portugal',font=('Arial',18),compound='bottom')
	dsc2.place(x=30,y=60)
	sb2=CTkButton(clb2,text='APPLY',font=('helvetica',20),corner_radius=20,command=applic)
	sb2.configure(height=55,width=150)
	sb2.pack(side='right',padx=15,pady=25)
	
	#club3
	clb_nam3=CTkLabel(clb3,text='UDINESE CALCIO',font=('Arial',35,'bold'),compound='left')
	clb_nam3.place(x=30,y=20)
	dsc3=CTkLabel(clb3,text='Serie A',font=('Arial',18),compound='bottom')
	dsc3.place(x=30,y=60)
	sb3=CTkButton(clb3,text='APPLY',font=('helvetica',20),corner_radius=20,command=applic)
	sb3.configure(height=55,width=150)
	sb3.pack(side='right',padx=15,pady=25)
	
	#club4
	clb_nam4=CTkLabel(clb4,text='FC PORTO',font=('Arial',35,'bold'),compound='left')
	clb_nam4.place(x=30,y=20)
	dsc4=CTkLabel(clb4,text='Liga Portugal',font=('Arial',18),compound='bottom')
	dsc4.place(x=30,y=60)
	sb4=CTkButton(clb4,text='APPLY',font=('helvetica',20),corner_radius=20,command=applic)
	sb4.configure(height=55,width=150)
	sb4.pack(side='right',padx=15,pady=25)
	
	#club5
	clb_nam5=CTkLabel(clb5,text='GALATASARAY CK',font=('Arial',35,'bold'),compound='left')
	clb_nam5.place(x=30,y=20)
	dsc5=CTkLabel(clb5,text='Trendyol Super Lig',font=('Arial',18),compound='bottom')
	dsc5.place(x=30,y=60)
	sb5=CTkButton(clb5,text='APPLY',font=('helvetica',20),corner_radius=20,command=applic)
	sb5.configure(height=55,width=150)
	sb5.pack(side='right',padx=15,pady=25)
	
	#club6
	clb_nam6=CTkLabel(clb6,text='SEVILLA FC',font=('Arial',35,'bold'),compound='left')
	clb_nam6.place(x=30,y=20)
	dsc6=CTkLabel(clb6,text='La Liga',font=('Arial',18),compound='bottom')
	dsc6.place(x=30,y=60)
	sb6=CTkButton(clb6,text='APPLY',font=('helvetica',20),corner_radius=20,command=applic)
	sb6.configure(height=55,width=150)
	sb6.pack(side='right',padx=15,pady=25)
	
	#club7
	clb_nam7=CTkLabel(clb7,text='RB LEIPZIG',font=('Arial',35,'bold'),compound='left')
	clb_nam7.place(x=30,y=20)
	dsc7=CTkLabel(clb7,text='Bundesliga',font=('Arial',18),compound='bottom')
	dsc7.place(x=30,y=60)
	sb7=CTkButton(clb7,text='APPLY',font=('helvetica',20),corner_radius=20,command=applic)
	sb7.configure(height=55,width=150)
	sb7.pack(side='right',padx=15,pady=25)
	
	#club8
	clb_nam8=CTkLabel(clb8,text='GETAFE CF',font=('Arial',35,'bold'),compound='left')
	clb_nam8.place(x=30,y=20)
	dsc8=CTkLabel(clb8,text='La Liga',font=('Arial',18),compound='bottom')
	dsc8.place(x=30,y=60)
	sb8=CTkButton(clb8,text='APPLY',font=('helvetica',20),corner_radius=20,command=applic)
	sb8.configure(height=55,width=150)
	sb8.pack(side='right',padx=15,pady=25)
	
	#club9
	clb_nam9=CTkLabel(clb9,text='SS LAZIO',font=('Arial',35,'bold'),compound='left')
	clb_nam9.place(x=30,y=20)
	dsc9=CTkLabel(clb9,text='Serie A',font=('Arial',18),compound='bottom')
	dsc9.place(x=30,y=60)
	sb9=CTkButton(clb9,text='APPLY',font=('helvetica',20),corner_radius=20,command=applic)
	sb9.configure(height=55,width=150)
	sb9.pack(side='right',padx=15,pady=25)


#applications function
def aply():
	win_control()
	
	avp=CTkLabel(win,text='AVAILABLE PLAYERS', font=('helvetica', 40 ,'bold'))
	avp.place(relx=0.5,rely=0.1,anchor='center')
	
	#scrollable frame 
	fr6=CTkScrollableFrame(win)
	fr6.configure(height=550,width=950,corner_radius=20)
	fr6.place(relx=0.5,rely=0.5,anchor='center')
	
	
	#player list frames
	#1
	pll1=CTkFrame(fr6,height=200,width=850,corner_radius=20)
	pll1.configure(border_width=2)
	pll1.pack(fill='both',expand=True,pady=5)
	
	#2
	
	pll2=CTkFrame(fr6,height=200,width=850,corner_radius=20)
	pll2.configure(border_width=2)
	pll2.pack(fill='both',expand=True,side='bottom',pady=5)
	
	#3

	pll3=CTkFrame(fr6,height=200,width=850,corner_radius=20)
	pll3.configure(border_width=2)
	pll3.pack(fill='both',expand=True,side='bottom',pady=5)
	
	#4
	pll4=CTkFrame(fr6,height=200,width=850,corner_radius=20)
	pll4.configure(border_width=2)
	pll4.pack(fill='both',expand=True,pady=5)
	
	#5
	
	pll5=CTkFrame(fr6,height=200,width=850,corner_radius=20)
	pll5.configure(border_width=2)
	pll5.pack(fill='both',expand=True,side='bottom',pady=5)
	
	#6

	pll6=CTkFrame(fr6,height=200,width=850,corner_radius=20)
	pll6.configure(border_width=2)
	pll6.pack(fill='both',expand=True,side='bottom',pady=5)	
	
	#7
	pll7=CTkFrame(fr6,height=200,width=850,corner_radius=20)
	pll7.configure(border_width=2)
	pll7.pack(fill='both',expand=True,pady=5)
	
	
	#players list
	
	#player 1
	pll_nam1=CTkLabel(pll1,text='Thomas Parri',font=('Arial',35,'bold'),compound='left')
	pll_nam1.place(x=30,y=20)
	
	pos_nam1=CTkLabel(pll1,text='(CM)',font=('Arial',35,'bold'),compound='left')
	pos_nam1.place(x=450,y=20)	
	
	nat1=CTkLabel(pll1,text='Venezuela',font=('Arial',18),compound='bottom')
	nat1.place(x=30,y=60)
	
	age1=CTkLabel(pll1,text='20 y/o',font=('Arial',18))
	age1.place(x=250,y=60)	
	
	sg1=CTkButton(pll1,text='SIGN',font=('helvetica',20),corner_radius=20,command=applic1)
	sg1.configure(height=55,width=150)
	sg1.pack(side='right',padx=15,pady=25)
	
	#player 2
	pll_nam2=CTkLabel(pll2,text='Andre Onana',font=('Arial',35,'bold'),compound='left')
	pll_nam2.place(x=30,y=20)
	
	pos_nam2=CTkLabel(pll2,text='(GK)',font=('Arial',35,'bold'),compound='left')
	pos_nam2.place(x=450,y=20)

	nat2=CTkLabel(pll2,text='Cameroon',font=('Arial',18),compound='bottom')
	nat2.place(x=30,y=60)
	
	age2=CTkLabel(pll2,text='29 y/o',font=('Arial',18))
	age2.place(x=250,y=60)
	
	sg2=CTkButton(pll2,text='SIGN',font=('helvetica',20),corner_radius=20,command=applic2)
	sg2.configure(height=55,width=150)
	sg2.pack(side='right',padx=15,pady=25)
	
	#player 3
	pll_nam3=CTkLabel(pll3,text='Aaron Wan Bissaka',font=('Arial',35,'bold'),compound='left')
	pll_nam3.place(x=30,y=20)
	
	pos_nam3=CTkLabel(pll3,text='(FB)',font=('Arial',35,'bold'),compound='left')
	pos_nam3.place(x=450,y=20)
	
	nat3=CTkLabel(pll3,text='DR Congo',font=('Arial',18),compound='bottom')
	nat3.place(x=30,y=60)
	
	age3=CTkLabel(pll3,text='27 y/o',font=('Arial',18))
	age3.place(x=250,y=60)
	
	sg3=CTkButton(pll3,text='SIGN',font=('helvetica',20),corner_radius=20,command=applic3)
	sg3.configure(height=55,width=150)
	sg3.pack(side='right',padx=15,pady=25)
	
	#player 4
	pll_nam4=CTkLabel(pll4,text='Kevin De Bruyne',font=('Arial',35,'bold'),compound='left')
	pll_nam4.place(x=30,y=20)
	
	pos_nam4=CTkLabel(pll4,text='(CM)',font=('Arial',35,'bold'),compound='left')
	pos_nam4.place(x=450,y=20)	
	
	nat4=CTkLabel(pll4,text='Belgium',font=('Arial',18),compound='bottom')
	nat4.place(x=30,y=60)
	
	age4=CTkLabel(pll4,text='34 y/o',font=('Arial',18))
	age4.place(x=250,y=60)
	
	sg4=CTkButton(pll4,text='SIGN',font=('helvetica',20),corner_radius=20,command=applic4)
	sg4.configure(height=55,width=150)
	sg4.pack(side='right',padx=15,pady=25)
	
	#player 5
	pll_nam5=CTkLabel(pll5,text='Jonathan Tah',font=('Arial',35,'bold'),compound='left')
	pll_nam5.place(x=30,y=20)
	
	pos_nam5=CTkLabel(pll5,text='(CB)',font=('Arial',35,'bold'),compound='left')
	pos_nam5.place(x=450,y=20)
	
	nat5=CTkLabel(pll5,text='Germany',font=('Arial',18),compound='bottom')
	nat5.place(x=30,y=60)
	
	age5=CTkLabel(pll5,text='29 y/o',font=('Arial',18))
	age5.place(x=250,y=60)
	
	sg5=CTkButton(pll5,text='SIGN',font=('helvetica',20),corner_radius=20,command=applic5)
	sg5.configure(height=55,width=150)
	sg5.pack(side='right',padx=15,pady=25)
	
	#player 6
	pll_nam6=CTkLabel(pll6,text='Leroy Sane',font=('Arial',35,'bold'),compound='left')
	pll_nam6.place(x=30,y=20)

	pos_nam6=CTkLabel(pll6,text='(ST)',font=('Arial',35,'bold'),compound='left')
	pos_nam6.place(x=450,y=20)

	nat6=CTkLabel(pll6,text='Germany',font=('Arial',18),compound='bottom')
	nat6.place(x=30,y=60)
	
	age6=CTkLabel(pll6,text='29 y/o',font=('Arial',18))
	age6.place(x=250,y=60)
	
	sg6=CTkButton(pll6,text='SIGN',font=('helvetica',20),corner_radius=20,command=applic6)
	sg6.configure(height=55,width=150)
	sg6.pack(side='right',padx=15,pady=25)
	
	#player 7
	pll_nam7=CTkLabel(pll7,text='Trent Alexander Arnold',font=('Arial',35,'bold'),compound='left')
	pll_nam7.place(x=30,y=20)
	
	pos_nam7=CTkLabel(pll7,text='(FB)',font=('Arial',35,'bold'),compound='left')
	pos_nam7.place(x=450,y=20)	
	
	nat7=CTkLabel(pll7,text='England',font=('Arial',18),compound='bottom')
	nat7.place(x=30,y=60)
	
	age7=CTkLabel(pll7,text='26 y/o',font=('Arial',18))
	age7.place(x=250,y=60)
	
	sg7=CTkButton(pll7,text='SIGN',font=('helvetica',20),corner_radius=20,command=applic7)
	sg7.configure(height=55,width=150)
	sg7.pack(side='right',padx=15,pady=25)
	

	
	


	
#manager function
def manager():
	win_control()
	
	fr5=CTkFrame(win,height=550,width=950,corner_radius=20)
	fr5.place(relx=0.5,rely=0.4,anchor='center')
	
	vt=CTkButton(fr5,text='My team',font=('helvetica',20),corner_radius=20,command=tab)
	vt.configure(height=75,width=200)
	vt.place(relx=0.5,rely=0.35,anchor='center')
	
	ap=CTkButton(fr5,text='players',font=('helvetica',20),corner_radius=20,command=aply)
	ap.configure(height=75,width=200)
	ap.place(relx=0.5,rely=0.55,anchor='center')
	
	rp=CTkButton(fr5,text='release',font=('helvetica',20),corner_radius=20)
	rp.configure(height=75,width=200,fg_color='red')
	rp.place(relx=0.5,rely=0.75,anchor='center')


	
	
#Treeview function
def tab():
	fr7=CTkFrame(win,height=550,width=950)
	fr7.pack()
	
	def ins():
		global nm,ag,nt,ps
		win_control()
	
	
	
		p1=('Christian Eriksen','33','Denmark','CM')
		p2=('Takehiro Tomiyasu','26','Japan','FB')
		p3=('Victor Gyorkeres','31','Sweeden','ST')	
		p4=('Kyle Walker','35','England','FB')
		p5=('Thiago Silva','40','Brazil','CB')
		p6=('Keylor Navas','38','Costa Rica','GK')
		p7=('Willian','37','Brazil','CM')
		
		l=[p1,p2,p3,p4,p5,p6,p7]

		for i in l:
			tree.insert('',index=0,values=(i))
		
		
		
	tree=ttk.Treeview(fr7,columns=('one','two','three','four'),show='headings')
	
	tree.heading('one',text='name')
	tree.heading('two',text='age')
	tree.heading('three',text='nationality')
	tree.heading('four',text='position')
	
	ins()
	
	tree.pack(fill='both',expand=True)
#-----Main-----

#welcome text
lab=CTkLabel(win,text='WELCOME TO THE TRANSFER MARKET', font=('helvetica', 30,'bold'))

lab.place(relx=0.5,rely=0.3 ,anchor='center')


#player button

play=CTkButton(win,text='player', font=('helvetica', 20 ),corner_radius=20,command=player)
play.configure(height=75,width=200)
play.place(relx=0.5 , rely=0.45 , anchor='center')

#manager button
mana=CTkButton(win,text='manager',font=('helvetica',20),corner_radius=20,command=manager)	
mana.configure(height=75,width=200)	
mana.place(relx=0.5,rely=0.6,anchor='center')
	


win.mainloop()