from tkinter import *
from cg import *
def f(s='1'):
	regno=txt.get()
	
	try:
		if s=='h':
			d='More @ t.me/SmartManojBot'
			d+=cg(rn='')  
			d+='\nDiploma too'
		elif regno.isdigit():
			print(len(regno))
			d=dipres(rn=regno)
		else:
			d=cg(rn=regno) 
		print(d)
		res.configure(text=d, justify='left')
	except Exception as e:
		print(e)
def f2():
	v1.set('')
	res.configure(text='')
def f3():
	v1.set('')
	res.configure(text='')	
window = Tk()
global v1
window.title("CGPA - KEC & KPC")
window.geometry('400x250')
lbl = Label(window,text="Register No")
lbl.grid(column=0, row=0)
v1=StringVar()
v1.set("19205089")
txt = Entry(window,width=20,textvariable=v1)
txt.grid(column=1, row=0)
btn = Button(window, text="Submit",width=5,command=f)
btn.grid(column=1,row=1)
btn2 = Button(window, text="Reset",width=5,command=f2)
btn2.grid(column=0,row=1)
btn2 = Button(window, text="About",width=5,command=lambda :f('h'))
btn2.grid(column=2,row=1)
res=Label(window)
res.grid(row=2)
window.mainloop()
