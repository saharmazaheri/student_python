from bl_s import *
from tkinter import *

master = Tk()

Label(master, text='student ID').grid(row=0)
Label(master, text='student Name').grid(row=1)
Label(master, text='student Family').grid(row=2)


ent_id_student = Entry(master)
ent_name_student = Entry(master)
ent_family_student = Entry(master)
ent_id_student.grid(row=0, column=1)
ent_name_student.grid(row=1, column=1)
ent_family_student.grid(row=2, column=1)


from tkinter import messagebox


def record_s():

    i = int(ent_id_student.get())
    n = ent_name_student.get()
    f = ent_family_student.get()
    s = student(i,n,f)
    s.insert()
    messagebox.showinfo('ALERT',"recorded Student to list")


def show_s():

    Lb = Listbox(master)
    L = student.select()
    for i in L:
        Lb.insert(END, i)
    Lb.grid(row=4, column=1)


button1 = Button(master, text='record', width=15, command=record_s)
button1.grid(row=3, column=0)

button2 = Button(master, text='show', width=15, command=show_s)
button2.grid(row=3, column=1)

mainloop()
