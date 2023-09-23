from bl_s import *
from tkinter import *

master = Tk()

Label(master, text='lesson ID').grid(row=0)
Label(master, text='professor ID').grid(row=1)
Label(master, text='lesson Name').grid(row=2)
Label(master, text='lesson vahed').grid(row=3)


ent_id_lesson = Entry(master)
ent_id_professor = Entry(master)
ent_name_lesson = Entry(master)
ent_vahed_lesson = Entry(master)
ent_id_lesson.grid(row=0, column=1)
ent_id_professor.grid(row=1, column=1)
ent_name_lesson.grid(row=2, column=1)
ent_vahed_lesson.grid(row=3, column=1)


from tkinter import messagebox


def record_l():

    i = int(ent_id_lesson.get())
    pid = int(ent_id_professor.get())
    n = ent_name_lesson.get()
    v = int(ent_vahed_lesson.get())
    l = lesson(i,pid,n,v)
    l.insert()
    messagebox.showinfo('ALERT',"recorded lesson to list")


def show_l():

    Lb = Listbox(master)
    L = lesson.select()
    for i in L:
        Lb.insert(END,i)
    Lb.grid(row=5, column=1)


button1 = Button(master, text='record', width=15, command=record_l)
button1.grid(row=4, column=0)

button2= Button(master, text='show', width=15, command=show_l)
button2.grid(row=4, column=1)


mainloop()
