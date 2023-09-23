from bl_s import *
from tkinter import *

master = Tk()
Label(master, text='lesson ID :').grid(row=0)
Label(master, text='lesson name :').grid(row=1)
Label(master, text='profsor name :').grid(row=2)
Label(master, text='<<_______________Score List_______________>>').grid(row=4, column=1)


ent_id_lessons = Entry(master)
ent_id_lessons.grid(row=0, column=1)


from tkinter import messagebox
from tkinter import ttk

l1 = LabelFrame(master)
l2 = LabelFrame(master)

canvas=Canvas(l1)
canvas.pack(side=LEFT,fill="both",expand="yes")

scroll=ttk.Scrollbar(l1,orient="vertical",command=canvas.yview)
scroll.pack(side=RIGHT,fill="y")

canvas.configure(yscrollcommand=scroll.set)

canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

frmee = Frame(canvas)
canvas.create_window((0,0),window=frmee)

l1.grid(row=5,column=1, padx=10, pady=10)
l2.grid(row=5,column=1, padx=10, pady=10)



s = 0
mark = []
L = student.select1()

for i in L:
    Label(frmee, text=i).grid(row=s,column=0)
    mark.append(Entry(frmee))
    mark[s].grid(row=s,column=1)
    s += 1


def search_l():
    
    global cd
    code= int(ent_id_lessons.get())
    cd=code
    s1 = lesson.search1(code)
    s2 = professor.search3(code)
    Label(master, text=s1).grid(row=1, column=1)
    Label(master, text=s2).grid(row=2, column=1)
    messagebox.showinfo('ALERT', "search")


def record_m():

    x=0
    for i in mark:
        a1=L[x][0]
        a2=i.get()
        a3=cd
        s=scor(a1,a2,a3)
        s.insert()
        x+=1
    messagebox.showinfo('ALERT', "record scores")


def avrg():
    
    c = lesson([0], [1], [2],[3])
    c.avg()
    messagebox.showinfo('ALERT', "record average")


button1 = Button(master, text='search', width=10, command=search_l)
button1.grid(row=0, column=2)

button2 = Button(master, text='record', width=10, command=record_m)
button2.grid(row=12, column=2)

button2 = Button(master, text='average', width=10, command=avrg)
button2.grid(row=12, column=0)

mainloop()
