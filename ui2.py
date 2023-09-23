from bl_s import *
from tkinter import *

master = Tk()

Label(master, text='professor ID').grid(row=0)
Label(master, text='professor Name').grid(row=1)
Label(master, text='professor Family').grid(row=2)


ent_id_professor = Entry(master)
ent_name_professor = Entry(master)
ent_family_professor = Entry(master)
ent_id_professor.grid(row=0, column=1)
ent_name_professor.grid(row=1, column=1)
ent_family_professor.grid(row=2, column=1)


from tkinter import messagebox


def record_p():

    i = int(ent_id_professor.get())
    n = ent_name_professor.get()
    f = ent_family_professor.get()
    p = professor(i,n,f)
    p.insert()
    messagebox.showinfo('ALERT',"recorded professor to list")


def show_p():

    Lb = Listbox(master)
    L = professor.select()
    for i in L:
        Lb.insert(END,i)
    Lb.grid(row=4, column=1)


button1 = Button(master, text='record', width=15, command=record_p)
button1.grid(row=3, column=0)

button2 = Button(master, text='show', width=15, command=show_p)
button2.grid(row=3, column=1)

mainloop()
