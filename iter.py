from customtkinter import *
from tkinter import *

set_appearance_mode('Dark')
set_default_color_theme('green')

win=CTk()
win.geometry('1920x1080')



def win_control():
	for widget in win.winfo_children():
		widget.destroy()

#player funtion
def player():
	win_control()
	
	#submit function
	def submit():
		a=e1.get()
		b=e2.get()
		c=e3.get()
		win_control()
		
		lab1=CTkLabel(win,text='Welcome',font=('helvetica', 30,'bold'))
		lab1.configure(text=f'Welcome {a}!')
		lab1.place(relx=0.5,rely=0.1,anchor='center')
	
	def combo(v):
		pass
#frame for details
	fr1=CTkFrame(win,fg_color='#1D593E')
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

#position
	e4=CTkComboBox(fr1,values=['GK','CB','FB','CM','ST'],command=combo)
	e4.configure(height=40,width=300,corner_radius=15)
	e4.place(relx=0.5,rely=0.6,anchor='center')
	
#sumbit button
	sub=CTkButton(fr1,text='submit',font=('helvetica',20),corner_radius=20 ,command=submit)
	sub.configure(height=75,width=200)
	sub.place(relx=0.5,rely=0.85,anchor='center')
	
#welcome text
lab=CTkLabel(win,text='WELCOME TO THE TRANSFER MARKET', font=('helvetica', 30,'bold'))

lab.place(relx=0.5,rely=0.3 ,anchor='center')


#player button
play=CTkButton(win,text='player', font=('helvetica', 20 ),corner_radius=20,command=player)
play.configure(height=75,width=200)
play.configure(hover_color='grey')

play.place(relx=0.5 , rely=0.45 , anchor='center')

#manager button
mana=CTkButton(win,text='manager',font=('helvetica',20),corner_radius=20)
mana.configure(height=75,width=200)
mana.configure(hover_color='grey')

mana.place(relx=0.5,rely=0.6,anchor='center')

win.mainloop()