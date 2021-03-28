from tkinter import *
from tkinter import messagebox

def message1 ():
	messagebox.showinfo('hello','Lew Lew')
def message2 ():
	messagebox.showinfo('hello',"Lew Lew ne")
def quit ():
	question = messagebox.askquestion('Quit?','Do you want to quit?',icon='warning')
	if question == 'yes':
		chaukha.destroy()
	else:
		messagebox.showinfo('Return','Return to homescreen')

chaukha = Tk()
chaukha.title("Application")

control1 = Label(chaukha,text='Welcome',font=('Comic Sans MS',22)).pack()
#define windows size
chaukha.geometry('500x500')

#

button = Button(chaukha,text='Click Me',font=('Comic Sans MS',18),command=message1).pack()
quit = Button(chaukha,text='Quit',font=('Comic Sans MS',18),command=quit).pack()



chaukha.mainloop()